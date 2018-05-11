from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7687", username="neo4j", password="12345")
#Crear los primero nodos#
Mario= db.nodes.create(name="Mario Juarez", contact="12653248", speciality="Pediatra")
Mario.labels.add("Doctor")
Aspirina= db.nodes.create(name="Aspirina")
Aspirina.labels.add("Medicine")
Roberto= db.nodes.create(name="Roberto Garcia", contact="24889647" )
Roberto.labels.add("Patient")
Roberto.relationships.create("Visits", Mario, date="11/05/18")
Mario.relationships.create("Prescribes", Aspirina,amount="500g")
Roberto.relationships.create("Takes", Aspirina)
#Menu#
menu = True
while menu:
    print "1.Ingresar Doctores, con los datos de su especialidad y como contactarlo. \n"
    print "2.Ingresar Pacientes, con sus datos. \n"
    print "3.Ingresar que un paciente dado, visita a un doctor especifico. \n"
    print "4.Indicar la fecha de visita y la medicinaque le receta. \n"
    print "5.Consultar cuales doctores por especialidad. \n"
    print "6.Ingresar que una persona conoce a otra persona. \n"
    print "7.Salir"
    
