import csv


def crear_csv(user):
    direccion = "__tablas_presupuestos__/" + user + ".csv"
    with open(direccion, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(
            ['presupuesto', 'objetos', 'cantidades', 'tiempos'])
