import numpy as np
import pandas as pd


df = pd.read_excel(r'') #Para revision en caso de replicar el procedimiento copiar ruta de donde se alojo el archivo Canasta_Familiar_version1

df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Año"] = df["Fecha"].dt.year

tabla_promedios = (
    df.groupby(["Producto", "Año"])["Precio promedio por kilogramo*"]
    .mean()
    .to_dict()
)

promedios_ant = []
variaciones = []
precios_cero = []

for idx, fila in df.iterrows():
    producto = fila["Producto"]
    anio_anterior = fila["Año"] - 1
    precio_actual = fila["Precio promedio por kilogramo*"]

    if (producto, anio_anterior) in tabla_promedios:
        val_anterior = tabla_promedios[(producto, anio_anterior)]
        promedios_ant.append(val_anterior)

      
        variacion = ((precio_actual - val_anterior) / val_anterior) * 100
        variaciones.append(variacion)
        precios_cero.append("No")
    else:
      
        promedios_ant.append(None)
        variaciones.append(None)
        precios_cero.append("Si")

df["Promedio kg Año Anterior"] = promedios_ant
df["Variacion Anual %"] = variaciones
df["Precio en cero"] = precios_cero

ruta_guardado = r"" #ruta donde se desea que el archivo quede guardado 

df.to_excel(ruta_guardado, sheet_name="Datos Canasta", index=False)

print("Proceso finalizado")