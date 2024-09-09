def evaluar(anno):
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        respuesta = str(anno) + " es bisiesto"
    else:
        respuesta = str(anno) + " no es bisiesto"
    return respuesta

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())
    respuesta = evaluar(anno)
    print(respuesta)
