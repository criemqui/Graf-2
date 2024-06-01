import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Datos del dataset en formato de cadena
data = """id,materia,nota,aprobado
1,Matemáticas,80,Aprobados
2,Historia,65,No Aprobados
3,Ciencias,90,Aprobados
4,Lenguaje,75,Aprobados
5,Matemáticas,95,Aprobados
6,Historia,70,Aprobados
7,Ciencias,85,Aprobados
8,Lenguaje,60,No Aprobados
9,Matemáticas,78,Aprobados
10,Historia,82,Aprobados
11,Ciencias,93,Aprobados
12,Lenguaje,68,Aprobados
13,Matemáticas,73,Aprobados
14,Historia,88,Aprobados
15,Ciencias,77,Aprobados
16,Lenguaje,50,No Aprobados
17,Matemáticas,92,Aprobados
18,Historia,63,No Aprobados
19,Ciencias,85,Aprobados
20,Lenguaje,79,Aprobados"""

# Utilizar StringIO para leer la cadena como si fuera un archivo
df = pd.read_csv(StringIO(data))

# Contar el número de estudiantes aprobados y no aprobados
aprobados_count = df['aprobado'].value_counts()

# Crear el pie chart
plt.figure(figsize=(8, 8))
plt.pie(aprobados_count, labels=aprobados_count.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff6666'])
plt.title('Distribución de Aprobados')

# Mostrar el gráfico
plt.show()
