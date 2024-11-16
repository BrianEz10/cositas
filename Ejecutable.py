def ejecutable():
    print("Ingrese el ADN (6 filas de 6 caracteres cada una):")
    adnmatriz = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]

    return adnmatriz

def ejecutable2(ADN, detector):
    print("Bienvenido")
    print("Seleccione una opcion")
    print("1. Detectar Mutaciones")
    print("2. Mutar")
    print("3. Salir")
    opcion = int(input("Opcion: "))
    
    if opcion == 1:
        print("Se ingreso a localizar Mutaciones")
        from Clases import Detector
        deteccion = Detector(ADN,detector)
        deteccion.detectar_mutante()
        print("Deteccion Finalizada")
        eleccion = int(input("¿Desea realizar otra operacion?\nIngrese 0 para salir o 1 Para continuar"))
        if eleccion == 1:
            print("Seleccione una opcion")
            print("1. Mutar")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                print("Seleccione el tipo de mutacion a realizar")
                print("1. Radiacion")
                print("2. Virus")
                opcion = int(input("Opcion: "))
                if opcion == 1:#que pasa si el muchacho entra directamente a mutar pero no tiene una posicion inicial ni la orientacion de la mutacion, va a largar un error
                    pass
                    from Clases import Radiación
                    from Clases import posicion_inicial
                    from Clases import posicion_mutador
                    mutador_radiacion = Radiación(ADN, posicion_inicial, orientacion_de_la_mutacion)#Ver como pasamos las variables
                    mutador_radiacion.crear_mutante()
        elif eleccion != 0:
            print("Saliendo del programa...")
            print("Salida Exitosa")

    elif opcion > 3:
        print("Programa finalizado")



ADN = ejecutable()
detector = 4
ejecutable2(ADN,detector)
from Clases import posicion_inicial
print(posicion_inicial)
