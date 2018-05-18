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
    q = 'MATCH (u: Patient) WHERE u.name="'+paciente+'" RETURN u'
    resultsP = db.query(q, returns=(client.Node, str, client.Node))
    q = 'MATCH (u: Doctor) WHERE u.especialidad="'+especialidad+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    for i in resultsP:
        print i[0]
    for j in resultsD:
        print j[0]
    q = 'MATCH (u:Paciente) WHERE u.name="'+paciente+'" RETURN u'
    pacientes = db.query(q, returns=(client.Node))
