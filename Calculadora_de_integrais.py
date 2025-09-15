from sympy import symbols, parse_expr, sin, exp, log
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, convert_xor

# Define a variável simbólica 'x'
x = symbols('x')

def calcular_integral(funcao_expr, a, b, n):
    delta_x = (b - a) / n
    soma_area = 0

    for i in range(n):
        x_i = a + i * delta_x
        # Substitui o valor de x na expressão da função para calcular a altura
        soma_area += funcao_expr.subs(x, x_i) * delta_x

    return soma_area

# --- Funções de Exemplo ---
# Para usar uma delas, descomente a função desejada e comente as outras.

# Exemplo 1: f(x) = x**2
funcao_selecionada = x**2
funcao_nome = "x**2"

# Exemplo 2: f(x) = sin(x)
#funcao_selecionada = sin(x)
#funcao_nome = "sin(x)"

# Exemplo 3: f(x) = exp(x)
#funcao_selecionada = exp(x)
#funcao_nome = "exp(x)"

# Exemplo 4: f(x) = log(x)
#funcao_selecionada = log(x)
#funcao_nome = "log(x)"

# Exemplo 5: f(x) = x**3 + 2*x - 1
#funcao_selecionada = x**3 + 2*x - 1
#funcao_nome = "x**3 + 2*x - 1"

# --- Bloco Principal ---
if __name__ == "__main__":
    print("--- Calculadora de Integrais - Método dos Retângulos ---")

    # Define os limites e o número de divisões
    a = 0.0
    b = 2.0
    n = 1000

    # Chama a função para calcular a integral com a função selecionada
    resultado = calcular_integral(funcao_selecionada, a, b, n)

    # Exibe o resultado
    print(f"\n--- Resultado ---")
    print(f"Função selecionada: '{funcao_nome}'")
    print(f"Intervalo de cálculo: [{a}, {b}]")
    print(f"Número de retângulos: {n}")
    print(f"A integral é aproximadamente: {resultado}")