# crear = [nombre_tabla, objetos, cantidades, tiempos]
import pandas as pd


def operacion(crear):
	wats_totales = 0
	col_list = ["nombre", "maximo"]
	df = pd.read_csv("__tablas_data__/objetos.csv", sep=',', usecols=col_list)
	strOptions1 = df["nombre"].array
	strOptions2 = df["maximo"].array
	
	for x in range (len(crear[1])):
		for e in range (len(strOptions1)):
			if strOptions1[e] == crear[1][x]:
				print("woking")
				conversion_t = float(crear[3][x]) / 60
				conversion_w = float(strOptions2[e]) / 1000
				wats = conversion_w * conversion_t
				wats_momentaneos = float(crear[2][x]) * wats
				wats_totales += wats_momentaneos
				print("working end", wats_momentaneos, "bya", wats_totales)
	monto_inicial = 21.69 
	monto_final = 0
	
	if 0 < wats_totales <= 60:
		monto_final = (0.45 * wats_totales) + monto_inicial
		print(monto_final)
		return monto_final, wats_totales

	elif 61 <= wats_totales <= 125:
		monto_final = (0.78 * wats_totales) + monto_inicial
		print(monto_final)
		return monto_final, wats_totales

	elif 126 <= wats_totales <= 200:
		monto_final = (1.18 * wats_totales) + monto_inicial
		print(monto_final)
		return monto_final, wats_totales

	elif 201 <= wats_totales <= 300:
		monto_final = (1.25 * wats_totales) + monto_inicial
		print(monto_final)
		return monto_final, wats_totales

	elif 300 < wats_totales :
		monto_final = (2.03 * wats_totales) + monto_inicial
		print(monto_final)
		return str(monto_final), str(wats_totales)
			
