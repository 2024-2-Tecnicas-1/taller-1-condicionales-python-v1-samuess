def evaluar(peso, estatura, edad):
    imc = peso / (estatura * estatura)
    if imc < 22.0 and edad < 45:
        respuesta = "bajo"
    elif imc >= 22.0 and edad < 45:
        respuesta = "medio"
    elif imc < 22.0 and edad >= 45:
        respuesta = "medio"
    elif imc >= 22.0 and edad >= 45:
        respuesta = "alto"                    
    return respuesta

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
