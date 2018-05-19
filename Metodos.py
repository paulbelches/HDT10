def ingresarDoctor (nombre, contacto, especialidad,db):
    Doctor = db.nodes.create(name=nombre, contact=contacto, speciality=especialidad)
    Doctor.labels.add("Doctor")
def ingresarPaciente (nombre,db):
    Paciente = db.nodes.create(name=nombre, contact=contacto, speciality=especialidad)
    Paciente.labels.add("Patient")
def ingresarMedicina (nombre,db):
    Medicina = db.nodes.create(name=nombre, contact=contacto, speciality=especialidad)
    Medicina.labels.add("Medicine")
def pacienteVisitaDoctor (nombreDoctor,nombrePaciente,medicina,cantidad,fecha,db):
    q = 'MATCH (u: Doctor) WHERE u.name="'+nombreDoctor+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    q = 'MATCH (u: Patient) WHERE u.name="'+nombrePacientes+'" RETURN u'
    resultsP = db.query(q, returns=(client.Node, str, client.Node))
    q = 'MATCH (u: Medicine) WHERE u.name="'+medicina+'" RETURN u'
    resultsM = db.query(q, returns=(client.Node, str, client.Node))
    resultsP.relationships.create("Visits", resultsD, date=fecha)
    resultsD.relationships.create("Prescribes", medicina,amount=cantidad)
    resultsP.relationships.create("Takes", medicina)
def doctorEspecialidad (especialidad,db):
    q = 'MATCH (u: Doctor) WHERE u.speciality="'+especialidad+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
def conoceA (nombre1,nombre2,db):
    q = 'MATCH (u: Patient) WHERE u.name="'+nombre1+'" RETURN u'
    resul1 = db.query(q, returns=(client.Node, str, client.Node))
    if (not(result1)):
        q = 'MATCH (u: Doctor) WHERE u.name="'+nombre1+'" RETURN u'
        resul1 = db.query(q, returns=(client.Node, str, client.Node))
    q = 'MATCH (u: Patient) WHERE u.name="'+nombre2+'" RETURN u'
    resul2 = db.query(q, returns=(client.Node, str, client.Node))
    if (not(result2)):
        q = 'MATCH (u: Doctor) WHERE u.name="'+nombre1+'" RETURN u'
        resul2 = db.query(q, returns=(client.Node, str, client.Node))
    result1.relationships.create("knows", result2)

def recomedacion(paciente, especialidad):
    #q = 'MATCH (u: Patient) WHERE u.name="'+paciente+'" RETURN u'
    q = 'MATCH (u:Pacient)-[r:Knows]->(m:Pacient) WHERE u.name="'+paciente+'" RETURN u
    resultsP = db.query(q, returns=(client.Node, str, client.Node))
    q = 'MATCH (u: Doctor) WHERE u.especialidad="'+especialidad+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    doctores={} #Se crea un diccionacio
    for j in resultsD:
        doctores[j]=0 #Se agregan todos los doctores con la especialidad
    for i in resultsP:
        q = 'MATCH (u:Pacient)-[r:Visits]->(m:Doctor) WHERE u.name="'+i+'" m.especialidad="'+especialidad+'" RETURN u'
        doctors = db.query(q, returns=(client.Node))#Se optienen todos los doctores con la especialidad visitados por los pacientes
        #Se agregan valores a los doctores que estan
        for element in doctors:
            doctores[element]=doctores[element]+1
        #Valores de los conocidos de los conocidos
        q = 'MATCH (u:Pacient)-[r:Knows]->(m:Pacient) WHERE u.name="'+i+'" RETURN u
        resultsP2 = db.query(q, returns=(client.Node, str, client.Node))
        for k in resultsP2:    
            q = 'MATCH (u:Pacient)-[r:Visits]->(m:Doctor) WHERE u.name="'+k+'" m.especialidad="'+especialidad+'" RETURN u'
            doctors = db.query(q, returns=(client.Node))#Se optienen todos los doctores con la especialidad visitados por los pacientes
            #Se agregan valores a los doctores que estan
            for element in doctors:
                doctores[element]=doctores[element]+1
    #Mostrar la lista de doctores en orden decendente
    for key, value in sorted(doctores.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        print "%s: %s" % (key, value)

def recomedacionDoctor(doctor, especialidad):
    #q = 'MATCH (u: Patient) WHERE u.name="'+paciente+'" RETURN u'
    q = 'MATCH (u:PDoctor)-[r:Knows]->(m:Doctor) WHERE u.name="'+doctor'" RETURN u
    resultsP = db.query(q, returns=(client.Node, str, client.Node))
    q = 'MATCH (u: Doctor) WHERE u.especialidad="'+especialidad+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    doctores={} #Se crea un diccionacio
    for j in resultsD:
        doctores[j]=0 #Se agregan todos los doctores con la especialidad
    for i in resultsP:
        doctores[i]=doctores[i]+1
        #Valores de los conocidos de los conocidos
        q = 'MATCH (u:PDoctor)-[r:Knows]->(m:Doctor) WHERE u.name="'+doctor'" RETURN u
        resultsP2 = db.query(q, returns=(client.Node, str, client.Node))
        for k in resultsP2:    
            q = 'MATCH (u:Pacient)-[r:Visits]->(m:Doctor) WHERE u.name="'+k+'" m.especialidad="'+especialidad+'" RETURN u'
            doctors = db.query(q, returns=(client.Node))#Se optienen todos los doctores con la especialidad visitados por los pacientes
            #Se agregan valores a los doctores que estan
            for element in doctors:
                doctores[element]=doctores[element]+1
    #Mostrar la lista de doctores en orden decendente
    for key, value in sorted(doctores.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        print "%s: %s" % (key, value)
