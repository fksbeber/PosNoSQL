# Exercício 1 
> :play https://guides.neo4j.com/intro-neo4j-exercises/01.html

## 1.1 Write a query to retrieve all nodes from the database.
```
match (n) return n
```
## 1.2 Write a query to display the schema of your database.
```
call db.schema()
```
## 1.3 Write a query to retrieve all Person nodes.
```
match (p:Person) return p 
```
## 1.4 Write a query to retrieve all Movie nodes.
```
match (m:Movie) return m 
```

# Exercício 2 
> :play https://guides.neo4j.com/intro-neo4j-exercises/02.html

## 2.1 Retrieve all Movie nodes that have a released property value of 2003.
```
match (m:Movie {released: 2003}) return m
```
## 2.2 View the results you just viewed in Neo4j Browser as a table.
```
Clicar no ícone para ver o resultado em forma de tabela 
```
### 2.2.1 (Taking it further) Retrieve all movie nodes in the database and view the data as a table. Notice the values for the released property for each node.
```
match (m:Movie) return m 
```

### 2.2.2 (Taking it further) Try querying the graph using different years.
```
match (m:Movie {released: 2004}) return m
```

## 2.3 Query the database for all property keys.
```
call db.propertyKeys
```

## 2.4 Retrieve all Movies released in 2006, returning their titles.
```
match (m:Movie {released: 2006}) return m.title 
```

### 2.4.1 (Taking it further) Retrieve all Movie nodes and view them as a table. Observe the properties that Movie nodes have.
```
match (m:Movie) return m 
```

### 2.4.2 (Taking it further) Query the database using a different year and also return more property values.
```
match (m:Movie) return m.title, m.tagline
```

## 2.5 Retrieve all Movie nodes from the database and return the title, released, and tagline values.
```
match (m:Movie) return m.title, m.released, m.tagline
```

## 2.6 Modify the query you just ran so that the headings for the columns of the table returned are more descriptive.
```
match (m:Movie) return m.title as `movie title`, m.released as released, m.tagline as tagline
```

# Exercício 3 
> :play https://guides.neo4j.com/intro-neo4j-exercises/03.html

## 3.1 Display the schema of the database.
```
call db.schema()
```

## 3.2 Retrieve all people who wrote the movie Speed Racer.
```
match (p:Person)-[:WROTE]->(:Movie{title: 'Speed Racer'}) return p.name 
```
### 3.2.1 (Taking it further) Retrieve all people who have written other movies.
```
match (p:Person)-[:WROTE]->(:Movie) return p.name
```

### 3.2.2 (Taking it further) Retrieve people who have acted in a particular movie.
```
match (p:Person)-[:ACTED_IN]->(:Movie{title: 'The Matrix'}) return p.name
```

### 3.2.3 (Taking it further) Retrieve people who have directed a particular movie.
```
match (p:Person)-[:DIRECTED]->(:Movie{title: 'Jerry Maguire'}) return p.name
```

## 3.3 Retrieve all movies connected with Tom Hanks.
```
match (Person{name: 'Tom Hanks'})-->(m:Movie) return m.title
```

### 3.3.1 (Taking it further) Retrieve all movies connected with another actor.
```
match (Person{name: 'Christian Bale'})-->(m:Movie) return m.title
```

### 3.3.2 (Taking it further) Retrieve all people connected with a particular movie.
```
match (p:Person)-->(Movie{title:'Cast Away'}) return p.name
```

## 3.4 Modify the query that you just executed to return the type information about the relationships between Tom Hanks and the movies.
```
match (Person{name: 'Tom Hanks'})-[r]->(m:Movie) return m.title, type(r)
```

### 3.4.1 (Taking it further) Retrieve the relationship information about a different actor.
```
match (Person{name: 'Keanu Reeves'})-[r]->(m:Movie) return m.title, type(r)
```

## 3.5 Retrieve information about the roles that Tom Hanks played.
```
match (:Person{name: 'Tom Hanks'})-[r:ACTED_IN]->(m:Movie) return m.title, r.roles
```

### 3.5.1 (Taking it further) Retrieve all roles for a different actor.
```
match (:Person{name: 'Helen Hunt'})-[r:ACTED_IN]->(m:Movie) return m.title, r.roles
```

### 3.5.2 (Taking it further) Retrieve all roles played for a particular movie.
```
match (p:Person)-[r:ACTED_IN]->(:Movie{title: 'Cloud Atlas'}) return p.name, r.roles
```

# Exercício 4 
> :play https://guides.neo4j.com/intro-neo4j-exercises/04.html

## 4.1 Retrieve all movies that Tom Cruise acted in and return their titles.
```
match (m:Movie)<-[ACTED_IN]-(p:Person)
where p.name = 'Tom Cruise'
return m.title as Movie 
```

## 4.2 Retrieve all people that were born in the 70’s and return their names and year born.
```
match (m:Movie)<--(p:Person)
where p.born >= 1970 and p.born < 1980
return p.name as Name, p.born as `Year Born`
```

## 4.3 Retrieve the actors who acted in the movie The Matrix who were born after 1960, and return their names and year born.
```
match (m:Movie)<-[:ACTED_IN]-(p:Person)
where p.born 1960 and m.title='The Matrix'
return p.name as Name, p.born as `Year Born`
```

## 4.4 Retrieve all movies released in 2000 by testing the node label and the released property, returning the movie titles.
```
match (m)
where m:Movie and m.released=2000
return m.title as Title
```

## 4.5 Retrieve all people that wrote movies by testing the relationship between two nodes, returning the names of the people and the titles of the movies.
```
match (p)-[r]->(m)
where m:Movie and p:Person and type(r) = 'WROTE'
return p.name as Name, m.title as Movie
```

## 4.6 Retrieve all people in the graph that do not have a born property, returning their names.
```
match (p:Person)
where not exists(p.born)
return p.name as Name
```

## 4.7 Retrieve all people related to movies where the relationship has the rating property, then return their name, movie title, and the rating.
```
match (p:Person)-[r]->(m:Movie)
where exists(r.rating)
return p.name as Name, m.title as Movie, r.rating as Rating
```

## 4.8 Retrieve all actors whose name begins with James, returning their names.
```
match (p:Person)-[:ACTED_IN]->(:Movie)
where p.name=~'James.*'
return p.name as Name
```

## 4.9 Retrieve all REVIEWED relationships from the graph where the summary of the review contains the string fun, returning the movie title reviewed and the rating and summary of the relationship.
```
match (p:Person)-[r:REVIEWED]->(m:Movie)
where toLower(r.summary) CONTAINS 'fun'
return m.title as Movie, r.summary as Review, r.rating as Rating
```

### 4.9.1 (Taking it further) Retrieve all movies in the database that have love in their tagline and return the movie titles
```
match (m:Movie)
where m.tagline CONTAINS 'love'
return m.title as Movie
```

### 4.9.2 (Taking it further) Retrieve movies in the database, specifying a regular expression for the content of the tagline.
```
match (m:Movie)
where m.tagline contains 'story'
return m.title as Movie
```

## 4.10 Retrieve all people who have produced a movie, but have not directed a movie, returning their names and the movie titles.
```
match (p:Person)-[:PRODUCED]->(m:Movie)
where not ((p)-[:DIRECTED]->(:Movie))
return p.name as Name, m.title as Movie
```

## 4.11 Retrieve the movies and their actors where one of the actors also directed the movie, returning the actors names, the director’s name, and the movie title.
```
match (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person)
where exists((p2)-[:DIRECTED]->(m))
return p1.name as Name, p2.name as Director, m.title as Movie
```

## 4.12 Retrieve all movies that were released in the years 2000, 2004, and 2008, returning their titles and release years.
```
match (m:Movie)
where m.released in [2000,2004,2008]
return m.title as Movie, m.released as Year
```

## 4.13 Retrieve the movies that have an actor’s role that is the name of the movie, return the movie title and the role.
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title in r.roles
return m.title as Movie, p.name as Actor
```

# Exercício 5 
> :play https://guides.neo4j.com/intro-neo4j-exercises/05.html

## 5.1 Write a Cypher query that retrieves all movies that Gene Hackman has acted it, along with the directors of the movies. In addition, retrieve the actors that acted in the same movies as Gene Hackman. Return the name of the movie, the name of the director, and the names of actors that worked with Gene Hackman.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p2:Person), (p3:Person)-[:ACTED_IN]->(m:Movie)
where p.name = 'Gene Hackman'
return m.title as Movie, p2.name as Director, p3.name as Actor
```

## 5.2 Retrieve all nodes that the person named James Thompson directly has the FOLLOWS relationship in either direction.
```
match (p1:Person)-[:FOLLOWS]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

## 5.3 Modify the query to retrieve nodes that are exactly three hops away.
```
match (p1:Person)-[:FOLLOWS*3]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

## 5.4 Modify the query to retrieve nodes that are one and two hops away.
```
match (p1:Person)-[:FOLLOWS*1..2]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

## 5.5 Modify the query to retrieve all nodes that are connected to James Thompson by a Follows relationship no matter how many hops are required.
```
match (p1:Person)-[:FOLLOWS*]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

## 5.6 Write a Cypher query to retrieve all people in the graph whose name begins with Tom and optionally retrieve all people named Tom who directed a movie.
```
match (p:Person)
where p.name =~ 'Tom.*' 
optional match (p)-[:DIRECTED]->(m:Movie)
return p.name as Name, m.title as Movie
```

## 5.7 Retrieve actors and the movies they have acted in, returning each actor’s name and the list of movies they acted in.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
return p.name as Name, collect(m.title) as `Movie List`
```

## 5.8 Retrieve all movies that Tom Cruise has acted in and the co-actors that acted in the same movie, returning the movie title and the list of co-actors that Tom Cruise worked with.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person)
where p.name = 'Tom Cruise'
return m.title as Movie, collect(p2.name) as `Co-Actors`
```

## 5.9 Retrieve all people who reviewed a movie, returning the list of reviewers and how many reviewers reviewed the movie.
```
match (p:Person)-[:REVIEWED]->(m:Movie)
return m.title as Movie, count(p) as `Number of Reviews`, collect(p.name) as Reviewers
```

## 5.10 Retrieve all directors, their movies, and people who acted in the movies, returning the name of the director, the number of actors the director has worked with, and the list of actors.
```
match (p:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(p2:Person)
return p.name as Director, count(p2) as `Number of Actors`, collect(p2.name) as Actors
```

## 5.11 Retrieve the actors who have acted in exactly five movies, returning the name of the actor, and the list of movies for that actor.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, count(p) as numberMovies, collect(m.title) as Movies
where numberMovies = 5
return p.name as Actor, Movies
```

## 5.12 Retrieve the movies that have at least 2 directors, and optionally the names of people who reviewed the movies.
```
match (p:Person)-[:DIRECTED]->(m:Movie)
with m, count(m) as numberDirectors
where numberDirectors >= 2
optional match (p2:Person)-[:REVIEWED]->(m)
return m.title as Movie, p2.name as Reviewer
```

# Exercício 6 
> :play https://guides.neo4j.com/intro-neo4j-exercises/06.html

## 6.1 You want to know what actors acted in movies in the decade starting with the year 1990. First write a query to retrieve all actors that acted in movies during the 1990s, where you return the released date, the movie title, and the collected actor names for the movie. For now do not worry about duplication.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released < 2000
return m.released as `Release Date`, m.title as Movie, collect(p.name) as Actors
```

## 6.2 The results returned from the previous query include multiple rows for a movie released value. Next, modify the query so that the released date records returned are not duplicated. To implement this, you must add the collection of the movie titles to the results returned.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released < 2000
return m.released as `Release Date`, collect(m.title) as Movie, collect(p.name) as Actors
```

## 6.3 The results returned from the previous query returns the collection of movie titles with duplicates. That is because there are multiple actors per released year. Next, modify the query so that there is no duplication of the movies listed for a year.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released < 2000
return m.released as `Release Date`, collect(distinct m.title) as Movie, collect(p.name) as Actors
```

## 6.4 Modify the query that you just wrote to order the results returned so that the more recent years are displayed first.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 and m.released < 2000
return m.released as `Release Date`, collect(distinct m.title) as Movie, collect(p.name) as Actors
order by m.released desc
```

## 6.5 Retrieve the top 5 ratings and their associated movies, returning the movie title and the rating.
```
match (p:Person)-[r:REVIEWED]->(m:Movie)
return m.title as Movie, r.rating as Rating
order by r.rating desc limit 5
```

## 6.6 Retrieve all actors that have not appeared in more than 3 movies. Return their names and list of movies.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, count(p) as numberMovies, collect(m.title) as Movies
where numberMovies <= 3
return p.name as Actors, Movies
```

# Exercício 7 
> :play https://guides.neo4j.com/intro-neo4j-exercises/07.html

## 7.1 Write a Cypher query that retrieves all actors that acted in movies, and also retrieves the producers for those movies. During the query, collect the names of the actors and the names of the producers. Return the movie titles, along with the list of actors for each movie, and the list of producers for each movie making sure there is no duplication of data. Order the results returned based upon the size of the list of actors.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)<-[:PRODUCED]-(p2:Person)
with m, collect(distinct p.name) as Actors, collect(distinct p2.name) as Producers
return distinct m.title as Movies, Actors, Producers
order by size(Actors)
```

## 7.2 Write a Cypher query that retrieves all actors that acted in movies, and collects the list of movies for any actor that acted in more than five movies. Return the name of the actor and the list.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, collect(m) as Movies
where size(Movies) 5
return p.name as Actor, Movies
```

## 7.3 Modify the query you just wrote so that before the query processing ends, you unwind the list of movies and then return the name of the actor and the title of the associated movie
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, collect(m) as Movies
where size(Movies) 5
with p, Movies unwind Movies as Movie
return p.name as Actor, Movie.title
```

## 7.4 Write a query that retrieves all movies that Tom Hanks acted in, returning the title of the movie, the year the movie was released, the number of years ago that the movie was released, and the age of Tom when the movie was released.
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where p.name = 'Tom Hanks'
return m.title as Movie, m.released as Year, date().year - m.released as yearsAgoReleased, m.released - p.born as `Age of Tom Cruise`
order by yearsAgoReleased
```

# Exercício 8 
> :play https://guides.neo4j.com/intro-neo4j-exercises/08.html

## 8.1 Create a Movie node for the movie with the title, Forrest Gump.
```
create (:Movie{title: 'Forrest Gump'})
```

## 8.2 Retrieve the node you just created by its title.
```
match (m:Movie)
where m.title='Forrest Gump'
return m
```

## 8.3 Create a Person node for the person with the name, Robin Wright.
```
create (:Person{name: 'Robin Wright'})
```

## 8.4 Retrieve the Person node you just created by its name.
```
match (p:Person)
where p.name = 'Robin Wright'
return p
```

## 8.5 Add the label OlderMovie to any Movie node that was released before 2010.
```
match (m:Movie)
where m.released < 2010
set m:OlderMovie
return distinct(labels(m))
```

## 8.6 Retrieve all older movie nodes to test that the label was indeed added to these nodes.
```
match (m:OlderMovie)
return m.title, m.released
```

## 8.7 Add the label Female to all Person nodes that has a person whose name starts with Robin.
```
match (p:Person)
where p.name =~'Robin.*'
set p:Female
```

## 8.8 Retrieve all Female nodes
```
match (p:Female)
return p.name
```

## 8.9 We’ve decided to not use the Female label. Remove the Female label from the nodes that have this label.
```
match (p:Female)
remove p:Female
```

## 8.10 View the current schema of the graph.
```
call db.schema
```

## 8.11 Add the following properties to the movie, Forrest Gump:

* released: 1994

* tagline: Life is like a box of chocolates…​you never know what you’re gonna get.

* lengthInMinutes: 142

```
match (m:Movie)
where m.title = 'Forrest Gump'
set m:OlderMovie,
 	m.released = 1994, 
 	m.tagline = "Life is like a box of chocolates...you never know what you're gonna get", 
   m.lengthInMinutes = 142
```

## 8.12 Retrieve this OlderMovie node to confirm that the properties and label have been properly set.
```
match (m:OlderMovie)
where m.title = 'Forrest Gump'
return m
```

## 8.13 Add the following properties to the person, Robin Wright:

* born: 1966

* birthPlace: Dallas

```
match (p:Person)
where p.name = 'Robin Wright'
set p.born = 1966, p.birthPlace = 'Dallas'
```

## 8.14 Retrieve this Person node to confirm that the properties have been properly set.
```
match (p:Person)
where p.name = 'Robin Wright'
return p
```

# 8.15 Remove the lengthInMinutes property from the movie, Forrest Gump.
```
match (m:Movie)
where m.title = 'Forrest Gump'
set m.lengthInMinutes = null
```

## 8.16 Retrieve the Forrest Gump node to confirm that the property has been removed.
```
match (m:Movie)
where m.title='Forrest Gump'
return m
```

## 8.17 Remove the birthPlace property from the person, Robin Wright.
```
match (p:Person)
where p.name = 'Robin Wright'
remove p.birthPlace
```

## 8.18 Retrieve the Robin Wright node to confirm that the property has been removed.
```
match (p:Person)
where p.name = 'Robin Wright'
return p
```

## 8.19 - Taking it further

### 8.19.1 Add more labels to the Movie nodes to reflect the movie genre (action, drama, etc.).
```
match (m:Movie)
where m.title =~ 'The Matrix.*'
set m:ScienceFiction 
```

### 8.19.2 Query the database using different labels for movies.
```
match (m:ScienceFiction)
return m.title
```

### 8.19.3 Try adding or updating properties using the JSON-style syntax using = and +=.
```
match (m:Movie), (p:Person)
where m.title = 'Forrest Gump' and p.name = 'Robin Wright'
create (p)-[r:ACTED_IN]->(m)
set r = {roles:'Jenny Curran'}
return p, m
```

```
match (m:Movie), (p:Person)
where m.title = 'Forrest Gump' and p.name = 'Tom Hanks'
create (p)-[r:ACTED_IN]->(m)
set r.roles = 'Forrest Gump'
return p, m
```

### 8.19.4 Add properties to nodes using the JSON-style format where you add all of the properties to the node.
```
match (p:Person)
where p.name = 'Tom Hanks'
set p+={birthPlace:'Concord',oscars:2}
```

### 8.19.5 Query the database to confirm your additions.
```
match (p:Person)
where p.name = 'Tom Hanks'
return p
```

### 8.19.6 Call the Cypher built-in method to retrieve all of the property keys in the graph.
```
call db.propertyKeys
```

# Exercício 9 
> :play https://guides.neo4j.com/intro-neo4j-exercises/09.html

## 9.1 Create the ACTED_IN relationship between the actors, Robin Wright, Tom Hanks, and Gary Sinise and the movie, Forrest Gump.
```
match (m:Movie)
where m.title = 'Forrest Gump'
match (p:Person)
where p.name = 'Tom Hanks' or p.name = 'Robin Wright' or p.name = 'Gary Sinise'
create (p)-[:ACTED_IN]->(m)
```

## 9.2 Create the DIRECTED relationship between Robert Zemeckis and the movie, Forrest Gump.
```
match (m:Movie)
where m.title = 'Forrest Gump' 
match (p:Person)
where p.name = 'Robert Zemeckis'
create (p)-[:DIRECTED]->(m)
```

## 9.3 Create a new relationship, HELPED from Tom Hanks to Gary Sinise.
```
match (p1:Person)
where p1.name = 'Tom Hanks' 
match (p2:Person)
where p2.name = 'Gary Sinise'
create (p1)-[:HELPED]->(p2)
```

## 9.4 Write a Cypher query to return all nodes connected to the movie, Forrest Gump, along with their relationships.
```
match (p:Person)-[r]->(m:Movie)
where m.title='Forrest Gump'
return p, r, m
```

## 9.5 Add the roles property to the three ACTED_IN relationships that you just created to the movie, Forrest Gump using this information: Tom Hanks played the role, Forrest Gump. Robin Wright played the role, Jenny Curran. Gary Sinise played the role, Lieutenant Dan Taylor.
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title='Forrest Gump'
set r.roles = case p.name
	when 'Tom Hanks' then ['Forrest Gump']
    when 'Robin Wright' then ['Jenny Curran']
    when 'Gary Sinise' then ['Lieutenant Dan Taylor']
end
```

## 9.6 Add a new property, research to the HELPED relationship between Tom Hanks and Gary Sinise and set this property’s value to war history.
```
match (p1:Person)-[r:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise'
set r.research = 'war history'
```

## 9.7 View the current list of property keys in the graph.
```
call db.propertyKeys
```

## 9.8 View the current schema of the graph.
```
call db.schema
```

## 9.9 Query the graph to return the names and roles of actors in the movie, Forrest Gump.
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title='Forrest Gump'
return p.name, r.roles
```

## 9.10 Query the graph to retrieve information about any HELPED relationships.
```
match (p1:Person)-[r:HELPED]-(p2:Person)
return p1.name, r, p2.name
```

## 9.11 Modify the role that Gary Sinise played in the movie, Forrest Gump from Lieutenant Dan Taylor to Lt. Dan Taylor.
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title='Forrest Gump' and p.name='Gary Sinise'
set r.roles=['Lt. Dan Taylor']
```

## 9.12 Remove the research property from the HELPED relationship from Tom Hanks to Gary Sinise.
```
match (p1:Person)-[r:HELPED]-(p2:Person)
where p1.name='Tom Hanks' and p2.name='Gary Sinise'
remove r.research
```

## 9.13 Query the graph to confirm that your modifications were made to the graph.
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title='Forrest Gump'
return p, r, m
```

## 9.14 (Taking it further) Try adding or updating properties using the JSON-style syntax using = and +=.
```
match (p:Person)-[r:ACTED_IN]-(m:Movie)
where m.title='Forrest Gump' and p.name='Tom Hanks'
set r += {mainCharacter: true}
```

# Exercício 10 
> :play https://guides.neo4j.com/intro-neo4j-exercises/10.html

## 10.1 Delete the HELPED relationship from the graph.
```
match (:Person)-[r:HELPED]-(:Person)
delete r
```

## 10.2 Query the graph to confirm that the relationship no longer exists.
```
match (:Person)-[r:HELPED]-(:Person)
return r
```

## 10.3 Query the graph to display Forrest Gump and all of its relationships.
```
match (m:Movie)-[r]-(p:Person)
where m.title = 'Forrest Gump'
return m,r,p
```

## 10.4 Try deleting the Forrest Gump node without detaching its relationships.
```
match (m:Movie)
where m.title = 'Forrest Gump'
delete m
```

## 10.5 Delete Forrest Gump, along with its relationships in the graph.
```
match (m:Movie)
where m.title = 'Forrest Gump'
detach delete m
```

## 10.6 Query the graph to confirm that the Forrest Gump node has been deleted. 
```
match (p:Person)-[r]-(m:Movie)
where m.title='Forrest Gump'
return p,r,m
```


