import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel(r"") #Usar ruta donse se tiene guardado el archivo CANASTA FAMILIAR 2023 - 2026

df_grafico = df[df["Precio en cero"] == "No"].copy()

total_muestras = len(df_grafico)
mediana = df_grafico["Variacion Anual %"].median()
media = df_grafico["Variacion Anual %"].mean()

desviacion_estandar = df_grafico["Variacion Anual %"].std()

indice_asimetria = (media - mediana) / desviacion_estandar

if abs(indice_asimetria) > 0.555:
    resultado_texto = "FUERTE (Bimodal/Multimodal)"
else:
    resultado_texto = "DÉBIL (Unimodal/Uniforme)"

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid", rc={"grid.linestyle": ":", "grid.alpha": 0.5})

sns.histplot(
    data=df_grafico,
    x="Variacion Anual %",
    stat="density",
    kde=False,
    color="#3182bd",
    bins=1800,
    edgecolor="black",
    linewidth=0.5,
    alpha=0.75,
)

sns.kdeplot(
    data=df_grafico,
    x="Variacion Anual %",
    color="#1d5a8a",  
    linewidth=2,
    bw_adjust=1.3,    
    gridsize=2000,    
)

plt.axvline(
    x=mediana,
    color="green",
    linestyle="-",
    linewidth=1.8,
    label=f"Mediana: {mediana:.2f}%",
)
plt.axvline(
    x=media,
    color="red",
    linestyle="--",
    linewidth=1.8,
    label=f"Media: {media:.2f}%",
)

texto_info = (
    f"Muestras: {total_muestras:,}\n"
    f"Índice de Asimetría: {indice_asimetria:.3f}\n"
    f"Resultado: {resultado_texto}"
)

plt.text(
    0.95,
    0.95,
    texto_info,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment="top",
    horizontalalignment="right",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="0.7"),
)

plt.title(
    "Diagnóstico de Dispersión de Inflación - Validación del Modelo",
    fontsize=13,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Variación de Precio Anual (%)", fontsize=11)
plt.ylabel("Densidad de Frecuencia", fontsize=11)

plt.xticks(
    [-50, -25, 0, 25, 50, 75, 100],
    ["-50%", "-25%", "0%", "25%", "50%", "75%", "100%"],
)

plt.xlim(-55, 115)

plt.legend(loc="upper left", fontsize=9)
plt.tight_layout()

ruta_grafico = (
    r""         # Usar ruta donde se desea guardar la imagen
)
plt.savefig(ruta_grafico, dpi=300)
plt.show()

print("Proceso finalizado")