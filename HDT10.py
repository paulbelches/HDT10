from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")
#Crear los primero nodos#
Mario= db.nodes.create(name="Mario Juarez", contact="12653248", speciality="Pediatra")
Mario.labels.add("Doctor")
Aspirina= db.nodes.create(name="Aspirina")
Aspirina.labels.add("Medicine")
Roberto= db.nodes.create(name="Roberto Garcia")
Roberto.labels.add("Patient")
Roberto.relationships.create("Visits", Mario, date="11/05/18")
Mario.relationships.create("Prescribes", Aspirina,amount="500g")
Roberto.relationships.create("Takes", Aspirina)

##
