import matplotlib.pyplot as plt

# qtd_chegada = int(input("Quantidade de chegadas em 30 min: "))
qtd_atendentes = int(input("Quantidade de atendentes: "))
tmp_atendimento = [1.5, 1.8, 2.0, 1.6, 1.7]

# for i in range(30):
#     chegada = int(input(f"\t Chegadas no {i+1}º minuto: "))
#     chegada_p_minuto.append(chegada)

chegada_p_minuto = [3, 5, 4, 2, 6, 7, 5, 4, 3, 4, 5, 2, 3, 4, 6, 3, 5, 4, 3, 2, 5, 4, 6, 5, 3, 4, 2, 3, 4, 5]
# print("Tempo de atendimento nos 5 primeiros atendimentos: ")
# for i in range(5):
#     tmp = float(input("\t Tempo de atendimento(em minutos): "))
#     tmp_atendimento.append(tmp)
    
tmp_medio_atendimento = sum(tmp_atendimento) / len(tmp_atendimento)

taxa_chegada = len(chegada_p_minuto) / 30
taxa_atendimento = 1 / tmp_medio_atendimento
taxa_ocupacao = (taxa_chegada / (qtd_atendentes * taxa_atendimento))

print("ANÁLISE DE FILAS - Buffet RU da Faculdade\n Horário: 12 às 12h30min")

print("DADOS COLETADOS: ")
print("\t Total de chegadas em 30 min: ",len(chegada_p_minuto))
print("\t Numero de atendentes: ",qtd_atendentes)
print(f"\t Tempo médio de atendimento (min): {tmp_medio_atendimento:.2f} minutos")

print("\n RESULTADOS: ")
print("\t Taxa de chegada (λ):)",taxa_chegada ,"clientes/minuto")
print(f"\t Taxa de atendimento (μ): {taxa_atendimento:.2f} clientes/minuto")
print(f"\t Taxa de Ocupação (ρ): {taxa_ocupacao:.2f} clientes/minuto")
if taxa_ocupacao > 1:
    print(f"\t Taxa de Ocupação (ρ): {taxa_ocupacao:.2f}\n SISTEMA SOBRECARREGADO")


# Criando o gráfico de linhas para as chegadas por minuto
plt.plot(range(1, 31), chegada_p_minuto, marker='o', linestyle='-', color='b')

# Adicionando título e rótulos
plt.title("Chegadas por Minuto (12h00 às 12h30)")
plt.xlabel("Minuto")
plt.ylabel("Número de Chegadas")

# Exibindo o gráfico
plt.grid(True)  # Adiciona grid ao gráfico para melhor visualização
plt.show()


# =========================
# Cenário 2 - Caixa Supermercado
# =========================

qtd_atendentes_sm = int(input("Quantidade de caixas abertos: "))

# tempos de atendimento em minutos (amostra coletada)
tmp_atendimento_sm = [3.2, 2.8, 3.5, 3.0, 3.3]  # mais demorados que RU

# chegadas por minuto (30 min de observação)
chegada_p_minuto_sm = [2, 3, 2, 4, 3, 2, 5, 3, 4, 2, 
                    3, 3, 4, 5, 3, 2, 4, 3, 5, 2, 
                    3, 2, 4, 3, 3, 2, 5, 4, 3, 2]

# cálculo do tempo médio de atendimento
tmp_medio_atendimento_sm = sum(tmp_atendimento_sm) / len(tmp_atendimento)

# parâmetros de teoria das filas
taxa_chegada_sm = sum(chegada_p_minuto_sm) / 30  # média de clientes por minuto
taxa_atendimento_sm = 1 / tmp_medio_atendimento_sm
taxa_ocupacao_sm = (taxa_chegada_sm / (qtd_atendentes_sm * taxa_atendimento_sm))

print("\nANÁLISE DE FILAS - Caixa Supermercado\n Horário: 18h às 18h30min")

print("DADOS COLETADOS: ")
print("\t Total de chegadas em 30 min: ", sum(chegada_p_minuto_sm))
print("\t Numero de caixas (atendentes): ", qtd_atendentes_sm)
print(f"\t Tempo médio de atendimento (min): {tmp_medio_atendimento_sm:.2f} minutos")

print("\nRESULTADOS: ")
print(f"\t Taxa de chegada (λ): {taxa_chegada_sm:.2f} clientes/minuto")
print(f"\t Taxa de atendimento (μ): {taxa_atendimento_sm:.2f} clientes/minuto")

if taxa_ocupacao > 1:
    print(f"\t Taxa de Ocupação (ρ): {taxa_ocupacao:.2f}\n SISTEMA SOBRECARREGADO")
else: print(f"\t Taxa de Ocupação (ρ): {taxa_ocupacao_sm:.2f}")
# gráfico de chegadas por minuto
plt.plot(range(1, 31), chegada_p_minuto_sm, marker='o', linestyle='-', color='g')
plt.title("Chegadas por Minuto (18h00 às 18h30) - Supermercado")
plt.xlabel("Minuto")
plt.ylabel("Número de Chegadas")
plt.grid(True)
plt.show()