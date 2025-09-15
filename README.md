# Calculadora de Integrais - Método dos Retângulos

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![SymPy](https://img.shields.io/badge/Uses-SymPy-66cc33.svg)](https://www.sympy.org/en/index.html)

Este projeto implementa uma calculadora de integrais definidas que utiliza o **Método da Soma de Riemann à Esquerda**. O objetivo é fornecer uma ferramenta simples e didática para aproximar o valor da área sob a curva de uma função em um dado intervalo $[a, b]$, utilizando a biblioteca **SymPy** para a manipulação de expressões matemáticas.

## Tabela de Conteúdo

- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Como Usar](#como-usar)
- [Como o Código Funciona](#como-o-código-funciona)
- [Link do Video no YouTube](#link-do-video-no-youtube)

---

## Visão Geral

O projeto se baseia no princípio da Soma de Riemann, que aproxima uma integral definida somando as áreas de múltiplos retângulos infinitesimais. A flexibilidade do código permite ao usuário escolher entre várias funções pré-definidas (`x**2`, `sin(x)`, `exp(x)`, `log(x)`, etc.) e ajustar os limites do intervalo de integração, bem como o número de retângulos para maior precisão.

---

## Pré-requisitos

Para rodar este código, você precisa ter o **Python** e a biblioteca **SymPy** instalados em sua máquina. Se você não os tiver, você pode instalar a biblioteca SymPy via `pip`:

```bash
    pip install sympy
```

## Como Usar:
Salve o código em um arquivo Python, por exemplo, calculadora_riemann.py.

Abra o arquivo em um editor de texto ou IDE.

Escolha a função que deseja integrar, no bloco de código: 

```bash
--- Funções de Exemplo --- 
```

escomente a linha da função desejada e comente as outras.

Exemplo: Para calcular a integral de sin(x):


```bash 
´Exemplo 1: f(x) = x**2

funcao_selecionada = x**2

funcao_nome = "x**2"´

```


```bash
Exemplo 2: f(x) = sin(x)

funcao_selecionada = sin(x)

funcao_nome = "sin(x)"
```

As outras funções devem estar comentadas, deve ajustar os parâmetros na linha:
```bash
 --- Bloco Principal ---
```
Modifique os valores de a (limite inferior), b (limite superior) e n (número de retângulos) conforme necessário:

```bash

a = 0.0  # Limite inferior
b = 2.0  # Limite superior
n = 1000 # Número de retângulos
```

Execute o script a partir do terminal:
```bash
python calculadora_riemann.py
```
O resultado da aproximação será exibido no console.

## Como o Código Funciona

O projeto se baseia na função calcular_integral que implementa a Soma de Riemann à Esquerda. O processo é simples e direto:

1º Cálculo da Largura (Δx): A função divide o intervalo total (b−a) pelo número de retângulos (n) para determinar a largura de cada retângulo. A fórmula é: Δx=(b−a)/n


2º Soma das Áreas: Um laço de repetição (for) itera n vezes. Em cada iteração, ele calcula a altura do retângulo (o valor da função no ponto x_i) e multiplica pela largura Δx para obter a área. Essa área é adicionada a um somatório.

3º Resultado: Após percorrer todos os subintervalos, a função retorna o valor acumulado, que é a aproximação da integral.


## Link do Video no YouTube

[Video no YouTube](https://www.youtube.com/watch?v=k4Rsy8GbKE0&t=10s&ab_channel=FernandaKipper%7CDev)
















