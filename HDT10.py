from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")


Mario= db.nodes.create(name="Mario Juarez", contact="12653248", speciality="Pediatra")
mario.label.add("Doctor")

Mario= db.nodes.create(name="Aspirina",amount="500g")
mario.label.add("Medicine")

Mario= db.nodes.create(name="Roberto Garcia")
mario.label.add("Patient")

