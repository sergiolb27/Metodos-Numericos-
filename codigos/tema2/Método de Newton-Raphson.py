Método de Newton-Raphson - Ejemplo de ejercicio resuelto 


def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson
    Parámetros:
    f: función a evaluar
    df: derivada de la función
    x0: valor inicial
    tolerancia: error permitido
    max_iter: número máximo de iteraciones
    """
    iteracion = 0
    resultados = []
    x_ant = x0

    while iteracion < max_iter:
        # Calcular siguiente valor usando la fórmula de Newton-Raphson
        f_x = f(x_ant)
        df_x = df(x_ant)

        # Verificar si la derivada es cercana a cero
        if abs(df_x) < 1e-10:
            return None, "Error: Derivada cercana a cero"

        x = x_ant - f_x / df_x

        # Calcular error relativo porcentual
        error = abs((x - x_ant) / x) * 100 if x != 0 else abs(x - x_ant)

        # Almacenar resultados
        resultados.append({
            'iteracion': iteracion + 1,
            'x_n': x_ant,
            'f(x_n)': f_x,
            'f\'(x_n)': df_x,
            'x_n+1': x,
            'error': error
        })

        # Verificar convergencia
        if abs(x - x_ant) < tolerancia:
            return x, resultados

        x_ant = x
        iteracion += 1

    return x, resultados

# Ejemplo de uso con la función del Problemario: f(x) = x³ - x - 1
def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

# Ejecutar el método
raiz, resultados = newton_raphson(f, df, 1.5)

# Imprimir resultados
print("\nMétodo de Newton-Raphson para f(x) = x³ - x - 1")
print("-" * 90)
print(f"{'Iter':^6} {'x_n':^12} {'f(x_n)':^12} {'f\'(x_n)':^12} {'x_n+1':^12} {'Error %':^12}")
print("-" * 90)

for r in resultados:
    print(f"{r['iteracion']:^6d} {r['x_n']:^12.6f} {r['f(x_n)']:^12.6f} {r['f\'(x_n)']:^12.6f} {r['x_n+1']:^12.6f} {r['error']:^12.6f}")

print("-" * 90)
print(f"La raíz encontrada es: {raiz:.6f}")



Output:

Método de Newton-Raphson para f(x) = x³ - x - 1
------------------------------------------------------------------------------------------
 Iter      x_n        f(x_n)      f'(x_n)      x_n+1       Error %   
------------------------------------------------------------------------------------------
   1     1.500000    1.375000    5.750000    1.260870    18.967391
   2     1.260870    0.267850    3.765424    1.189726    5.980892
   3     1.189726    0.023843    3.242542    1.182377    0.622321
   4     1.182377    0.000205    3.189486    1.182313    0.005435
   5     1.182313    0.000000    3.189296    1.182313    0.000000
------------------------------------------------------------------------------------------
La raíz encontrada es: 1.182313
