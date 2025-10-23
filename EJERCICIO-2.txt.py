#  ESTRUCTURA DO - WHILE PYTHON

#Funcion para mostrar el menu
def mostrar_menu():
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa\n")



def procesar_opcion(opcion):
    if opcion == "A":
        print("Actualizando sistema...\n")
    elif opcion == "E":
        print("Eliminando catálogo...\n")
    elif opcion == "C":
        print("Creando productos...\n")
    elif opcion == "S":
        print("Finalizó con éxito.\n")
    else:
        print("Opción no válida.\n")

def main():
    while True:
        mostrar_menu()
        letra = input("Digite una opción: ").upper()
        procesar_opcion(letra)
        if letra == "S":
            break
    print("El DO-WHILE ha finalizado.\n")

# Llamado del programa principal
main()
     