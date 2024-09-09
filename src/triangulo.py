def evaluar(a, b, c):
    if ((a + b > c) and (a + c > b) and (b + c > a)):
        if (a == b and b == c):
            respuesta = "El triángulo es equilátero"
        elif (a == b or b == c or a == c):
            respuesta = "El triángulo es isósceles"  
        else:
            respuesta = "El triángulo es escaleno"    
    else:
        respuesta = "No es un triángulo válido"                              
    return respuesta

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
