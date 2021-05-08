import __creating_csv__ as c_c
import __main_menu__ as m_m

# TODO mover estas funciones a otro lado ya que son globales, leer y dumper


def leer(name):
    archivo = open(name, encoding='utf-8')
    texto = archivo.read()
    archivo.close()

    quitarlineas = texto.split('\n')
    array = []

    for quitarcomas in quitarlineas:
        array.append(quitarcomas.split(','))

    return texto, array


def dumper(name, dumption):
    archivo = open(name, 'w', encoding='utf-8')
    archivo.write(dumption)
    archivo.close()


def salir():

    print('OPCIONES: \n1. Regresar a menu\n2. Nuevo intento')
    confirmacion_inter = False
    confirmacion = False
    while not confirmacion_inter:
        opcion = input('\t>> Seleccione una opcion (numero): ')
        if opcion == '1':
            print('--------------------------------------------\nREGRESANDO A MENU...')
            confirmacion = True
            confirmacion_inter = True
        elif opcion == '2':
            print('REINTENTANDO...')
            confirmacion = False
            confirmacion_inter = True
        else:
            print(
                '\t\t[OPCION INVALIDA]\nOPCIONES: \n1. Regresar a menu\n2. Nuevo intento')
    return confirmacion


def accion(op):
    if op == 1:
        print("--------------------------------------------\nINGRESO DE USUARIO...\n--------------------------------------------")
    if op == 2:
        print("--------------------------------------------\nCREACION DE USUARIO...\n--------------------------------------------")
    exit = False
    while not exit:
        normal, arreglo = leer('__tablas_data__/users.csv')
        usuario = input(">> Ingrese usuario: ")
        contra = input(">> Ingrese contraseña: ")

        valid, valid2 = 0, 0

        for e in range(len(arreglo)):
            try:
                if (usuario == arreglo[e][0]) and (contra == arreglo[e][1]):
                    valid = valid + 1
                if usuario == arreglo[e][0]:
                    valid2 = valid2 + 1
            except:
                pass

        if op == 1:
            if valid > 0:
                print("\t\t\t[INGRESANDO]")
                m_m.main_menu(usuario)
                exit = True
                # TODO Aqui me falta poner la llamada a la funcion menu ya logeado, solo eso esto trabaja individual

            else:
                print("\t\t[NO EXISTEN TALES CREDENCIALES]")

        if op == 2:
            if valid2 > 0:
                print("\t\t[USUARIO YA EXISTENTE]")
            else:
                print("\t\t[¡USUARIO CREADO CORRECTAMENTE!]")
                texto = normal + '\n' + usuario + "," + contra
                dumper('__tablas_data__/users.csv', texto)
                c_c.crear_csv(usuario)
        if not exit:
            exit = salir()
    login()


def login():
    menu = '--------------------------------------------\n\t<== PRESUPUESTOS LOGIN ==>\n--------------------------------------------\n1. Iniciar Sesión\n2. Crear cuenta\n3. Terminar ejecución'

    print(menu)
    opcion = input('\t>> Seleccione una opción (numero): ')
    if (opcion == '1') or (opcion == '2'):
        accion(int(opcion))
    elif opcion == '3':
        print(
            '--------------------------------------------\nSALIENDO...\n--------------------------------------------\n\t\t\t[¡SALIDA EXITOSA!]')
    else:
        print('--------------------------------------------\nOPCION INVALIDA...')
        login()


# TODO AQUI EMPIEZA TODO
#login()
# TODO discutir si trabajamos en una sola tabla
