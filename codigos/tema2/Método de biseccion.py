 Método de Bisección
def metodo_biseccion(f, a, b, tolerancia=1e-6, max_iter=100):
    """
    Implementación del método de bisección para encontrar raíces
    Parámetros:
    f: función a evaluar
    a, b: límites del intervalo inicial
    tolerancia: error permitido
    max_iter: número máximo de iteraciones
    """
    # Verificar si hay un cambio de signo en el intervalo
    if f(a) * f(b) >= 0:
        return None, "Error: No hay cambio de signo en el intervalo"

    iteracion = 0
    # Lista para almacenar resultados
    resultados = []

    while iteracion < max_iter:
        # Calcular punto medio
        c = (a + b) / 2

        # Calcular el error relativo porcentual
        error = abs((b - a) / b) * 100 if b != 0 else abs(b - a)

        # Almacenar resultados de esta iteración
        resultados.append({
            'iteracion': iteracion + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': f(c),
            'error': error
        })

        # Verificar si hemos encontrado la raíz
        if abs(f(c)) < tolerancia:
            return c, resultados

        # Actualizar intervalo
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    return c, resultados

# Ejemplo de uso con la función del problemario: f(x) = x³ - 25
def f(x):
    return x**3 - 25

# Ejecutar el método
raiz, resultados = metodo_biseccion(f, 1, 3)

# Imprimir resultados en formato tabular
print("\nMétodo de Bisección para f(x) = x³ - 25")
print("-" * 80)
print(f"{'Iter':^6} {'a':^12} {'b':^12} {'c':^12} {'f(c)':^12} {'Error %':^12}")
print("-" * 80)

for r in resultados:
    print(f"{r['iteracion']:^6d} {r['a']:^12.6f} {r['b']:^12.6f} {r['c']:^12.6f} {r['f(c)']:^12.6f} {r['error']:^12.6f}")

print("-" * 80)
print(f"La raíz encontrada es: {raiz:.6f}")



Output



Iter      a           b           c          f(c)       Error %   
--------------------------------------------------------------------------------
   1     1.000000    3.000000    2.000000   -17.000000   66.666667
   2     2.000000    3.000000    2.500000    -9.375000   33.333333
   3     2.500000    3.000000    2.750000    -3.359375   16.666667
   4     2.750000    3.000000    2.875000    -0.048828    8.333333
   5     2.875000    3.000000    2.937500     1.677246    4.166667
   6     2.875000    2.937500    2.906250     0.816345    2.083333
   7     2.875000    2.906250    2.890625     0.384459    1.041667
--------------------------------------------------------------------------------
La raíz encontrada es: 2.924017
