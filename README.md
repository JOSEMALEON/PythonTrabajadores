# 📊 Sistema de Reporte de Horas Trabajadas para ERP-CRM

## 🚀 Descripción
Este proyecto es un componente desarrollado en **Python** para la gestión de horas trabajadas por empleados dentro de un sistema **ERP-CRM**. Permite la **recolección, procesamiento y generación de informes** en formatos **PDF y Excel**.

## 📌 Características
- 📥 **Entrada de datos**: Permite registrar las horas trabajadas por cada empleado.
- 🧮 **Procesamiento de datos**: Calcula totales y promedios de horas trabajadas.
- 📊 **Generación de informes**:
  - 📄 **PDF** con resumen de horas trabajadas.
  - 📂 **Excel** con detalle por empleado.
- 🔧 **Fácil integración** con sistemas ERP-CRM mediante APIs o archivos generados.

## 🛠️ Tecnologías Usadas
- 🐍 **Python**
- 📜 **JSON** (almacenamiento de datos)
- 📄 **ReportLab** (generación de PDF)
- 📊 **Pandas & OpenPyXL** (generación de Excel)

## 📂 Estructura del Proyecto
```
📦 erp-crm-reporte-horas
 ┣ 📜 main.py             # Punto de entrada del programa
 ┣ 📜 entrada_datos.py     # Módulo de ingreso de datos
 ┣ 📜 procesamiento.py     # Módulo de cálculo de totales y promedios
 ┣ 📜 informe_pdf.py       # Generación de informes en PDF
 ┣ 📜 informe_excel.py     # Generación de informes en Excel
 ┣ 📜 horas_trabajadas.json # Almacenamiento temporal de datos
 ┣ 📜 README.md            # Documentación del proyecto
```

## 🚀 Instalación y Uso
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/erp-crm-reporte-horas.git
cd erp-crm-reporte-horas
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar el programa
```bash
python main.py
```

## 📋 Documentación
Para más detalles sobre el código, revisa la [documentación completa](DOCUMENTACION.md).

## 📌 Capturas de Pantalla
_Aquí puedes agregar imágenes del programa en ejecución._

## 📜 Licencia
Este proyecto está bajo la **Licencia MIT**.

---
**Desarrollado por el equipo DAVANTE** 🚀

