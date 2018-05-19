import operator
lista = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
lista2 = ['Lunes','Miercoles','Jueves','Domingo']
dias = {}
for element in lista:
    dias[element]=0
for element in lista2:
    dias[element]=dias[element]+1
for key, value in sorted(dias.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
