import __adding__ as ad


def main_menu(user):
    menu = '--------------------------------------------\n\t<== PRESUPUESTOS MENU ==>\n--------------------------------------------\n1. Crear presupuesto\n2. Editar presupuesto\n3. Ver presupuesto y resultados\n4. Eliminar presupuesto\n5. Logout'
    items = 5

    while True:
        opcion = ad.imprimirMenu(menu, items)
        if opcion == 1:
            ad.anadiendo(user)

        # TODO el 2 seria editar
        # TODO el 3 seria ver
        # TODO el 4 eliminar

        if opcion == 5:
            print("--------------------------------------------\nREGRESANDO...")
            break
    return
