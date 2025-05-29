# Tema 2: Métodos de Solución de Ecuaciones No Lineales

En el ámbito de la ciencia y la ingeniería, la mayoría de los problemas reales no se presentan de forma sencilla ni con soluciones exactas. Con frecuencia se trabaja con **ecuaciones no lineales** que no pueden resolverse con métodos algebraicos comunes. Por ejemplo:

- Estimar la trayectoria de un satélite considerando variaciones en la gravedad y la fricción atmosférica.
- Identificar estados de equilibrio en procesos químicos complejos.
- Mejorar el rendimiento de sistemas energéticos donde las variables están interrelacionadas.

Ante este tipo de situaciones, los **métodos numéricos** resultan fundamentales. A través de algoritmos iterativos, permiten obtener soluciones aproximadas con el nivel de precisión requerido. Estos métodos facilitan la implementación computacional, convirtiéndose en una pieza clave para abordar problemas que no pueden resolverse analíticamente. Gracias a ellos, es posible simular, modelar y optimizar sistemas complejos en diversas áreas del conocimiento.

---

## ¿Por qué usar métodos para resolver ecuaciones?

> "Cuando las soluciones exactas no existen o no son prácticas, los métodos numéricos marcan el camino."

**Usos destacados:**
- Cálculo de raíces en ecuaciones sin solución directa.
- Optimización de funciones complicadas.
- Resolución numérica de sistemas con múltiples incógnitas.
- Evaluación del comportamiento del error y verificación de la convergencia de los métodos.

### Problemario de Métodos de Solución

**Descripción:**  
Ejercicios prácticos enfocados en la aplicación de los métodos numéricos para encontrar raíces de ecuaciones no lineales. Cada subapartado describe brevemente el método utilizado y presenta un ejercicio representativo, resuelto con Python.

---

#### 1. Método de Bisección

**Descripción del método:**  
El método de bisección es un procedimiento iterativo que consiste en dividir repetidamente un intervalo en dos mitades y seleccionar la subintervalo donde ocurre un cambio de signo, garantizando así la existencia de una raíz. Es un método robusto y siempre converge si la función es continua y hay cambio de signo.

**Ejercicio resuelto:**  
Aproximar la raíz de la función \( f(x) = x^3 - 25 \) en el intervalo \([1, 3]\).

**Procedimiento:**  
Se seleccionan los extremos del intervalo, se verifica el cambio de signo, se calcula el punto medio y se repite el proceso hasta alcanzar la precisión deseada.



[🔗 Ver código de método de bisección (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/390e40270b0a4f3b5e712389f812fb8864b2495a/codigos/tema2/M%C3%A9todo%20de%20biseccion.py)

---

#### 2. Método de la Regla Falsa

**Descripción del método:**  
La regla falsa, o método de falsa posición, es similar a la bisección pero utiliza una aproximación lineal entre los extremos del intervalo para estimar la raíz. Es más rápido que la bisección en muchos casos, aunque puede estancarse si la función es muy asimétrica.

**Ejercicio resuelto:**  
Encontrar la raíz de \( f(x) = x^3 - x - 1 \) en el intervalo \([1, 2]\).

**Procedimiento:**  
Se usan los extremos del intervalo y la fórmula de la regla falsa para aproximar la raíz, actualizando el intervalo en cada iteración.



[🔗 Ver código de método de regla falsa (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/390e40270b0a4f3b5e712389f812fb8864b2495a/codigos/tema2/M%C3%A9todo%20de%20la%20regla%20falsa.py)

---

#### 3. Método de Punto Fijo

**Descripción del método:**  
El método de punto fijo transforma la ecuación original en una forma iterativa \( x = g(x) \) y utiliza una suposición inicial para generar una sucesión que converge a la raíz, siempre que la función de iteración cumpla ciertas condiciones de convergencia.

**Ejercicio resuelto:**  
Resolver \( f(x) = e^{-x} - x \) usando la función de iteración \( x = e^{-x} \).

**Procedimiento:**  
Se elige un valor inicial y se itera usando la función de punto fijo hasta que el error absoluto sea suficientemente pequeño.



[🔗 Ver código de método de punto fijo (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/390e40270b0a4f3b5e712389f812fb8864b2495a/codigos/tema2/M%C3%A9todo%20de%20punto%20fijo.py)

---

#### 4. Método de Newton-Raphson

**Descripción del método:**  
El método de Newton-Raphson utiliza la derivada de la función para construir una sucesión que converge rápidamente a la raíz, partiendo de una suposición inicial. Es muy eficiente, pero requiere que la derivada no sea cero y que la suposición inicial esté cerca de la raíz.

**Ejercicio resuelto:**  
Determinar la raíz de \( f(x) = x^3 - x - 1 \) usando un valor inicial \( x_0 = 1.5 \).

**Procedimiento:**  
Se calcula la derivada, se aplica la fórmula de Newton-Raphson y se repite hasta alcanzar la tolerancia deseada.



[🔗 Ver código de método de Newton-Raphson (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/390e40270b0a4f3b5e712389f812fb8864b2495a/codigos/tema2/M%C3%A9todo%20de%20Newton-Raphson.py)

---

#### 5. Método de la Secante

**Descripción del método:**  
El método de la secante es una variante del método de Newton-Raphson que no requiere el cálculo de la derivada. Utiliza dos aproximaciones iniciales y construye una sucesión usando una secante entre los puntos.

**Ejercicio resuelto:**  
Encontrar la raíz de \( f(x) = \cos(x) - x \) usando valores iniciales \( x_0 = 0.5 \) y \( x_1 = 1 \).

**Procedimiento:**  
Se aplica la fórmula de la secante iterativamente hasta que el error relativo sea suficientemente pequeño.



[🔗 Ver código de método de la secante (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/390e40270b0a4f3b5e712389f812fb8864b2495a/codigos/tema2/M%C3%A9todo%20de%20la%20secante.py)

---


[ Volver al README principal](../README.md)
