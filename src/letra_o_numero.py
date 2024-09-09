def evaluar(caracter):
    if caracter.isdigit():
        respuesta = "Es número"
    elif caracter.isalpha():
        if caracter.isupper():
            respuesta = "Es letra mayúscula"
        else:
            respuesta = "Es letra minúscula"
    else:
        respuesta = "No es letra ni número"                
    return respuesta

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
