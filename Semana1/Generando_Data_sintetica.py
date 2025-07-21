import pandas as pd
import random
import numpy as np
import os
from faker import Faker
from datetime import date, datetime

# Configuración inicial
fake = Faker('es_ES')
random.seed(42)
np.random.seed(42)

def generar_empleados_belcorp(n=1000):
    areas = {
        'Finanzas': ['Analista Financiero', 'Contador', 'Jefe de Tesorería'],
        'Marketing': ['Especialista en Marca', 'Diseñador Gráfico', 'Coordinador de Producto'],
        'Logística': ['Almacenero', 'Supervisor de Logística', 'Coordinador de Transporte'],
        'TI': ['Desarrollador Backend', 'Soporte Técnico', 'Analista de Sistemas'],
        'Recursos Humanos': ['Analista de RRHH', 'Reclutador', 'Asistente de Bienestar'],
        'Producción': ['Operario de Planta', 'Jefe de Línea', 'Supervisor de Producción']
    }

    ciudades = ['Lima', 'Arequipa', 'Trujillo', 'Piura', 'Cusco', 'Tacna', 'Iquitos', 'Chiclayo']
    generos = ['Masculino', 'Femenino']
    modalidades = ['Presencial', 'Remoto', 'Mixto']
    tipos_contrato = ['Indeterminado', 'Plazo Fijo', 'Prácticas']

    data = []

    for i in range(1, n + 1):
        id_empleado = f"E{i:04d}"
        nombre = fake.first_name()
        apellido = fake.last_name()
        edad = random.randint(20, 60)
        genero = random.choice(generos)
        area = random.choice(list(areas.keys()))
        puesto = random.choice(areas[area])
        ciudad = random.choice(ciudades)
        modalidad = random.choice(modalidades)
        from datetime import date
        fecha_ingreso = fake.date_between(start_date=date(2018, 1, 1), end_date=date.today())

        # Asignación coherente de sueldo y tipo de contrato
        sueldo = round(random.uniform(930, 6000), 2)
        if sueldo < 1025:
            tipo_contrato = 'Prácticas'
        else:
            tipo_contrato = random.choice([tc for tc in tipos_contrato if tc != 'Prácticas'])

        # 20% de cesados
        estado = 'Cesado' if random.random() < 0.2 else 'Activo'

        evaluacion = round(random.uniform(0, 100), 2)

        data.append([
            id_empleado, nombre, apellido, edad, genero, area, puesto, tipo_contrato,
            fecha_ingreso, sueldo, ciudad, modalidad, estado, evaluacion
        ])

    columnas = [
        "ID Empleado", "Nombre", "Apellido", "Edad", "Género", "Área", "Puesto",
        "Tipo de Contrato", "Fecha de Ingreso", "Sueldo", "Ciudad",
        "Modalidad de Trabajo", "Estado", "Evaluación de Desempeño"
    ]

    # Crear DataFrame
    df = pd.DataFrame(data, columns=columnas)

    # Ruta de salida en tu estructura
    output_dir = os.path.join("Data_sintetica")
    os.makedirs(output_dir, exist_ok=True)

    # Guardar en CSV
    output_path = os.path.join(output_dir, 'empleados_belcorp.csv')
    df.to_csv(output_path, index=False)

    print(f"✅ Dataset sintético generado con éxito en:\n{output_path}")

# Llamada directa si el script se ejecuta
if __name__ == "__main__":
    generar_empleados_belcorp()

