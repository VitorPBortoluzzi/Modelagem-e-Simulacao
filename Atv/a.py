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

def opc_1(a:float, c: int):
    p_Wait = erlang_c(a,c)
    p_util_serv = a/c

    print(f'Probabilidade de Espera: {p_Wait:.2f}')
    print(f'Taxa de Utilização do servidor: {p_util_serv:.2f}')


def opc_2(lam:float, mu:float, c:int) ->float:
    a = lam / mu
    p_Wait = erlang_c(a,c)
    p_util_serv = a/c
    Wq = p_Wait / (c * mu - lam)
    Lq = lam * Wq
    w = Wq + (1/mu)
    l = lam * w

    print(f'Probabilidade de Espera: {p_Wait:.2f}')
    print(f'Taxa de Utilização do servidor: {p_util_serv:.2f}')
    print(f'Tempo médio de espera na fila: {Wq:.2f}')
    print(f'Número médio de clientes na fila: {Lq:.2f}')
    print(f'Tempo médio no sistema: {w:.2f}')
    print(f'Número médio de clientes no sistema: {l:.2f}')


def main():
    print('\n=== Calculadora Erlang C (P(wait)) ===')
    print('1) Entrar com a (a = λ/μ) e c')
    print('2) Entrar com λ, μ e c')
    opc = input('Escolha (1/2): ').strip()
    
    if opc == '1':
        a = ler_float('Informe a (lam/mu) em Erlangs: ')
        c = ler_int('Informe c (nº de servidores)')

        opc_1(a,c)
        
    elif opc == '2':
        lam = ler_float('Informe λ (taxa de chegadas): ')
        mu = ler_float('Informe μ (taxa de atendimento por servidor): ')
        c   = ler_int('Informe c (nº de servidores): ')
        if mu <= 0:
            print('μ deve ser > 0. Encerrando')
            return
        opc_2(lam,mu,c)

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