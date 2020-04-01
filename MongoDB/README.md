# Exercício 1 - Aquecendo com os pets
Insira os seguintes registros no MongoDB e em seguida responda as questões
abaixo:

> use petshop

> db.pets.insert({name: "Mike", species: "Hamster"})

> db.pets.insert({name: "Dolly", species: "Peixe"})

> db.pets.insert({name: "Kilha", species: "Gato"})

> db.pets.insert({name: "Mike", species: "Cachorro"})

> db.pets.insert({name: "Sally", species: "Cachorro"})

> db.pets.insert({name: "Chuck", species: "Gato"}) 

## 1.1 Adicione outro Peixe e um Hamster com nome Frodo:

> db.pets.insert({Name: "Frodo", species: "Hamster"})
```
 WriteResult({ "nInserted" : 1 })
```

> db.pets.insert({Name: "Frodo", species: "Peixe"}) 
```
WriteResult({ "nInserted" : 1 })
```
	
## 1.2 Faça uma contagem dos pets na coleção
> db.pets.count()
```
8
```
	
## 1.3 Retorne apenas um elemento o método prático possível
> db.pets.findOne()
```
"_id" : ObjectId("5e7b8ae1cd87b0c783d5fccb"),
"name" : "Mike",
"species" : "Hamster"
```

## 1.4 Identifique o ID para o Gato Kilha
> db.pets.find({"$and":[{name: "Kilha"},{species: "Gato"}]},{_id:1})
```
{ "_id" : ObjectId("5e7bbb314546989d4cbc71d9") }
```
	
## 1.5 Faça uma busca pelo ID e traga o Hamster Mike
> db.pets.find({_id: ObjectId("5e7bbb314546989d4cbc71d7")})
```
 { "_id" : ObjectId("5e7bbb314546989d4cbc71d7"), "name" : "Mike", "species" : "Hamster" }
```
	
## 1.6 Use o find para trazer todos os Hamsters
> db.pets.find({species: "Hamster"})
```
{ "_id" : ObjectId("5e7bbb314546989d4cbc71d7"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e7bbb524546989d4cbc71dd"), "name" : "Frodo", "species" : "Hamster" }
```
	
## 1.7 Use o find para listar todos os pets com nome Mike
> db.pets.find({name: "Mike"})
```
{ "_id" : ObjectId("5e7bbb314546989d4cbc71d7"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e7bbb314546989d4cbc71da"), "name" : "Mike", "species" : "Cachorro" }
```
	
## 1.8 Liste apenas o documento que é um Cachorro chamado Mike
> db.pets.find({"$and":[{name: "Mike"},{species: "Cachorro"}]})
```
{ "_id" : ObjectId("5e7bbb314546989d4cbc71da"), "name" : "Mike", "species" : "Cachorro" }
```
	
# Exercício 2

## 2.1 Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.
>  db.italians.find({age: 99}).count()
```
0
```

## 2.2 Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)
>  db.italians.find({age:{"$gt": 65}}).count()
```
1729
```
	
## 2.3 Identifique todos os jovens (pessoas entre 12 a 18 anos).
>  db.italians.find({age:{"$gte": 12, "$lte": 18}}).count()
```
863
```

## 2.4 Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois
>  db.italians.find({cat: {$exists: true}}).count()
```
6035
```
>  db.italians.find({dog: {$exists: true}}).count()
```
4025
```
>  db.italians.find({"$nor":[{dog:{$exists: true}},{cat: {$exists: true}}]}).count()
```
2393
```
	
## 2.5 Liste/Conte todas as pessoas acima de 60 anos que tenham gato
>  db.italians.find({"$and":[{age: {$gt: 60}},{cat:null}]}).count()
```
945
```
	
## 2.6 Liste/Conte todos os jovens com cachorro
>  db.italians.find({"$and":[{age: {$gte: 12, $lte: 18}},{dog:null}]}).count()
```
543
```
	
## 2.7 Utilizando o $where, liste todas as pessoas que tem gato e cachorro
>  db.italians.find({$where: "this.cat && this.dog"}).count()
```
2453
```
>  db.italians.find({$where: "this.cat && this.dog"},{_id:0,firstname:1})

```
{ "firstname" : "Pietro" }
{ "firstname" : "Claudio" }
{ "firstname" : "Lucia" }
{ "firstname" : "Gianluca" }
{ "firstname" : "Fabio" }
{ "firstname" : "Giusy" }
{ "firstname" : "Angelo" }
{ "firstname" : "Rosa" }
{ "firstname" : "Barbara" }
{ "firstname" : "Rita" }
{ "firstname" : "Giacomo" }
{ "firstname" : "Fabrizio" }
{ "firstname" : "Cristian" }
{ "firstname" : "Alessandra" }
{ "firstname" : "Roberta" }
{ "firstname" : "Giovanna" }
{ "firstname" : "Cristian" }
{ "firstname" : "Mirko" }
{ "firstname" : "Antonella" }
{ "firstname" : "Giovanna" }
Type "it" for more
```

## 2.8 Liste todas as pessoas mais novas que seus respectivos gatos.
>  db.italians.find({$and:[{cat: {$exists: true}},{$where: "this.age < this.cat.age"}]},{_id:0,firstname:1})
```
{ "firstname" : "Federica" }
{ "firstname" : "Rosa" }
{ "firstname" : "Barbara" }
{ "firstname" : "Fabrizio" }
{ "firstname" : "Simone" }
{ "firstname" : "Giovanna" }
{ "firstname" : "Sara" }
{ "firstname" : "Valentina" }
{ "firstname" : "Maurizio" }
{ "firstname" : "Pasquale" }
{ "firstname" : "Alex" }
{ "firstname" : "Alex" }
{ "firstname" : "Anna" }
{ "firstname" : "Valeira" }
{ "firstname" : "Giovanni" }
{ "firstname" : "Valentina" }
{ "firstname" : "Sabrina" }
{ "firstname" : "Michela" }
{ "firstname" : "Lorenzo" }
{ "firstname" : "Matteo" }
Type "it" for more
```
>  db.italians.find({$and:[{cat: {$exists: true}},{$where: "this.age < this.cat.age"}]}).count()
```
659
```
	
## 2.9 Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)
>  db.italians.find({$and:[{$or  [{cat: {$exists: true}},{dog: {$exists: true}}]},{$where: "(this.cat && this.firstname == this.cat.name) || (this.dog && this.firstname == this.dog.name)"}]},{_id:0,'firstname':1, 'dog.name':1, 'cat.name':1})
```
{ "firstname" : "Cristian", "cat" : { "name" : "Cristian" } }
{ "firstname" : "Michele", "cat" : { "name" : "Michele" } }
{ "firstname" : "Elisa", "cat" : { "name" : "Fabrizio" }, "dog" : { "name" : "Elisa" } }
{ "firstname" : "Tiziana", "dog" : { "name" : "Tiziana" } }
{ "firstname" : "Claudio", "cat" : { "name" : "Claudio" } }
{ "firstname" : "Lorenzo", "cat" : { "name" : "Lorenzo" }, "dog" : { "name" : "Maurizio" } }
{ "firstname" : "Elena", "cat" : { "name" : "Elena" } }
{ "firstname" : "Simona", "dog" : { "name" : "Simona" } }
{ "firstname" : "Mirko", "cat" : { "name" : "Mirko" }, "dog" : { "name" : "Giorgio" } }
{ "firstname" : "Lorenzo", "cat" : { "name" : "Lorenzo" } }
{ "firstname" : "Rita", "cat" : { "name" : "Rita" } }
{ "firstname" : "Enzo ", "cat" : { "name" : "Enzo " }, "dog" : { "name" : "Claudio" } }
{ "firstname" : "Enrico", "dog" : { "name" : "Enrico" } }
{ "firstname" : "Pietro", "cat" : { "name" : "Pietro" }, "dog" : { "name" : "Enzo " } }
{ "firstname" : "Simona", "cat" : { "name" : "Simona" } }
{ "firstname" : "Nicola", "cat" : { "name" : "Nicola" } }
{ "firstname" : "Sabrina", "cat" : { "name" : "Sabrina" } }
{ "firstname" : "Sabrina", "cat" : { "name" : "Sabrina" } }
{ "firstname" : "Elisabetta", "cat" : { "name" : "Elisabetta" }, "dog" : { "name" : "Alberto" } }
{ "firstname" : "Veronica", "cat" : { "name" : "Alessandra" }, "dog" : { "name" : "Veronica" } }
Type "it" for more
```
>  db.italians.find({$and:[{$or:  [{cat: {$exists: true}},{dog: {$exists: true}}]},{$where: "(this.cat && this.firstname == this.cat.name) || (this.dog && this.firstname == this.dog.name)"}]}).count()
```
112
```
	
## 2.10 Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo
>  db.italians.find({"bloodType": /-/i},{'_id':0,'firstname':1,'surname':1})
```
{ "firstname" : "Teresa", "surname" : "Damico" }
{ "firstname" : "Pietro", "surname" : "Mazza" }
{ "firstname" : "Massimo", "surname" : "Gallo" }
{ "firstname" : "Lucia", "surname" : "Cattaneo" }
{ "firstname" : "Gabiele", "surname" : "Costatini" }
{ "firstname" : "Fabio", "surname" : "Damico" }
{ "firstname" : "Cristian", "surname" : "Battaglia" }
{ "firstname" : "Federica", "surname" : "Morelli" }
{ "firstname" : "Alessio", "surname" : "Martini" }
{ "firstname" : "Angelo", "surname" : "Serra" }
{ "firstname" : "Barbara", "surname" : "Barone" }
{ "firstname" : "Rosa", "surname" : "Guerra" }
{ "firstname" : "Cinzia", "surname" : "Santoro" }
{ "firstname" : "Rita", "surname" : "De Rosa" }
{ "firstname" : "Davide", "surname" : "Vitali" }
{ "firstname" : "Paolo", "surname" : "Conte" }
{ "firstname" : "Rita", "surname" : "Fiore" }
{ "firstname" : "Serena", "surname" : "Damico" }
{ "firstname" : "Giacomo", "surname" : "Donati" }
{ "firstname" : "Fabrizio", "surname" : "Martinelli" }
Type "it" for more
```
	
## 2.11 Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)
>  db.italians.find({$where: "this.cat || this.dog"},{'_id':0,'cat':1,'dog':1})
```
{ "cat" : { "name" : "Alessandro", "age" : 6 } }
{ "cat" : { "name" : "Marco", "age" : 3 } }
{ "dog" : { "name" : "Anna", "age" : 9 } }
{ "cat" : { "name" : "Teresa", "age" : 4 }, "dog" : { "name" : "Davide", "age" : 13 } }
{ "cat" : { "name" : "Fabrizio", "age" : 2 }, "dog" : { "name" : "Laura", "age" : 12 } }
{ "dog" : { "name" : "Matteo", "age" : 12 } }
{ "cat" : { "name" : "Fabrizio", "age" : 6 }, "dog" : { "name" : "Valentina", "age" : 15 } }
{ "cat" : { "name" : "Cristian", "age" : 12 } }
{ "cat" : { "name" : "Elisabetta", "age" : 11 } }
{ "cat" : { "name" : "Sara", "age" : 11 }, "dog" : { "name" : "Elena", "age" : 13 } }
{ "cat" : { "name" : "Sara", "age" : 11 }, "dog" : { "name" : "Salvatore", "age" : 15 } }
{ "cat" : { "name" : "Cristina", "age" : 3 }, "dog" : { "name" : "Marco", "age" : 5 } }
{ "cat" : { "name" : "Davide", "age" : 7 } }
{ "cat" : { "name" : "Alberto", "age" : 11 } }
{ "dog" : { "name" : "Massimiliano", "age" : 8 } }
{ "dog" : { "name" : "Paolo", "age" : 0 } }
{ "cat" : { "name" : "Anna", "age" : 14 }, "dog" : { "name" : "Alex", "age" : 1 } }
{ "cat" : { "name" : "Emanuela", "age" : 13 } }
{ "cat" : { "name" : "Sabrina", "age" : 3 }, "dog" : { "name" : "Cinzia", "age" : 15 } }
{ "cat" : { "name" : "Davide", "age" : 2 } }
Type "it" for more
```	
## 2.12 Quais são as 5 pessoas mais velhas com sobrenome Rossi?
>  db.italians.find({'surname': 'Rossi'},{'_id': 0,'firstname': 1,'age': 1}).limit(5).sort({'age': -1})
```
{ "firstname" : "Massimo", "age" : 79 }
{ "firstname" : "Chiara", "age" : 78 }
{ "firstname" : "Giovanna", "age" : 77 }
{ "firstname" : "Nicola", "age" : 77 }
{ "firstname" : "Ilaria", "age" : 76 }
```

## 2.13 Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano
>  db.italians.insert({firstname: "Matteo", surname: "Coppola", age: '41',email: 'matteo.coppola@hotmail.com',bloodType: 'AB+', id_num: '858585858585', jobs: ['Gestão de Segurança Privada','Segurança Pública'], favFruits: ['Laranja','Banana','Mamão'], lion: {name: 'Filipo', age: 8}})
```
WriteResult({ "nInserted" : 1 })
```
	
## 2.14 Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.
>  db.italians.remove({"_id" : ObjectId("5e7ce669272f7c6603b09fc7")})
```
WriteResult({ "nRemoved" : 1 })
```
	
## 2.15 Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1
>  db.italians.update({},{'$inc': {'age': 1}},{multi: true})
```
WriteResult({ "nMatched" : 10000, "nUpserted" : 0, "nModified" : 10000 })
```
>  db.italians.update({cat: {$exists: true}},{'$inc': {'cat.age': 1}},{multi: true})
```
WriteResult({ "nMatched" : 6035, "nUpserted" : 0, "nModified" : 6035 })
```	

## 2.16 O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.
>  db.italians.remove({$and: [{'age': 66},{'cat': {$exists: true}}]})
```
WriteResult({ "nRemoved" : 81 })
```
	
## 2.17 Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.

>  db.italians.aggregate([{$match: {mother:  {$exists: true}, $or:  [{cat: {$exists: true}},{dog: {$exists: true}}]}},{'$project': {'firstname': 1, 'mother': 1, 'cat': 1, 'dog': 1, 'isEqual': {'$cmp': ['$firstname','$mother.firstname']}}},{$match: {'isEqual': 0}}])
```
{ "_id" : ObjectId("5e7cb53c272f7c6603b07dd6"), "firstname" : "Federica", "mother" : { "firstname" : "Federica", "surname" : "Valentini", "age" : 46 }, "cat" : { "name" : "Giusy", "age" : 8 }, "dog" : { "name" : "Andrea", "age" : 6 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e7cb53d272f7c6603b07f8b"), "firstname" : "Barbara", "mother" : { "firstname" : "Barbara", "surname" : "Ferretti", "age" : 21 }, "cat" : { "name" : "Michela", "age" : 7 }, "dog" : { "name" : "Paola", "age" : 15 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e7cb53e272f7c6603b08206"), "firstname" : "Gianni", "mother" : { "firstname" : "Gianni", "surname" : "Guerra", "age" : 49 }, "cat" : { "name" : "Matteo", "age" : 3 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e7cb544272f7c6603b08e58"), "firstname" : "Chiara", "mother" : { "firstname" : "Chiara", "surname" : "Bianco", "age" : 75 }, "cat" : { "name" : "Teresa", "age" : 18 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e7cb546272f7c6603b090d6"), "firstname" : "Silvia", "mother" : { "firstname" : "Silvia", "surname" : "Lombardo", "age" : 55 }, "cat" : { "name" : "Marta", "age" : 7 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e7cb54a272f7c6603b09ab7"), "firstname" : "Alessia", "mother" : { "firstname" : "Alessia", "surname" : "Bianco", "age" : 90 }, "dog" : { "name" : "Daniele", "age" : 6 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e7cb54c272f7c6603b09d70"), "firstname" : "Luca", "mother" : { "firstname" : "Luca", "surname" : "Leone", "age" : 39 }, "cat" : { "name" : "Barbara", "age" : 11 }, "dog" : { "name" : "Massimiliano", "age" : 10 }, "isEqual" : 0 } 
```
	
## 2.18 Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome
>  db.italians.aggregate([{$group: {_id: '$firstname'}}])
```
{ "_id" : "Anna" }
{ "_id" : "Cristina" }
{ "_id" : "Alberto" }
{ "_id" : "Tiziana" }
{ "_id" : "Rosa" }
{ "_id" : "Sabrina" }
{ "_id" : "Marco" }
{ "_id" : "Antonella" }
{ "_id" : "Claudio" }
{ "_id" : "Gianni" }
{ "_id" : "Davide" }
{ "_id" : "Enzo " }
{ "_id" : "Cinzia" }
{ "_id" : "Marta" }
{ "_id" : "Sara" }
{ "_id" : "Mirko" }
{ "_id" : "Elisa" }
{ "_id" : "Filipo" }
{ "_id" : "Giuseppe" }
{ "_id" : "Gabiele" }
Type "it" for more
```
	
## 2.19 Agora faça a mesma lista do item acima, considerando nome completo.
> db.italians.aggregate([{$group: {_id: {firstname:'$firstname', surname: '$surname'}}}])
```
{ "_id" : { "firstname" : "Domenico", "surname" : "Moretti" } }
{ "_id" : { "firstname" : "Giacomo", "surname" : "Vitali" } }
{ "_id" : { "firstname" : "Gianni", "surname" : "D’Amico" } }
{ "_id" : { "firstname" : "Sergio", "surname" : "Moretti" } }
{ "_id" : { "firstname" : "Alessio", "surname" : "Farina" } }
{ "_id" : { "firstname" : "Emanuele", "surname" : "Bianco" } }
{ "_id" : { "firstname" : "Ilaria", "surname" : "De Luca" } }
{ "_id" : { "firstname" : "Daniele", "surname" : "Caruso" } }
{ "_id" : { "firstname" : "Elisabetta", "surname" : "Ricci" } }
{ "_id" : { "firstname" : "Alessandro", "surname" : "De Angelis" } }
{ "_id" : { "firstname" : "Giulia", "surname" : "Rizzi" } }
{ "_id" : { "firstname" : "Giorgio", "surname" : "Damico" } }
{ "_id" : { "firstname" : "Roberto", "surname" : "Silvestri" } }
{ "_id" : { "firstname" : "Antonella", "surname" : "Martini" } }
{ "_id" : { "firstname" : "Claudio", "surname" : "Bruno" } }
{ "_id" : { "firstname" : "Daniela", "surname" : "Montanari" } }
{ "_id" : { "firstname" : "Gabiele", "surname" : "Milani" } }
{ "_id" : { "firstname" : "Tiziana", "surname" : "Sartori" } }
{ "_id" : { "firstname" : "Emanuela", "surname" : "Farina" } }
{ "_id" : { "firstname" : "Mario", "surname" : "Serra" } }
Type "it" for more
```
	
## 2.20 Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato,
mais de 20 e menos de 60 anos
>  db.italians.find({$and: [{$or:  [{favFruits: 'Banana'},{favFruits: 'Maçã'}]},{$or:  [{cat: {$exists: true}},{dog: {$exists: true}}]},{age: {'$gt': 20,'$lt': 60}}]},{'_id': 0, 'firstname': 1, 'favFruits': 1, 'cat': 1, 'dog': 1})
```
{ "firstname" : "Teresa", "favFruits" : [ "Banana", "Laranja", "Pêssego" ], "cat" : { "name" : "Alessandro", "age" : 7 } }
{ "firstname" : "Pietro", "favFruits" : [ "Banana" ], "cat" : { "name" : "Teresa", "age" : 5 }, "dog" : { "name" : "Davide", "age" : 13 } }
{ "firstname" : "Giusy", "favFruits" : [ "Maçã", "Tangerina", "Pêssego" ], "cat" : { "name" : "Cristina", "age" : 4 }, "dog" : { "name" : "Marco", "age" : 5 } }
{ "firstname" : "Cristian", "favFruits" : [ "Maçã", "Goiaba", "Kiwi" ], "cat" : { "name" : "Davide", "age" : 8 } }
{ "firstname" : "Alessio", "favFruits" : [ "Banana", "Uva", "Mamão" ], "dog" : { "name" : "Massimiliano", "age" : 8 } }
{ "firstname" : "Cinzia", "favFruits" : [ "Uva", "Uva", "Banana" ], "dog" : { "name" : "Gianluca", "age" : 6 } }
{ "firstname" : "Federico", "favFruits" : [ "Maçã" ], "cat" : { "name" : "Chiara", "age" : 7 } }
{ "firstname" : "Cristian", "favFruits" : [ "Maçã", "Uva" ], "cat" : { "name" : "Cristian", "age" : 18 } }
{ "firstname" : "Giuseppe", "favFruits" : [ "Mamão", "Melancia", "Maçã" ], "cat" : { "name" : "Sara", "age" : 2 }, "dog" : { "name" : "Federica", "age" : 10 } }
{ "firstname" : "Simona", "favFruits" : [ "Goiaba", "Banana", "Maçã" ], "cat" : { "name" : "Federica", "age" : 8 } }
{ "firstname" : "Sabrina", "favFruits" : [ "Laranja", "Maçã" ], "cat" : { "name" : "Elisabetta", "age" : 10 } }
{ "firstname" : "Michele", "favFruits" : [ "Banana", "Kiwi", "Banana" ], "cat" : { "name" : "Michele", "age" : 8 } }
{ "firstname" : "Sonia", "favFruits" : [ "Banana", "Maçã", "Pêssego" ], "cat" : { "name" : "Domenico", "age" : 8 } }
{ "firstname" : "Giacomo", "favFruits" : [ "Kiwi", "Banana" ], "cat" : { "name" : "Raffaele", "age" : 2 } }
{ "firstname" : "Federico", "favFruits" : [ "Banana" ], "cat" : { "name" : "Angela", "age" : 11 } }
{ "firstname" : "Giorgio", "favFruits" : [ "Melancia", "Maçã", "Kiwi" ], "dog" : { "name" : "Mauro", "age" : 14 } }
{ "firstname" : "Giorgia", "favFruits" : [ "Mamão", "Banana" ], "cat" : { "name" : "Maria", "age" : 9 }, "dog" : { "name" : "Daniela", "age" : 3 } }
{ "firstname" : "Enrico", "favFruits" : [ "Maçã", "Laranja", "Laranja" ], "cat" : { "name" : "Rita", "age" : 10 }, "dog" : { "name" : "Paolo", "age" : 4 } }
{ "firstname" : "Alberto", "favFruits" : [ "Laranja", "Kiwi", "Maçã" ], "cat" : { "name" : "Alessio", "age" : 7 }, "dog" : { "name" : "Chiara", "age" : 17 } }
{ "firstname" : "Vincenzo", "favFruits" : [ "Pêssego", "Pêssego", "Maçã" ], "cat" : { "name" : "Elisa", "age" : 13 }, "dog" : { "name" : "Enzo ", "age" : 16 } }
Type "it" for more
```
	
# Exercício 3

## 3.1 Liste as ações com profit acima de 0.5 (limite a 10 o resultado)
>  db.stocks.find({'Profit Margin': {$gt: 0.5}},{'Company': 1, 'Profit Margin': 1, '_id': 0}).limit(10)
```
{ "Profit Margin" : 0.896, "Company" : "AllianceBernstein Holding L.P." }
{ "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "Profit Margin" : 0.654, "Company" : "Ares Capital Corporation" }
{ "Profit Margin" : 0.576, "Company" : "Apollo Commercial Real Estate Finance, Inc." }
{ "Profit Margin" : 0.848, "Company" : "ARMOUR Residential REIT, Inc." }
{ "Profit Margin" : 0.732, "Company" : "Athlon Energy Inc." }
{ "Profit Margin" : 0.548, "Company" : "Aircastle LTD" }
{ "Profit Margin" : 0.63, "Company" : "The Bank of New York Mellon Corporation" }
{ "Profit Margin" : 0.588, "Company" : "Banco Latinoamericano de Comercio Exterior, S.A" }
{ "Profit Margin" : 0.503, "Company" : "Brookfield Properties Corporation" }
```
	
## 3.2 Liste as ações com perdas (limite a 10 novamente)
> db.stocks.find({'Profit Margin': {$lt: 0}},{'Company': 1, 'Profit Margin': 1, '_id': 0}).limit(10)
```
{ "Profit Margin" : -0.023, "Company" : "Applied Optoelectronics, Inc." }
{ "Profit Margin" : -0.232, "Company" : "Advantage Oil & Gas Ltd." }
{ "Profit Margin" : -0.645, "Company" : "Cambium Learning Group, Inc." }
{ "Profit Margin" : -0.005, "Company" : "Arkansas Best Corporation" }
{ "Profit Margin" : -0.0966, "Company" : "American Bio Medica Corp." }
{ "Profit Margin" : -0.769, "Company" : "Barrick Gold Corporation" }
{ "Profit Margin" : -0.014, "Company" : "Accelrys Inc." }
{ "Profit Margin" : -0.18, "Company" : "Atlantic Coast Financial Corporation" }
{ "Profit Margin" : -0.051, "Company" : "Aluminum Corporation Of China Limited" }
{ "Profit Margin" : -0.173, "Company" : "Arch Coal Inc." }
```
	
## 3.3 Liste as 10 ações mais rentáveis
>  db.stocks.find({},{'Company': 1, 'Profit Margin': 1, '_id': 0}).sort({'Profit Margin': -1}).limit(10)
```
{ "Profit Margin" : 0.994, "Company" : "BP Prudhoe Bay Royalty Trust" }
{ "Profit Margin" : 0.994, "Company" : "Cascade Bancorp" }
{ "Profit Margin" : 0.99, "Company" : "Pacific Coast Oil Trust" }
{ "Profit Margin" : 0.986, "Company" : "Enduro Royalty Trust" }
{ "Profit Margin" : 0.982, "Company" : "Whiting USA Trust II" }
{ "Profit Margin" : 0.976, "Company" : "MV Oil Trust" }
{ "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "Profit Margin" : 0.971, "Company" : "VOC Energy Trust" }
{ "Profit Margin" : 0.97, "Company" : "Mesa Royalty Trust" }
{ "Profit Margin" : 0.97, "Company" : "One Liberty Properties Inc." }
```

## 3.4 Qual foi o setor mais rentável?
>  db.stocks.aggregate([{$group: {_id: '$Sector', Rentability: {$sum: '$Profit Margin'}}},{$sort: {'Rentability': -1}},{$limit: 1}])
```
{ "_id" : "Financial", "Rentability" : 162.5356 }
```
	
## 3.5 Ordene as ações pelo profit e usando um cursor, liste as ações.
>	* var cursor = db.stocks.find({},{'Company': 1, 'Profit Margin': 1, '_id': 0}).sort({'Profit Margin': -1}).limit(10)
>	*  cursor.forEach(function(x) {print(x.Company+': '+x['Profit Margin'])})
```
BP Prudhoe Bay Royalty Trust: 0.994
Cascade Bancorp: 0.994
Pacific Coast Oil Trust: 0.99
Enduro Royalty Trust: 0.986
Whiting USA Trust II: 0.982
MV Oil Trust: 0.976
American Capital Agency Corp.: 0.972
VOC Energy Trust: 0.971
Mesa Royalty Trust: 0.97
One Liberty Properties Inc.: 0.97
```
	
## 3.6 Renomeie o campo “Profit Margin” para apenas “profit”
>  db.stocks.update({'Profit Margin': {$exists: true}},{$rename: {'Profit Margin': 'profit'}},{multi: true})
```
WriteResult({ "nMatched" : 4302, "nUpserted" : 0, "nModified" : 4302 })
```
	
## 3.7 Agora liste apenas a empresa e seu respectivo resultado
>  db.stocks.find({profit: {$exists: true}},{_id: 0, 'Company': 1, 'profit': 1}).sort({profit: -1}).limit(10)
```
{ "Company" : "BP Prudhoe Bay Royalty Trust", "profit" : 0.994 }
{ "Company" : "Cascade Bancorp", "profit" : 0.994 }
{ "Company" : "Pacific Coast Oil Trust", "profit" : 0.99 }
{ "Company" : "Enduro Royalty Trust", "profit" : 0.986 }
{ "Company" : "Whiting USA Trust II", "profit" : 0.982 }
{ "Company" : "MV Oil Trust", "profit" : 0.976 }
{ "Company" : "American Capital Agency Corp.", "profit" : 0.972 }
{ "Company" : "VOC Energy Trust", "profit" : 0.971 }
{ "Company" : "Mesa Royalty Trust", "profit" : 0.97 }
{ "Company" : "One Liberty Properties Inc.", "profit" : 0.97 }
```
	
## 3.8 Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?
>  db.stocks.find({profit: {$exists: true}},{_id: 0, 'Company': 1, 'profit': 1}).sort({profit: -1}).limit(3)
```
{ "Company" : "BP Prudhoe Bay Royalty Trust", "profit" : 0.994 }
{ "Company" : "Cascade Bancorp", "profit" : 0.994 }
{ "Company" : "Pacific Coast Oil Trust", "profit" : 0.99 }
```
	
## 3.9 Liste as ações agrupadas por setor
>  db.stocks.aggregate([{"$group": {_id:"$Sector", companies: {"$addToSet": {Company:"$Company"}}}}])
```
Cria uma lista com o nome das companhias para cada setor 
```
	
# Exercício 4

## 4.1 Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?
>  db.enron.distinct("sender").length
```
2200
```
	
## 4.2 Contabilize quantos e-mails tem a palavra “fraud”
>  db.enron.find({"text": /fraud/i}).count()
```
25
```
