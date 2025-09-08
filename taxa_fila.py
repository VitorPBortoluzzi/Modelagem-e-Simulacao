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

# Criando o gráfico de linhas para as chegadas por minuto
plt.plot(range(1, 31), chegada_p_minuto, marker='o', linestyle='-', color='b')

# Adicionando título e rótulos
plt.title("Chegadas por Minuto (12h00 às 12h30)")
plt.xlabel("Minuto")
plt.ylabel("Número de Chegadas")

# Exibindo o gráfico
plt.grid(True)  # Adiciona grid ao gráfico para melhor visualização
plt.show()