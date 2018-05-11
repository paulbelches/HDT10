def ingersarDoctor(name, speciality ,contact):
    query = "CREATE (doctor:Doctor {name:" +name+", speciality:"+speciality+", contact:"contact"});"
    db.query(query)
def ingresarPaciente(nombre, numero)
    query = "CREATE (patinet:Patient {name:" +name+", contact:"contact"});"
    db.query(query)
