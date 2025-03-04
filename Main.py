import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

def ingresar_horas():
    empleados = {}
    while True:
        nombre = input("Ingrese el nombre del empleado (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        horas = float(input(f"Ingrese horas trabajadas por {nombre}: "))
        empleados[nombre] = horas
    with open("horas_trabajadas.json", "w") as f:
        json.dump(empleados, f)

def calcular_totales():
    with open("horas_trabajadas.json", "r") as f:
        empleados = json.load(f)
    total_horas = sum(empleados.values())
    promedio = total_horas / len(empleados) if empleados else 0
    return total_horas, promedio

def generar_reporte_pdf():
    total, promedio = calcular_totales()
    c = canvas.Canvas("informe_horas.pdf", pagesize=letter)
    c.drawString(100, 750, "Informe de Horas Trabajadas")
    c.drawString(100, 730, f"Total de Horas: {total}")
    c.drawString(100, 710, f"Promedio por Empleado: {promedio}")
    c.save()

def generar_reporte_excel():
    with open("horas_trabajadas.json", "r") as f:
        empleados = json.load(f)
    df = pd.DataFrame(list(empleados.items()), columns=["Empleado", "Horas"])
    df.to_excel("informe_horas.xlsx", index=False)

if __name__ == "__main__":
    ingresar_horas()
    generar_reporte_pdf()
    generar_reporte_excel()