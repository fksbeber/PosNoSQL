from typing import List, Optional
from redis import Redis

GLOBAL_SCORE = 'scores'
GAME = 'game'
USER = 'user:%.2d'
CARD = 'card:%.2d'
SCORE = 'score:%.2d'

def create_connection(host: str = 'localhost', 
                      port: int = 6379,
                      password: Optional[str] = None) -> Redis:
    """Create a connection to redis

    Args:
        host: redis ip address
        port: redis port 
        password: redis password
    
    Returns:
        A redis object
    """
    conn = Redis(host, port, password=password)
    conn.flushdb()
    return conn

def create_numbers(conn: Redis, size: int = 50) -> None:
    """Create a game with all possible numbers

    Args:
        conn: redis object
        size: number of unique numbers in the game
    """
    for value in range(1, size+1):
        conn.sadd(GAME, value)

def create_card(conn: Redis, number: int, size: int = 15) -> str:
    """Create a card with 'size' numbers

    Args:
        conn: redis object
        number: card unique identifier
        size: number of unique numbers in the card

    Returns:
        Card unique name
    """
    name = CARD % number
    for random_number in conn.srandmember(GAME, number=size):
        conn.sadd(name, random_number)

    return name

def create_score(conn: Redis, number: int) -> str:
    """Create a score object

    Args:
        conn: redis object
        number: score unique identifier

    Returns:
        Score unique name
    """
    name = SCORE % number
    conn.zadd(GLOBAL_SCORE, { name: 0})
    return name

def create_user(conn: Redis, number: int) -> str:
    """Create a user with a name, card and score

    Args:
        conn: redis object
        number: user unique identifier

    Returns:
        User unique name
    """
    name = USER % number
    conn.hset(name, 'name', name.replace(':', ''))
    conn.hset(name, 'card', create_card(conn, number))
    conn.hset(name, 'score', create_score(conn, number))
    return name

def update_score(conn: Redis, users: List[str], number: int) -> None:
    """Update the scores of all users

    Iterate all users and increase the score by one if the drawn number is in the card.

    Args:
        conn: redis object
        users: list of all users
        number: drawn number
    """
    for user in users:
        score_key = conn.hget(user, 'score') 
        card_key = conn.hget(user, 'card')
        if conn.sismember(card_key, number) == 1:
            conn.zincrby(GLOBAL_SCORE, 1, score_key)

def draw_number(conn: Redis) -> int:
    """Draw the game's next number

    Args:
        conn: redis object

    Returns:
        Game's next number
    """ 
    return int(conn.spop(GAME))

def check_winners(conn: Redis, score: int = 15) -> List[str]:
    """Check the players that won the game

    A player wins when it has a score equal to 'score'

    Args:
        conn: redis object
        score: required score to win the game

    Returns:
        A list with all winners
    """
    scores = conn.zrevrangebyscore(GLOBAL_SCORE, score, score)
    winners: List[str] = list()
    for s in scores:
        number = int(s.decode('utf8').split(':')[1])
        user = conn.hget(USER % number, 'name')
        winners.append(user.decode('utf8'))

    return winners

def create_game() -> None:
    # create a connection to redis server
    conn: Redis = create_connection()
    
    # create the numbers of the game
    create_numbers(conn, size=50)

    # create all users
    users: List[str] = list()
    for i in range(1, 51):
        u = create_user(conn, i)
        users.append(u)
    
    # start the game loop
    print('Game started...')
    winners: List[str] = list()
    while len(winners := check_winners(conn)) == 0:
        # draw the next number
        number: int = draw_number(conn)
        # update the scores
        update_score(conn, users, number)
        # log the numbers at each round
        print('- number \'{}\' was drawn from the pool'.format(number))
    
    print('The game has {} winner(s):'.format(len(winners)))
    for w in winners:
        print('- {}'.format(w))

if __name__ == '__main__':
    create_game()