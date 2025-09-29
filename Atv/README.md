=============================
Trabalho Avaliativo - Erlang C
Vítor Possebon Bortoluzzi
=============================

Forma de implementação:
-----------------------
Escolhi a Opção B — várias funções, cada uma responsável por uma métrica.
Isso torna o código modular, fácil de ler, testar e manter. 
Se houver necessidade de corrigir apenas uma fórmula (ex.: Wq), só é preciso
ajustar a função correspondente.

Como usar:
----------
Ao executar `a.py`, o usuário deve escolher o modo de entrada:

1) Entrar com "a" (Erlangs) e "c" (nº de servidores).
   - Entradas:
       * a: tráfego oferecido (Erlangs = λ/μ)
       * c: número de servidores (inteiro > 0)
   - Saídas:
       * P(wait): probabilidade de espera
       * ρ: taxa de utilização do sistema

2) Entrar com λ, μ e c.
   - Entradas:
       * λ: taxa de chegadas (clientes/unidade de tempo)
       * μ: taxa de atendimento por servidor (clientes/unidade de tempo)
       * c: número de servidores (inteiro > 0)
   - Saídas:
       * P(wait): probabilidade de espera
       * ρ: taxa de utilização
       * Wq: tempo médio de espera na fila (mesma unidade de λ e μ)
       * Lq: número médio de clientes na fila
       * W: tempo médio no sistema
       * L: número médio de clientes no sistema

Estabilidade:
-------------
O sistema é estável se a < c (ou ρ < 1). 
Caso a ≥ c, o programa considera o sistema instável e retorna:
    P(wait) = 1
    Wq, W, Lq e L → ∞

Validações:
-----------
- c deve ser > 0
- μ deve ser > 0
- Entradas não numéricas são rejeitadas
- Caso o sistema seja instável, uma mensagem é mostrada e as métricas 
  viram infinitas.

Unidades:
---------
- λ: clientes/unidade de tempo
- μ: atendimentos/unidade de tempo
- a: Erlangs (λ/μ)
- Wq e W: unidade de tempo
- Lq e L: número de clientes
- ρ: proporção de utilização (0 ≤ ρ ≤ 1)