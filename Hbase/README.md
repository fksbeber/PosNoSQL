# Parte 1 - Aquecendo com alguns dados

## 1. Crie a tabela com 2 famílias de colunas:
* a. personal-data
* b. professional-data
    > create 'italians', 'personal-data', 'professional-data'
	
## 2. Importe o arquivo via linha de comando
	> hbase shell /tmp/italians.txt

# Agora execute as seguintes operações:

## 1. Adicione mais 2 italianos mantendo adicionando informações como data
de nascimento nas informações pessoais e um atributo de anos de
experiência nas informações profissionais;
	> put 'italians', '11', 'personal-data:name',  'Matteo Coppola'
	> put 'italians', '11', 'personal-data:birth',  '25/11/1980'
	> put 'italians', '11', 'personal-data:city',  'Turin'
	> put 'italians', '11', 'professional-data:role',  'Gestão Industrial'
	> put 'italians', '11', 'professional-data:years_of_experience',  '15'
	> put 'italians', '11', 'professional-data:salary',  '13250'

	> put 'italians', '12', 'personal-data:name',  'Bianca Ferrari'
	> put 'italians', '12', 'personal-data:birth',  '17/05/1982'
	> put 'italians', '12', 'personal-data:city',  'Parma'
	> put 'italians', '12', 'professional-data:role',  'Geologia'
	> put 'italians', '12', 'professional-data:years_of_experience',  '13'
	> put 'italians', '12', 'professional-data:salary',  '10525'
	
## 2. Adicione o controle de 5 versões na tabela de dados pessoais.
	> alter 'italians', NAME=>'personal-data', VERSIONS=>5
	
## 3. Faça 5 alterações em um dos italianos;
	> put 'italians', '11', 'personal-data:birth',  '05/11/1980'
	> put 'italians', '11', 'personal-data:birth',  '15/11/1980'
	> put 'italians', '11', 'personal-data:city',  'Naples'
	> put 'italians', '11', 'personal-data:city',  'Rome'
	> put 'italians', '11', 'personal-data:city',  'Florence'
	
## 4. Com o operador get, verifique como o HBase armazenou o histórico.
	> get 'italians', '11',{COLUMN=>'personal-data:city', VERSIONS=>5}
	
    > COLUMN                                      > CELL
	personal-data:city                         timestamp=1585342238904, value=Florence
	personal-data:city                         timestamp=1585341197750, value=Rome
	personal-data:city                         timestamp=1585341195692, value=Naples
	personal-data:city                         timestamp=1585339693652, value=Turin
	1 row(s)
	Took 0.1323 seconds
	
## 5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.
	> scan 'italians',{COLUMNS=>['personal-data:name','professional-data:role']}
	
    > |ROW | COLUMN+CELL |
    > | - | ----------- |
    > | 1 | column=personal-data:name, timestamp=1585338610670, value=Paolo Sorrentino|
    > | 1 | column=professional-data:role, timestamp=1585338610792, value=Gestao Comercial
    > | 10 | column=personal-data:name, timestamp=1585338611239, value=Giovanna Caputo
    > | 10 | column=professional-data:role, timestamp=1585338611266, value=Comunicacao Institucional
    > | 11 | column=personal-data:name, timestamp=1585339693540, value=Matteo Coppola
    > | 11 | column=professional-data:role, timestamp=1585339693724, value=Gest??o Industrial
    > | 12 | column=personal-data:name, timestamp=1585339704611, value=Bianca Ferrari
    > | 12 | column=professional-data:role, timestamp=1585339704756, value=Geologia
    > | 2 | column=personal-data:name, timestamp=1585338610819, value=Domenico Barbieri
    > | 2 | column=professional-data:role, timestamp=1585338610843, value=Psicopedagogia
    > | 3 | column=personal-data:name, timestamp=1585338610872, value=Maria Parisi
    > | 3 | column=professional-data:role, timestamp=1585338610902, value=Optometria
    > | 4 | column=personal-data:name, timestamp=1585338610925, value=Silvia Gallo
    > | 4 | column=professional-data:role, timestamp=1585338610950, value=Engenharia Industrial Madeireira
    > | 5 | column=personal-data:name, timestamp=1585338610984, value=Rosa Donati
    > | 5 | column=professional-data:role, timestamp=1585338611014, value=Mecatronica Industrial
    > | 6 | column=personal-data:name, timestamp=1585338611039, value=Simone Lombardo
    > | 6 | column=professional-data:role, timestamp=1585338611066, value=Biotecnologia e Bioquimica
    > | 7 | column=personal-data:name, timestamp=1585338611090, value=Barbara Ferretti
    > | 7 | column=professional-data:role, timestamp=1585338611115, value=Libras
    > | 8 | column=personal-data:name, timestamp=1585338611140, value=Simone Ferrara
    > | 8 | column=professional-data:role, timestamp=1585338611163, value=Engenharia de Minas
    > | 9 | column=personal-data:name, timestamp=1585338611190, value=Vincenzo Giordano
    > | 9 | column=professional-data:role, timestamp=1585338611213, value=Marketing

    > 12 row(s)
    > Took 0.3221 seconds



## 6. Apague os italianos com row id ímpar
	> deleteall 'italians', '1'
	> deleteall 'italians', '3'
	> deleteall 'italians', '5'
	> deleteall 'italians', '7'
	> deleteall 'italians', '9'
	> deleteall 'italians', '11'
	
## 7. Crie um contador de idade 55 para o italiano de row id 5
	> incr 'italians', 5, 'personal-data:age', 55 
	
        COUNTER VALUE = 55
	    Took 0.0485 seconds

	> get_counter 'italians', 5, 'personal-data:age'
	    
        COUNTER VALUE = 55
	    Took 0.0116 seconds
	
## 8. Incremente a idade do italiano em 1
	> incr 'italians', 5, 'personal-data:age', 1
	
        COUNTER VALUE = 56
	    Took 0.0141 seconds
