Vitor P. Bortoluzzi

===================

Escolhi o método de múltiplas Funções: (B) Várias funções (uma por métrica, ou por grupo de métricas).

Como motivo a modularidade e a facil manutenção do código;

Legibilidade e manutenção: cada função tem uma responsabilidade clara;
Reuso: Funções podem ser chamadas em outros contextos sem reescrever código;
Testabilidade:Funções podem ser testadas individualmente;

O código foi dividido em funções:
Cálculos:
    erlang_c(a,c) --> Retorna P(wait);                                          erlang_c(a: float, c: int) retorna float;
    utilizacao(a,c) --> calcula p(utilização por servidor);                     utilizacao(a: float, c: int) retorna float;
    tempo_espera_fila(pwait, lam, mu, c) --> retorna Wq;                        tempo_espera_fila(pwait: float, lam: float, mu: float, c:int) retorna float;
    clientes_fila(mu, wq) --> retorna Lq;                                       clientes_fila(lam: float, wq: float) retorna float;
    tempo_sistema(wq, mu) --> retorna W;                                        tempo_sistema(wq: float, mu: float) retorna float;
    clientes_sistema(lam, w) --> retorna L;                                     clientes_sistema(lam: float, w: float) retorna float;
Entradas:
    ler_float(msg) e ler_int(msg) padronizam leitura e validação de dados;
Principal:
    main() integra tudo e guia a interação com o usuário;
