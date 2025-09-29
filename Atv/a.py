# -*- coding: utf-8 -*-
"""
=============================
|    Envio Atrasado         |
=============================
Vítor Possebon Bortoluzzi, Trabalho avaliativo de 3 Pontos
Implementação: Opção B — várias funções (uma por métrica ou grupo de métricas).

Justificativa da escolha:
-------------------------
Optei por implementar várias funções em vez de uma única porque isso deixa o
código mais organizado, modular e fácil de manter. Cada função fica responsável
por um cálculo específico (por exemplo: utilização do servidor, probabilidade
de espera, tempo médio na fila, etc.). Dessa forma, é possível testar, validar
ou até reaproveitar cada parte separadamente sem precisar executar todo o
programa. Além disso, caso seja necessário alterar uma fórmula, só é preciso
ajustar a função correspondente.

Forma de uso:
-------------
Ao executar o programa, o usuário escolhe uma das duas opções de entrada:

1) Informar diretamente o valor de "a" (tráfego oferecido em Erlangs, a = λ/μ)
   e o número de servidores "c".
   - Entradas: a (Erlangs), c (inteiro > 0)
   - Saídas: Probabilidade de Espera (P(wait)), Utilização do servidor (ρ)

2) Informar λ (taxa de chegadas), μ (taxa de atendimento por servidor) e "c".
   - Entradas: λ (clientes/unidade de tempo), μ (atendimentos/unidade de tempo), c (inteiro > 0)
   - Saídas:
        * Probabilidade de Espera: P(wait)
        * Utilização do servidor: ρ
        * Tempo médio de espera na fila: Wq (unidade de tempo)
        * Número médio de clientes na fila: Lq (clientes)
        * Tempo médio no sistema: W (unidade de tempo)
        * Número médio de clientes no sistema: L (clientes)

Validações implementadas:
-------------------------
- Não é permitido c <= 0.
- μ deve ser > 0.
- Caso a >= c (ou ρ > 1), o sistema é considerado instável:
  * P(wait) = 1.0
  * Métricas Wq, W, Lq e L tendem ao infinito.

Unidades:
---------
- λ: clientes/unidade de tempo
- μ: atendimentos/unidade de tempo por servidor
- a: Erlangs (tráfego oferecido)
- Wq e W: unidade de tempo
- Lq e L: número de clientes
- ρ: proporção de utilização (0 ≤ ρ ≤ 1)
"""

from math import factorial

def ler_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).replace(',', '.'))
        except ValueError:
            print('Valor inválido. Tente novamente.')

def ler_int(msg: str) -> int:
    while True:
        try:
            v = int(input(msg))
            if v <= 0:
                print('Digite um inteiro > 0.')
            else:
                return v
        except ValueError:
            print('Valor inválido. Tente novamente.')

def erlang_c(a:float, c:int)-> float:
    if a < 0 or c<=0:
        raise ValueError("'a' deve ser >=0 e 'c' > 0.")
    if a>=c:
        return 1.0
    
    soma = sum((a**n) / factorial(n) for n in range(c))
    termo = (a**c) / factorial(c) * (c / (c -a))
    return termo / (soma + termo)

def pratica(a:float = None, c:int = None, lam: float = None , mu:float = None):
    if a is None and lam is not None and mu is not None:
        a = lam / mu
    
    if a < c:
        return True
    elif a >= c:
        return
    

def utilizacao(a:float = None, c:int = None, lam: float = None , mu:float = None) -> float:
    if c is None:
        raise ValueError("É necessário fornecer o número de servidores (c).")
    
    if a is not None:
        rho = a / c
    elif lam is not None and mu is not None:
        rho = lam / (mu * c)
    else:
        raise ValueError("Forneça (a) ou (lam e mu).")
    
    if rho > 1:
        raise ValueError(f"Sistema instável: rho = {rho:.6f} > 1")
    
    return rho

def temp_fila(pwait:float, lam:float, mu:float , c:int) -> float:
    return pwait / (c * mu - lam)

def clientes_fila(lam:float , Wq:float):
    return lam * Wq
    
def tempo_Sistema(Wq:float , mu:float) -> float:
    return Wq + 1/mu

def clientes_sistema(lam:float, w:float) -> float:
    return lam * w


def main():
    print('\n=== Calculadora Erlang C (P(wait)) ===')
    print('1) Entrar com a (a = λ/μ) e c')
    print('2) Entrar com λ, μ e c')
    opc = input('Escolha (1/2): ').strip()
    
    if opc == '1':
        a = ler_float('Informe a (lam/mu) em Erlangs: ')
        c = ler_int('Informe c (nº de servidores)')

        if a >= c:  # instável
            print("\n Sistema instável: a ≥ c")
            print("Probabilidade de Espera = 1.0")
            return

        p_Wait = erlang_c(a,c)
        rho = utilizacao(a,c,None,None)
        print(f'Probabilidade de Espera: {p_Wait:.6f}')
        print(f'Taxa de Utilização do servidor: {rho:.6f}')
        
        
    elif opc == '2':
        lam = ler_float('Informe λ (taxa de chegadas): ')
        mu = ler_float('Informe μ (taxa de atendimento por servidor): ')
        c   = ler_int('Informe c (nº de servidores): ')
        if mu <= 0:
            print('μ deve ser > 0. Encerrando')
            return
        
        a = lam/mu

        if a >= c:  # instável
            print("\n Sistema instável: a ≥ c")
            print("Probabilidade de Espera = 1.0")
            print("Wq, W, Lq, L → ∞")
            return

        p_Wait = erlang_c(a,c)
        rho = utilizacao(None,c,lam,mu)
        Wq = temp_fila(p_Wait,lam,mu,c)
        Lq = clientes_fila(lam,Wq)
        w = tempo_Sistema(Wq,mu)
        l = clientes_sistema(lam,w)

        print(f'Probabilidade de Espera: {p_Wait:.6f}')
        print(f'Taxa de Utilização do servidor: {rho:.6f}')
        print(f'Tempo médio de espera na fila: {Wq:.6f}')
        print(f'Número médio de clientes na fila: {Lq:.6f}')
        print(f'Tempo médio no sistema: {w:.6f}')
        print(f'Número médio de clientes no sistema: {l:.6f}')

    else:
        print('Opção inválida. Encerrando.')
        return
    
if __name__ == '__main__':
    while True:
        main()
        denovo = input('\nDeseja calcular novamente? (s/n): ').strip().lower()
        if denovo != 's':
            print('Encerrado.')
            break