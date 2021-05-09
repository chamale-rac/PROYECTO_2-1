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


def guardand(user, crear):
    linea_objetos = "#".join(str(x)for x in crear[1])
    linea_cantidades = "#".join(str(x)for x in crear[2])
    linea_tiempos = "#".join(str(x)for x in crear[3])
    linea_nueva = crear[0] + ";" + linea_objetos + \
        ";" + linea_cantidades + ";" + linea_tiempos + \
        ";" + crear[4] + ";" + crear[5]
    #linea_nueva = ";".join(str(x) for x in crear)
    linea_nueva += '\n'
    with open('__tablas_presupuestos__/' + user + '.csv', 'a', encoding='utf-8') as f:
        f.write(linea_nueva)  # escribir
    f.close()


def anadiendo(user):
    nombre_tabla = input(">> Nombre para el presupuesto: ")

    menu = 'Desea ingresar otro objeto?\n1. Si\n2. No'

    items = 2
    objetos = []
    cantidades = []
    tiempos = []
    dinero = ''
    wats = ''
    crear = [nombre_tabla, objetos, cantidades, tiempos, dinero, wats]
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
            dinero, wats = a_d.operacion(crear)
            guardand(user, crear)

            # a_d.analizando(crear)
            break
        else:
            print("--------------------------------------------\nOPCION INVALIDA...\n--------------------------------------------")
