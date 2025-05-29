# Tema 4: Diferenciación e Integración Numérica

En las ciencias aplicadas y la ingeniería, muchas veces se trabaja con funciones cuya derivada o integral no puede obtenerse de manera exacta. Ya sea por la complejidad de la función o porque los datos provienen de experimentos, surge la necesidad de utilizar **métodos numéricos** para estimar derivadas e integrales.

Por ejemplo:

- Analizar la velocidad instantánea de un vehículo a partir de datos experimentales de posición.
- Calcular el área bajo la curva de una función de comportamiento no conocido con precisión .
- Estimar flujos de calor o cargas eléctricas en sistemas dinámicos donde las expresiones analíticas no son viables.

Aquí es donde entran en juego los métodos de **diferenciación e integración numérica**, permitiendo obtener aproximaciones útiles con alta precisión y eficiencia computacional.

## Importancia de la Diferenciación e Integración Numérica

> "Son técnicas que permiten traducir funciones continuas en cálculos discretos para resolver problemas reales."

**Aplicaciones principales:**
- Estimación de derivadas cuando no es posible derivar analíticamente.
- Cálculo de áreas, volúmenes y acumulados en procesos físicos.
- Solución de ecuaciones diferenciales mediante métodos numéricos.
- Modelado en ingeniería, física, biología y economía.


### Aplicación Práctica y Código

**Descripción:**  
Desarrollar programas en Python para implementar y comparar diferentes métodos de diferenciación e integración numérica. Cada ejercicio incluye el planteamiento del problema, el código implementado y la interpretación de resultados.

####  Método del Trapecio

**Descripción del método:**  
Este método aproxima el área bajo la curva dividiendo el intervalo en segmentos donde cada subárea es considerada un trapecio. Puede ser simple o compuesto para mayor precisión.

**Ejercicio resuelto:**  
Estimar el valor de la integral definida de \( f(x) = \ln(x) \) en el intervalo \([1, 2]\).

[ Ver código del método de Gauss (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/e26bd0d286256c871683fd435e8f4fa8cdd36a8b/codigos/tema4/Metodo%20del%20trapecio.py)


#### Regla de Simpson 1/3

**Descripción del método:**  
Este método utiliza parábolas para aproximar el área bajo la curva. Es muy preciso para funciones suaves y se aplica en intervalos pares.

**Ejercicio resuelto:**  
Calcular la integral de \( f(x) = e^{-x^2} \) en \([0, 1]\).

[ Ver código de Simpson 1/3 (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/e26bd0d286256c871683fd435e8f4fa8cdd36a8b/codigos/tema4/Metodo%20de%20Simpson%20un%20tercio.py)


#### Regla de Simpson 3/8

**Descripción del método:**  
Simpson 3/8 es una variante que utiliza polinomios cúbicos. Es útil cuando el número de subintervalos es múltiplo de 3.

**Ejercicio resuelto:**  
Aproximar la integral de \( f(x) = \sqrt{1 + x^4} \) en \([0, 3]\).

[ Ver código de Simpson 3/8 (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/e26bd0d286256c871683fd435e8f4fa8cdd36a8b/codigos/tema4/Metodo%20Simpson%20tres%20octavos.py)


#### Cuadratura Gaussiana

**Descripción del método:**  
Este método transforma la integral definida a una forma estándar y utiliza puntos y pesos especiales (raíces de polinomios de Legendre) para calcular una aproximación muy precisa.

**Ejercicio resuelto:**  
Evaluar la integral de \( f(x) = \frac{1}{1 + x^2} \) en \([-1, 1]\) usando 2 y 3 puntos.

[ Ver código de Cuadratura Gaussiana (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/e26bd0d286256c871683fd435e8f4fa8cdd36a8b/codigos/tema4/Cuadratura%20Gaussiana.py)

## Ejemplo: Limitación por valores no definidos (NaN o infinito) Metodo del trapecio.

Supón que el usuario ingresa la función:

funcion_str = "1/x"
a = -1
b = 1
n = 4
Aquí, la función 1/x no está definida en x = 0 (hay una discontinuidad), y Python (NumPy) devolverá un error o un valor inf o nan al evaluar en ese punto.

[Ver caso de prueba ](https://github.com/sergiolb27/Metodos-Numericos-/blob/d2a8bc01313feaaea7a15c9251888e550615513d/codigos/tema4/CasoPrueba%20(1).pyy)

[ Volver al README principal](../README.md)

