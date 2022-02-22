from statistics import mode
import math

datos = []
frec = []
frec_rel = []
frec_acum = []
datoxfrec = []
varianza = []


def truncate(num,n):
    temp = str(num)
    for x in range(len(temp)):
        if temp[x] == '.':
            try:
                return float(temp[:x+n+1])
            except:
                return float(temp)      
    return float(temp)

# VALORES DE DATO Y FRECUENCIA
n = int(input("Cuantos valores tienes?"))
for i in range(n):
    num = float(input("Escribe un numero(DATOS):"))
    datos.append(num)
for i in range(n):
    num = float(input("Escribe un numero(FREC):"))
    frec.append(num)

totalDatos = sum(frec)
#OBTENER FRECUENCIA RELATIVA
for i in range(n):
    oper = (frec[i]*100)/totalDatos
    frec_rel.append(truncate(oper,2))

#OBTENER DATO X FRECUENCIA
for i in range(n):
    oper = datos[i]*frec[i]
    datoxfrec.append(oper)

#MEDIA Y MODA
sumadedatos= sum(datoxfrec)
media = truncate((sumadedatos/totalDatos), 2)
moda = datos[datoxfrec.index(max(datoxfrec))]

#OBTENER VARIANZA EN TABLA
for i in range(n):
    oper = ((datos[i]-media)**2)*frec[i]
    varianza.append(truncate(oper,2))

#OBTENR VARIANZA Y DESVIACION ESTANDAR
sumVarianza = truncate(sum(varianza), 2)
varianzafinal = truncate(sumVarianza/totalDatos, 2)
Des_estandar = truncate(math.sqrt(varianzafinal), 2)

print("Frecuencia relativa:", frec_rel, "\n")
print("Dato x Frecuencia:", datoxfrec, "Valor de dato x frec=", sumadedatos, "\n" )
print("media:", media, "Moda=", moda, "\n")
print("Varianza(tabla)", varianza, "\n")
print("o**2=", varianzafinal, "o=", Des_estandar)