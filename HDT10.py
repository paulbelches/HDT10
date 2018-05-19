from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from Metodos import *
 
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
    print "4.Consultar cuales doctores por especialidad. \n"
    print "5.Ingresar que una persona conoce a otra persona. \n"
    print "6.Salir"
     op = int(raw_input("Ingrese una opcion"))
    if op == 1:
        nombre = raw_input("Ingresar nombre del doctor")
        contacto = raw_input("Ingresar el contacto del doctor")
        especialidad = raw_input("Ingresar la especialidad del doctor")
        ingresarDoctor(nombre,contacto,especialidad,db)
    elif op == 2:
        nombre = raw_input("Ingresar nombre del paciente")
        contacto = raw_input("Ingresar el contacto del paciente")
        ingresarPaciente(nombre,contacto,db)
    elif op == 3:
        nombreDoctor = raw_input("Ingresar nombre del Doctor")
        nombrePaciente = raw_input("Ingresar nombre del paciente")
        medicina = raw_input("Que medicina fue recetada")
        cantidad = raw_input("Cantidad de medicina recetada")
        fecha = raw_input("Ingresar fecha de la visita")
        pacienteVisitaDoctor(nombreDoctor,nombrePaciente,medicina,cantidad,fecha,db)
    elif op == 4:
         Especialidad = raw_input("Ingresar la especialidad que desea buscar")
         doctorEspecialidad(Especialidad,db)
    elif  op == 5:
        persona1 = raw_input("Ingresar el nombre de la primera persona")
        persona2 = raw_input("Ingresar el nombre de la segunda persona")
        conoceA(persona1,persona2,db)
    else:
        menu = False

    
