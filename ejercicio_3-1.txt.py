# ESTRUCTURA WHILE PYTHON

#Funcion para solicitar el numero
def solicitar_numero():
    return int(input("Digite un número (0 para salir): "))

def verificar_par_impar(num):
    if num % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

def main():
    num = 1
    while num != 0:
        num = solicitar_numero()
        if num != 0:
            print(verificar_par_impar(num))
    print("Finalizó el programa.")

# Llamado del programa principal
main()
