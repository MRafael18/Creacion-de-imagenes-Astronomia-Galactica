import pandas as pd
import matplotlib.pyplot as plt


archivo = "cumulos.csv"

df = pd.read_csv(archivo)


abiertos = df[df["Tipo"].str.lower() == "abierto"].copy()
globulares = df[df["Tipo"].str.lower() == "globular"].copy()


def graficar_carta(datos, titulo, nombre_salida):
    plt.figure(figsize=(12, 7))
    plt.scatter(datos["RA_horas"], datos["Dec_grados"])

    for _, fila in datos.iterrows():
        plt.annotate(
            fila["Objeto"],
            (fila["RA_horas"], fila["Dec_grados"]),
            fontsize=8
        )

    plt.xlim(0, 24)
    plt.ylim(-40, 70)
    plt.xticks(range(0, 25, 2))
    plt.yticks(range(-40, 71, 10))
    plt.xlabel("Ascensión recta (horas)")
    plt.ylabel("Declinación (grados)")
    plt.title(titulo)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(nombre_salida, dpi=200, bbox_inches="tight")
    plt.close()


graficar_carta(
    abiertos,
    "Carta celeste de cúmulos abiertos",
    "carta_cumulos_abiertos.png"
)

graficar_carta(
    globulares,
    "Carta celeste de cúmulos globulares",
    "carta_cumulos_globulares.png"
)


plt.figure(figsize=(12, 7))

for tipo, grupo in df.groupby("Tipo"):
    plt.scatter(grupo["RA_horas"], grupo["Dec_grados"], label=tipo)

for _, fila in df.iterrows():
    plt.annotate(
        fila["Objeto"],
        (fila["RA_horas"], fila["Dec_grados"]),
        fontsize=7
    )

plt.xlim(0, 24)
plt.ylim(-40, 70)
plt.xticks(range(0, 25, 2))
plt.yticks(range(-40, 71, 10))
plt.xlabel("Ascensión recta (horas)")
plt.ylabel("Declinación (grados)")
plt.title("Carta celeste combinada de cúmulos Messier")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("carta_cumulos_combinada.png", dpi=200, bbox_inches="tight")
plt.close()

print("Listo. Se generaron estas imágenes:")
print("- carta_cumulos_abiertos.png")
print("- carta_cumulos_globulares.png")
print("- carta_cumulos_combinada.png")