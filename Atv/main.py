# -*- coding: utf-8 -*-
# Vítor P. Bortoluzzi
"""
Calculadora mínima de Erlang C (P(wait)) em M/M/c 

Símbolos e fórmulas (todas no contexto M/M/c):
- λ (lambda): taxa de chegadas (clientes por unidade de tempo)
- μ (mi): taxa de atendimento de CADA servidor (clientes por unidade de tempo)
- c: número de servidores idênticos

Derivadas:
- a = λ/μ  (Erlangs)  → tráfego oferecido (carga média ofertada ao sistema)
- ρ = a/c = λ/(c μ)   → utilização média por servidor (0 < ρ < 1 para regime estável)

Fórmula de Erlang C (probabilidade de esperar na fila):
            (a^c / c!) * (c / (c − a))
P(wait) = ---------------------------------------------
          Σ_{n=0}^{c−1} (a^n / n!)  +  (a^c / c!) * (c / (c − a))

Observações:
- Estabilidade prática: a < c  (se a ≥ c, a fila “explode” e P(wait) → 1).
- Unidades de tempo em Wq e W são as mesmas usadas em λ e μ (min, h, ...).

A partir de P(wait), demais métricas (opcionais, mostradas aqui para referência):
- Wq = P(wait) / (c μ − λ)               (tempo médio de espera na fila)
- Lq = λ * Wq                             (número médio na fila — Little)
- W  = Wq + 1/μ                           (tempo médio no sistema)
- L  = λ * W                              (número médio no sistema — Little)

"""

from math import factorial

def erlang_c(a: float, c: int) -> float:
    """Retorna P(wait) dado o tráfego oferecido a=λ/μ (Erlangs) e c servidores.
    Observação: para estabilidade prática, é necessário a < c.
    """
    if a < 0 or c <= 0:
        raise ValueError("'a' deve ser >= 0 e 'c' > 0.")
    if a >= c:
        return 1.0  # sistema instável: P(wait) tende a 1
    
    #Formula: P(wait) = [ (a^c / c!) ×(c / (c -a)) ] / [ Σ(a^n / n!) + (a^c / c!) ×(c / (c -a)) ]
    soma = sum((a**n) / factorial(n) for n in range(c))        # Σ_{n=0}^{c-1} a^n/n!
    termo = (a**c) / factorial(c) * (c / (c - a))              # (a^c/c!) * (c/(c-a))
    return termo / (soma + termo)

def utilizacao(a: float, c: int) -> float:
    # print("Utilização média por servidor (p = a/c).")
    return a/c

def tempo_espera_fila(pwait: float, lam: float, mu: float, c:int) -> float:
    #- Wq = P(wait) / (c μ − λ)               (tempo médio de espera na fila)
    # print("Tempo médio de espera na fila (Wq).")
    return pwait / (c * mu - lam)

def clientes_fila(lam: float, wq: float) -> float:
    #- Lq = λ * Wq                             (número médio na fila — Little)
    # print("Número médio de clientes na fila (Lq).")
    return lam * wq

def tempo_sistema(wq: float, mu: float) -> float:
    #- W  = Wq + 1/μ                           (tempo médio no sistema)
    # print("Tempo médio do sistema (W = Wq + 1/u).")
    return wq + 1/mu

def clientes_sistema(lam: float, w: float) -> float:
    #- L  = λ * W                              (número médio no sistema — Little)
    # print("Número médio de clientes no sistema (L = lam * W)")
    return lam * w

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


 
def main():
    print('\n=== Calculadora Erlang C (P(wait)) ===')
    print('1) Entrar com a = λ/μ (Erlangs) e c')
    print('2) Entrar com λ, μ e c')
    opc = input('Escolha (1/2): ').strip()
    
    if opc == '1':
        a = ler_float('Informe a (λ/μ) em Erlangs: ')
        c = ler_int('Informe c (nº de servidores): ')

        p = erlang_c(a, c)
        rho = utilizacao(a, c)
    elif opc == '2':
        lam = ler_float('Informe λ (taxa de chegadas): ')
        mu  = ler_float('Informe μ (taxa de atendimento por servidor): ')
        c   = ler_int('Informe c (nº de servidores): ')
        if mu <= 0:
            print('μ deve ser > 0. Encerrando.')
            return
        a = lam / mu
        print(f'a = λ/μ = {a:.6f} Erlangs')
        if a >= c:
            print('Atenção: a ≥ c ⇒ sistema instável (fila explode).')
        else:
            p = erlang_c(a, c)
            rho = utilizacao(a, c)
            wq = tempo_espera_fila(p, lam, mu, c)
            lq = clientes_fila(lam, wq)
            w  = tempo_sistema(wq, mu)
            l  = clientes_sistema(lam, w)

        print(f'Tempo médio de espera na fila Wq = {wq:.6f}')
        print(f'Nº médio de clientes na fila Lq = {lq:.6f}')
        print(f'Tempo médio no sistema W = {w:.6f}')
        print(f'Nº médio de clientes no sistema L = {l:.6f}')

    else:
        print('Opção inválida. Encerrando.')
        return


    print(f'\nP(wait) = {p:.6f}  ({p*100:.2f}%)')
    print(f'Utilização média ρ = {rho:.6f}')
        

if __name__ == '__main__':
    while True:
        main()
        denovo = input('\nDeseja calcular novamente? (s/n): ').strip().lower()
        if denovo != 's':
            print('Encerrado.')
            break