# Tema 1: Introducción a los Métodos Numéricos

En la actualidad, los desafíos tecnológicos y científicos son cada vez más complejos. Aquí es donde los **métodos numéricos** juegan un papel crucial: permiten transformar modelos matemáticos en soluciones prácticas usando computadoras.

Ejemplos reales:
- Calcular la trayectoria de un satélite 
- Predecir el comportamiento del clima 
- Optimizar modelos de inteligencia artificial 

Estos problemas no pueden resolverse solo con cálculos manuales. Se necesitan algoritmos eficientes y confiables que trabajen con datos reales.

---

## ¿Por qué son importantes los métodos numéricos?

> "Son el puente entre el mundo real y las soluciones computacionales."

Aplicaciones destacadas:
- Resolver ecuaciones complejas sin solución exacta.
- Optimizar procesos de ingeniería y ciencia de datos.
- Simular escenarios naturales o artificiales para análisis o predicción.

Desde el diseño de productos hasta el análisis de sistemas naturales, estos métodos son indispensables.


---
### T1-E2: Problemario de Errores Numéricos
Actividad enfocada en la demostración de los diferentes tipos de errores en métodos numéricos, así como una explicación de estos.

1️ Errores de Precisión
Descripción breve:
Este ejercicio muestra cómo la acumulación de pequeños errores en operaciones repetidas puede llevar a resultados ligeramente diferentes de los esperados, debido a la representación finita de los números en la computadora.
### 🧾 Pseudocódigo
```
1. Elegir intervalo [a, b]
2. Evaluar f(x) en varios puntos
3. Graficar f(x) contra x
4. Observar el punto donde f(x) ≈ 0

Enunciado:
Realiza una suma repetida de un número decimal pequeño (por ejemplo, 0.0001) muchas veces y compara el resultado obtenido con el valor esperado. Calcula el error absoluto y relativo.

[🔗 Ver código de error de precisión (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/40045f9d503ccc2f1d14b517ff6b6ddf8f041ae4/codigos/tema1/Error%20de%20precision.py)

2️ Errores de Redondeo
Descripción breve:
Este ejercicio ilustra cómo la representación binaria de ciertos decimales (como 0.1) puede causar pequeñas discrepancias en los cálculos, generando errores de redondeo.
### 🧾 Pseudocódigo
```
1. Calcular f(a) y f(b)
2. Mientras |b - a| > tolerancia:
    x = (a + b)/2
    Si f(a)*f(x) < 0: b = x
    Si f(b)*f(x) < 0: a = x
3. Retornar x

Enunciado:
Suma el número 0.1 tres veces y compara el resultado con 0.3. Calcula el error absoluto y relativo.

[🔗 Ver código de error de redondeo (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/40045f9d503ccc2f1d14b517ff6b6ddf8f041ae4/codigos/tema1/Error%20de%20redondeo.py)

3️ Errores de Truncamiento
Descripción breve:
Este ejercicio demuestra cómo el error de truncamiento ocurre al aproximar una serie infinita (como la de Taylor para e) usando un número finito de términos.
### 🧾 Pseudocódigo
```
1. Calcular f(a) y f(b)
2. Mientras |f(x)| > tolerancia:
    x = b - f(b)*(b - a)/(f(b) - f(a))
    Si f(a)*f(x) < 0: b = x
    Si f(b)*f(x) < 0: a = x
3. Retornar x

Enunciado:
Aproxima el número e utilizando la serie de Taylor con un número limitado de términos. Compara el valor aproximado con el valor real y calcula el error absoluto y relativo.

[🔗 Ver código de error de truncamiento (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/40045f9d503ccc2f1d14b517ff6b6ddf8f041ae4/codigos/tema1/Error%20de%20truncamiento.py)

---
[ Volver al README principal](../README.md)
