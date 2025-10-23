#  ESTRUCTURA FOR PYTHON

#Funcion que solicita la cantidad de numeros
def solicitar_cantidad():
    return int(input("Digite la cantidad de números para sumar: "))

def solicitar_numero(indice):
    return int(input(f"Digite el número {indice + 1}: "))

def main():
    suma = 0
    cantidad = solicitar_cantidad()
    for i in range(cantidad):
        numero = solicitar_numero(i)
        suma += numero
    print("La sumatoria total es:", suma)

# Llamado del programa principal
main()
     
