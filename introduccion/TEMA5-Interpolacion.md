# Tema 5: Interpolación 

En la ciencia, la ingeniería y el análisis de datos, muchas veces solo disponemos de un conjunto limitado de mediciones o resultados experimentales. Sin embargo, necesitamos estimar valores intermedios, predecir comportamientos o modelar tendencias a partir de esos datos discretos. Por ejemplo:

- Estimar la concentración de un reactivo en un punto no medido de una reacción química .
- Predecir la temperatura en una ciudad a una hora no registrada .
- Ajustar una curva para modelar el crecimiento de una población o el rendimiento de un sistema energético .

En estos escenarios, los **métodos de interpolación y ajuste de funciones** se convierten en herramientas fundamentales. Permiten construir funciones que pasan exactamente por los puntos conocidos (interpolación) o que se aproximan lo mejor posible a los datos (ajuste), facilitando la simulación, la predicción y el análisis en contextos donde no existe una fórmula explícita.

---

## Importancia de la Interpolación 

> "Son las técnicas que nos permiten estimar, predecir y modelar cuando los datos exactos no están disponibles o son insuficientes."

**Aplicaciones principales:**
- Estimar valores intermedios entre datos experimentales.
- Modelar tendencias y comportamientos en sistemas complejos.
- Predecir resultados futuros a partir de datos históricos.
- Analizar la precisión y el error de las aproximaciones.

## Problemario de Métodos de Solución

Ejercicios prácticos enfocados en la aplicación de los métodos numéricos para interpolación, regresión, correlación y mínimos cuadrados. Cada subapartado describe brevemente el método utilizado y presenta un ejercicio representativo, resuelto con Python.

### 1. Interpolación Lineal

**Descripción del método:**  
La interpolación lineal estima el valor de una función entre dos puntos conocidos, asumiendo que el cambio entre ellos es lineal. Es simple y útil cuando los datos son aproximadamente rectos entre los puntos.

**Ejercicio resuelto:**  
Aproximar el valor de \( f(x) = \sqrt{x} \) en \( x = 6 \) usando los puntos conocidos \( (1, 1.0), (4, 2.0), (9, 3.0) \).

[ Ver código de interpolación lineal (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/bdb75c5a1b706f676c66ee02ac58ce55eb0c0466/codigos/tema5/Interpolacion%20Lineal.py)

---

### 2. Interpolación Polinómica (Lagrange)

**Descripción del método:**  
La interpolación polinómica de Lagrange construye un polinomio que pasa exactamente por todos los puntos conocidos. Es útil para estimar valores intermedios, pero puede ser inestable si se usan muchos puntos.

**Ejercicio resuelto:**  
Aproximar el valor de \( f(x) = x^2 \) en \( x = 3 \) usando los puntos \( (1, 1), (2, 4), (4, 16) \).

[ Ver código de interpolación polinómica (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/bdb75c5a1b706f676c66ee02ac58ce55eb0c0466/codigos/tema5/Interpolacion%20Polinomica%20(Lagrange).py)

### 3. Regresión Lineal

**Descripción del método:**  
La regresión lineal ajusta una recta a un conjunto de datos, minimizando la suma de los errores cuadrados. Es útil para modelar tendencias generales cuando los datos presentan ruido.

**Ejercicio resuelto:**  
Ajustar una recta a los datos de temperatura en función de la hora:  
Horas: [8, 12, 14, 16]  
Temperaturas: [15, 22, 25, 24]

[ Ver código de regresión lineal (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/bdb75c5a1b706f676c66ee02ac58ce55eb0c0466/codigos/tema5/Regresi%C3%B3n%20Lineal.py)

---

### 4. Correlación

**Descripción del método:**  
El coeficiente de correlación de Pearson mide la fuerza y dirección de la relación lineal entre dos variables. Un valor de 1 indica correlación positiva perfecta, -1 negativa perfecta y 0 ausencia de correlación lineal.

**Ejercicio resuelto:**  
Calcular el coeficiente de correlación para los datos:  
x: [1, 2, 3, 4, 5]  
y: [2, 4, 6, 8, 10]

[ Ver código de correlación (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/bdb75c5a1b706f676c66ee02ac58ce55eb0c0466/codigos/tema5/Correlaci%C3%B3n.py)

---

### 5. Mínimos Cuadrados

**Descripción del método:**  
El método de mínimos cuadrados ajusta una recta a los datos minimizando el error cuadrático medio. Es ampliamente usado para predicción y análisis de tendencias.

**Ejercicio resuelto:**  
Ajustar una recta a los datos:  
x: [1, 2, 3, 4, 5]  
y: [2.1, 3.9, 6.2, 7.8, 10.3]  
y estimar el valor para \( x = 6 \).

[ Ver código de mínimos cuadrados (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/bdb75c5a1b706f676c66ee02ac58ce55eb0c0466/codigos/tema5/M%C3%ADnimos%20Cuadrados.py)

## Caso de prueba: Método de Interpolacion lineal - error al dividir entre 0 

Se quiere resolver la siguiente funcion de interpolación lineal:

f(x) = y0 + (x−x0) * (y1−y0/x1-x0)

para el valor específico de x  =2.0

[ Ver caso de prueba ](https://github.com/sergiolb27/Metodos-Numericos-/blob/b0264ed9300907ab887c3367ddc201bbe190bb72/codigos/tema5/casoprueba%20(2).py)

¿Por qué falla?
La función falla porque tiene puntos duplicados consecutivos en X (x[0] = x[1] = 2.0) y el valor a interpolar (x_buscado = 2.0) coincide exactamente con esos puntos.
En la fórmula de interpolación lineal, el denominador (x1 - x0) se vuelve cero, causando una división por cero que Python no puede resolver.
Python lanza ZeroDivisionError cuando detecta división por cero, deteniendo completamente la ejecución del programa.


###  Programa 
[ Ver documento de la evaluacion en formato .docs, ](https://docs.google.com/document/d/1H1o9WfBWuakd4GwqDnt_SJYdxFQRNg-tlluIG9tSOvw/edit?usp=sharing)





[ Volver al README principal](../README.md)

