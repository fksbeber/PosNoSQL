# Redis
Este projeto é a implementação de um jogo de bingo, utilizando a linguagem python e o banco redis.

## Pré-requisitos
- Python versão 3.8 instalado;
- Redis server versão 3.0 em execução na máquina local;

## 1 - Configuração
Para executar o projeto é necessário fazer configurações detalhadas abaixo.

### 1.1 - Clonar o repositório
É necessário clonar o repositório através do comando abaixo.
```
git clone https://github.com/fksbeber/PosNoSQL.git
```
### 1.2 - Instalar as dependências:
É necessário criar um novo ambiente virtual e instalar as dependências necessárias do projeto:
1. Navegar até a pasta ``redis``
2. Executar os comandos abaixo
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 2 - Execução
Para executar o programa, basta navegar até a pasta ``redis`` e executar o comando abaixo.
```
python redisbingo.py
```
O programa exibirá um resultado similar ao seguinte
```
Game started...
- number '26' was drawn from the pool
- number '28' was drawn from the pool
- number '14' was drawn from the pool
- number '17' was drawn from the pool
- number '50' was drawn from the pool
- number '3' was drawn from the pool
- number '25' was drawn from the pool
- number '7' was drawn from the pool
- number '15' was drawn from the pool
- number '43' was drawn from the pool
- number '29' was drawn from the pool
- number '22' was drawn from the pool
- number '38' was drawn from the pool
- number '36' was drawn from the pool
- number '41' was drawn from the pool
- number '2' was drawn from the pool
- number '21' was drawn from the pool
- number '31' was drawn from the pool
- number '19' was drawn from the pool
- number '39' was drawn from the pool
- number '40' was drawn from the pool
- number '32' was drawn from the pool
- number '11' was drawn from the pool
- number '8' was drawn from the pool
- number '16' was drawn from the pool
- number '48' was drawn from the pool
- number '18' was drawn from the pool
- number '4' was drawn from the pool
- number '27' was drawn from the pool
- number '9' was drawn from the pool
- number '30' was drawn from the pool
- number '12' was drawn from the pool
- number '45' was drawn from the pool
- number '44' was drawn from the pool
- number '6' was drawn from the pool
- number '10' was drawn from the pool
- number '13' was drawn from the pool
- number '46' was drawn from the pool
- number '5' was drawn from the pool
The game has 1 winner(s):
- user05
```