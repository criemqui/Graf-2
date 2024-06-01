import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Datos del dataset en formato de cadena
data = """id,materia,nota,aprobado
1,Matemáticas,80,Sí
2,Historia,65,No
3,Ciencias,90,Sí
4,Lenguaje,75,Sí
5,Matemáticas,95,Sí
6,Historia,70,Sí
7,Ciencias,85,Sí
8,Lenguaje,60,No
9,Matemáticas,78,Sí
10,Historia,82,Sí
11,Ciencias,93,Sí
12,Lenguaje,68,Sí
13,Matemáticas,73,Sí
14,Historia,88,Sí
15,Ciencias,77,Sí
16,Lenguaje,50,No
17,Matemáticas,92,Sí
18,Historia,63,No
19,Ciencias,85,Sí
20,Lenguaje,79,Sí"""

# Utilizar StringIO para leer la cadena como si fuera un archivo
df = pd.read_csv(StringIO(data))

# Definir el orden de las materias
df['materia'] = pd.Categorical(df['materia'], categories=['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'], ordered=True)

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(12, 8))

# Crear el boxplot para cada materia en el orden especificado
df.boxplot(column='nota', by='materia', grid=True, ax=ax)

# Ajustar los ejes, agregar un título y etiquetas
ax.set_title('Distribución de Notas por Materia')
ax.set_xlabel('Materia')
ax.set_ylabel('Nota')
fig.suptitle('')  # Elimina el título automático de Pandas

# Mostrar el gráfico
plt.show()
