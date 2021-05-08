import __evaluating_similarities__ as e_s
import __analisis_data__ as a_d


def imprimirMenu(texto, num_opciones):
    valido = False
    while not valido:
        print(f"{texto}")
        seleccion = int(input("\t>> Seleccione una opción (numero): "))
        if 1 <= seleccion <= num_opciones:
            valido = True
            return seleccion
        else:
            print("\n\t\t[OPCION INVALIDA]")

    return seleccion


def verificar_int(mensaje):
    todo_bien = False
    while not todo_bien:
        try:
            num_entero = int(input(mensaje))
            todo_bien = True
        except:
            print("FORMATO INCORRECTO...")
    return num_entero


def anadiendo(user):
    nombre_tabla = input(">> Nombre para el presupuesto: ")

    menu = 'Desea ingresar otro objeto?\n1. Si\n2. No'

    items = 2
    terminar = False
    objetos = []
    cantidades = []
    tiempos = []
    crear = [nombre_tabla, objetos, cantidades, tiempos]
    while True:
        opcion = imprimirMenu(menu, items)
        if opcion == 1:
            print("INGRESANDO OBJETO...")
            objeto = e_s.similarities()
            cantidad = verificar_int("\t>> Cantidad de objetos: ")
            tiempo = verificar_int("\t>> Tiempo de uso (minutos): ")
            objetos.append(objeto)
            cantidades.append(cantidad)
            tiempos.append(tiempo)

        elif opcion == 2:
            print(crear)
            # TODO necesito incluuir la funcion para duumpear la info
            # TODO crear funcion para resultados
            # TODO funcion para arreglar y mostrar.
            print("CREANDO TABLA...\n\t\t[CREACION CORRECTA]")
            # a_d.analizando(crear)
            break
        else:
            print("--------------------------------------------\nOPCION INVALIDA...\n--------------------------------------------")
