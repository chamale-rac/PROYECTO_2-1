from fuzzywuzzy import process
import pandas as pd


def similarities():

    col_list = ["nombre"]
    df = pd.read_csv("objetos.csv", sep=';', usecols=col_list)
    strOptions = df["nombre"].array

    exit = False

    while not exit:
        str2Match = input("\t>> Ingrese nombre de objeto: ")
        Ratios = process.extract(str2Match, strOptions)

        valid = -1
        for e in range(len(strOptions)):
            try:
                if (str2Match == strOptions[e]):
                    valid = e
            except:
                pass

        if valid == -1:
            print("PROBABLEMENTE QUISO DECIR:")
            for e in range(len(Ratios)):
                print("\t"+str(e) + ". " + Ratios[e][0])
            continuar = False
            while not continuar:
                opcion = input(
                    "¿QUE DESEA HACER?\n1. Elegir entre posibles objetos\n2. Escribir de nuevo\n\t>> Ingrese una opcion (numero): ")

                if opcion == "1":
                    opcion_numero = int(
                        input("\t>> Ingrese numero de opcion para objeto: "))
                    elegido = str(Ratios[opcion_numero][0])
                    print("FUE ELEGIDO: ", elegido)
                    return elegido
                elif opcion == "2":
                    print("REINTENTANDO...")
                    continuar = True
                else:
                    print(
                        '--------------------------------------------\nOPCION INVALIDA...\n--------------------------------------------')

        elif valid != -1:
            print("FUE ELEGIDO: ", str2Match)
            return str2Match
