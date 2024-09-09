from time import localtime
def evaluar(dia, mes, anno):
    t = localtime()
    diaac = t.tm_mday
    mesac = t.tm_mon
    annoac = t.tm_year
    edad = annoac - anno - ((mesac, diaac) < (mes, diaac))
    respuesta = "Usted tiene " + str(edad) + " años"
    return respuesta

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
