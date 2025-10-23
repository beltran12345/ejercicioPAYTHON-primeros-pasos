# ESTRUCTURA SWITCH - MATCH PYTHON

#Funcion para solicitar el mes
def solicitar_mes():
    return int(input("Digite un número del 1 al 12: "))

def obtener_nombre_mes(num):
    
     match  num:
        case 1: return "Enero"
        case 2: return "Febrero"
        case 3: return "Marzo"
        case 4: return "Abril"
        case 5: return "Mayo"
        case 6: return "Junio"
        case 7: return "Julio"
        case 8: return "Agosto"
        case 9: return "Septiembre"
        case 10: return "Octubre"
        case 11: return "Noviembre"
        case 12: return "Diciembre"
        case _: return "Número no válido"
        
        

def main():
    num = solicitar_mes()
    mes = obtener_nombre_mes(num)
    print("El mes correspondiente es:", mes)

# Llamado del programa principal
main()
     
