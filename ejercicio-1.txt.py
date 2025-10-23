
    # *************** Programa que identifica si un número es positivo, negativo o neutro ***************
    
  
#funcion para solicitar el numero
def solicitar_numero():
    numero = int(input("digite un numero: "))
    return numero

 # funcion para identificar el tipo de numero
def ideentificar_numero(numero):
    if numero > 0:
        return "el numero positivo."
    elif numero == 0:
        return "el numero es neutro."
    else:
        return"el numero es negativo."

        # funcion principal que une todo
        def main ():
            num = solicitar_numero(num)
            print(resultado)

            #llamado de la funcion principal
            main()
    
    # funcion principal
     