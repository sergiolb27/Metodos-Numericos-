# Tema 3: Métodos de Solución de Sistemas de Ecuaciones

## Contexto Fundamental

En las ciencias e ingeniería, es común enfrentarse a problemas que requieren la resolución de múltiples ecuaciones simultáneamente. Estos sistemas de ecuaciones lineales aparecen en contextos como:

- El análisis estructural de puentes y edificios , donde se equilibran fuerzas en múltiples direcciones.
- La simulación de redes eléctricas , en las que se calculan corrientes y voltajes en mallas complejas.
- La modelación económica , en la que múltiples variables interdependientes deben satisfacer restricciones simultáneas.

Dado que resolver estos sistemas de forma manual no es práctico cuando el número de ecuaciones crece, se emplean **métodos numéricos** que permiten obtener soluciones aproximadas de manera eficiente mediante el uso de computadoras. Estos métodos, como **Gauss, Gauss-Jordan, LU, Jacobi y Gauss-Seidel**, son fundamentales en simulación, análisis de datos y cálculo científico.

## Importancia de los Métodos de Solución

> "Son las claves para desentrañar sistemas complejos que gobiernan el comportamiento del mundo físico y social."

**Aplicaciones principales:**
- Resolver sistemas lineales grandes y/o mal condicionados.
- Análisis estructural y térmico.
- Optimización y modelos predictivos.
- Simulaciones de fenómenos físicos, químicos y económicos.

### Problemario de Métodos de Solución

**Descripción:**  
Ejercicios prácticos enfocados en la aplicación de métodos numéricos para resolver sistemas de ecuaciones lineales. Cada subapartado describe brevemente el método y presenta un ejercicio resuelto con Python.

#### 1. Método de Eliminacion Gaussiana

**Descripción:**  
El método de eliminación de Gauss transforma el sistema original en uno triangular superior mediante operaciones fila, para luego resolver por sustitución hacia atrás.

**Ejercicio resuelto:**  
Resolver un sistema de 3x3 ecuaciones con coeficientes conocidos.

[ Ver código del método de Gauss (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/212b080085a77f9436c557a73cb78d215960f9bb/codigos/tema3/Eliminacion%20Gaussiana%20con%20pivote.py)

#### 2. Método de Gauss-Jordan

**Descripción:**  
Extiende el método de Gauss, eliminando también los elementos por encima de la diagonal principal para obtener una matriz identidad.

**Ejercicio resuelto:**  
Resolver el mismo sistema de 3x3 por Gauss-Jordan.

[ Ver código del método de Gauss-Jordan (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/212b080085a77f9436c557a73cb78d215960f9bb/codigos/tema3/Metodo%20Gauss%20Jordan.py)

#### 3. Método de Jacobi

**Descripción:**  
Es un método iterativo que calcula nuevas aproximaciones de cada variable usando los valores de la iteración anterior. Requiere matrices diagonales dominantes.

**Ejercicio resuelto:**  
Resolver un sistema iterativamente con Jacobi.

[ Ver código del método de Jacobi (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/212b080085a77f9436c557a73cb78d215960f9bb/codigos/tema3/Metodo%20de%20Jacobi.py)

#### 4. Método de Gauss-Seidel

**Descripción:**  
Similar al de Jacobi, pero utiliza inmediatamente los nuevos valores calculados en cada iteración, lo cual acelera la convergencia en muchos casos.

**Ejercicio resuelto:**  
Aplicar Gauss-Seidel a un sistema de 3x3.

[ Ver código del método de Gauss-Seidel (Python)](https://github.com/sergiolb27/Metodos-Numericos-/blob/212b080085a77f9436c557a73cb78d215960f9bb/codigos/tema3/Metodo%20de%20Gauss-Seidel.py)

## Caso de prueba: Ejemplo: Cuando el pivote de una columna es 0 Gauss-Jordan 
Resolver el siguiente sistema de ecuaciones lineales utilizando el método de eliminación Gauss-Jordan con pivoteo parcial. El usuario ingresa la matriz aumentada correspondiente y el programa muestra paso a paso el proceso hasta encontrar la solución:
                                                                                                                        
**x−2y=1**
**2x−4y=3**

[ Ver caso de prueba ](https://github.com/sergiolb27/Metodos-Numericos-/blob/212b080085a77f9436c557a73cb78d215960f9bb/codigos/tema3/CasoPrueba.py)

[ Volver al README principal](../README.md)

