import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


### GRAFICO DE INVESTIMENTOS
df_investimentos = pd.read_csv("investimentos.csv")

# Verificar o intervalo de anos para garantir que todos sejam mostrados
anos = df_investimentos['ano'].unique()
anos = sorted(anos)  # Ordenar os anos, se necessário

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Plotar os dados
plt.plot(df_investimentos['ano'], df_investimentos['total_liquidado'], label="Total Liquidado",linestyle='-', color='b')
plt.plot(df_investimentos['ano'], df_investimentos['total_pago'], label="Total Pago",linestyle='-', color='orange')

# Adicionar título e rótulos aos eixos
plt.title('Total Investido ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Valor Investido (Bi R$)')

# Definir ticks do eixo x para incluir todos os anos
plt.xticks(anos)

# Adicionar a legenda
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig("graficoInvestimentos.png")

# Mostrar o gráfico
plt.show()



### GRAFICO DE ENCARGOS
df_encargos = pd.read_csv("encargos.csv")

# Verificar o intervalo de anos para garantir que todos sejam mostrados
anos2 = df_encargos['ano'].unique()
anos2 = sorted(anos)  # Ordenar os anos, se necessário

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Plotar os dados
plt.plot(df_encargos['ano'], df_encargos['total_liquidado'], label="Total Liquidado",linestyle='-', color='b')
plt.plot(df_encargos['ano'], df_encargos['total_pago'], label="Total Pago",linestyle='-', color='orange')

# Adicionar título e rótulos aos eixos
plt.title('Total pago para Pessoal e Encargos Sociais ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Valor Investido (Bi R$)')

# Definir ticks do eixo x para incluir todos os anos
plt.xticks(anos2)

# Adicionar a legenda
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig("graficoEncargos.png")

plt.show()



### Grafico de Outras despesas
df_despesas = pd.read_csv("outrasDespesas.csv")

# Verificar o intervalo de anos para garantir que todos sejam mostrados
anos3 = df_despesas['ano'].unique()
anos3 = sorted(anos)  # Ordenar os anos, se necessário

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Plotar os dados
plt.plot(df_despesas['ano'], df_despesas['total_liquidado'], label="Total Liquidado",linestyle='-', color='b')
plt.plot(df_despesas['ano'], df_despesas['total_pago'], label="Total Pago",linestyle='-', color='orange')

# Adicionar título e rótulos aos eixos
plt.title('Total pago para Outras Despesas ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Valor Investido (Bi R$)')

# Definir ticks do eixo x para incluir todos os anos
plt.xticks(anos3)

# Adicionar a legenda
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig("graficoDespesas.png")

plt.show()


### GRAFICO DE GASTO TOTAIS
df_totalGastos = pd.read_csv("totalGastos.csv")

# Verificar o intervalo de anos para garantir que todos sejam mostrados
anos4 = df_totalGastos['ano'].unique()
anos4 = sorted(anos)  # Ordenar os anos, se necessário

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Plotar os dados
plt.plot(df_totalGastos['ano'], df_totalGastos['total_liquidado'], label="Total Liquidado",linestyle='-', color='b')
plt.plot(df_totalGastos['ano'], df_totalGastos['total_pago'], label="Total Pago",linestyle='-', color='orange')

# Adicionar título e rótulos aos eixos
plt.title('Gastos Totais ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Valor Investido (Bi R$)')

# Definir ticks do eixo x para incluir todos os anos
plt.xticks(anos4)

# Adicionar a legenda
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig("graficoTotal.png")

plt.show()


### GRAFICO DE ANALFABETISMO
# Ler os dados do arquivo CSV
df_analfa = pd.read_csv("analfabetismo.csv")

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 6))

# Definir as colunas de anos e os diferentes grupos de idade
anos = df_analfa['ano']
grupos = ['15-18', '18-25', '25-40', '40-60', '60+']
cores = ['blue', 'green', 'red', 'purple', 'orange']

# Plotar os dados e adicionar linhas de regressão para cada grupo de idade
for grupo, cor in zip(grupos, cores):
    plt.plot(anos, df_analfa[grupo], linestyle='-', label=f'{grupo} anos', color=cor)

    # Calcular a regressão linear para o grupo atual
    slope, intercept, _, _, _ = linregress(anos, df_analfa[grupo])
    regressao = slope * anos + intercept
    plt.plot(anos, regressao, linestyle='--', color=cor)

# Adicionar título e rótulos aos eixos
plt.title("Pessoas de 15 anos ou mais, analfabetas pelo grupo de idade")
plt.xlabel("Ano")
plt.ylabel("Quantidade de pessoas")

# Adicionar a legenda
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig("graficoAnalfabetismo.png")

# Mostrar o gráfico
plt.show()



df_analfa2 = pd.read_csv("analfabetismo2.csv")
df_analfa3 = pd.read_csv("analfabetismo3.csv")
df_analfa4 = pd.read_csv("analfabetismo4.csv")


### Gráfico analfabetismo 2
# Criar o gráfico
plt.figure(figsize=(10, 6))

# Plotar a primeira variável com bolinhas
plt.plot(df_analfa2["investimentos"], df_analfa2["15-18"], 'o', color='blue', label='15-18 anos')

# Calcular e plotar a linha de regressão para a primeira variável
slope1, intercept1, _, _, _ = linregress(df_analfa2["investimentos"], df_analfa2['15-18'])
regressao1 = slope1 * df_analfa2["investimentos"] + intercept1
plt.plot(df_analfa2["investimentos"], regressao1, linestyle='--', color='blue')

# Plotar a segunda variável com bolinhas
plt.plot(df_analfa2["investimentos"], df_analfa2["40-60"], 'o', color='green', label='40-60 anos')

# Calcular e plotar a linha de regressão para a segunda variável
slope2, intercept2, _, _, _ = linregress(df_analfa2["investimentos"], df_analfa2["40-60"])
regressao2 = slope2 * df_analfa2["investimentos"] + intercept2
plt.plot(df_analfa2["investimentos"], regressao2, linestyle='--', color='green')

# Adicionar títulos e legendas
plt.title('Diferença de 1 ano')
plt.xlabel('Investimento %')
plt.ylabel('Quantidade de analfabetos %')
plt.legend()
plt.savefig("graficoanalfa2.png")

# Mostrar o gráfico
plt.show()


### Gráfico analfabetismo 3
# Criar o gráfico
plt.figure(figsize=(10, 6))

# Plotar a primeira variável com bolinhas
plt.plot(df_analfa3["investimentos"], df_analfa3['15-18'], 'o', color='blue', label='15-18 anos')

# Calcular e plotar a linha de regressão para a primeira variável
slope1, intercept1, _, _, _ = linregress(df_analfa3["investimentos"], df_analfa3['15-18'])
regressao1 = slope1 * df_analfa3["investimentos"] + intercept1
plt.plot(df_analfa3["investimentos"], regressao1, linestyle='--', color='blue')

# Plotar a segunda variável com bolinhas
plt.plot(df_analfa3["investimentos"], df_analfa3["40-60"], 'o', color='green', label='40-60 anos')

# Calcular e plotar a linha de regressão para a segunda variável
slope2, intercept2, _, _, _ = linregress(df_analfa3["investimentos"], df_analfa3["40-60"])
regressao2 = slope2 * df_analfa3["investimentos"] + intercept2
plt.plot(df_analfa3["investimentos"], regressao2, linestyle='--', color='green')

# Adicionar títulos e legendas
plt.title('Diferença de 2 anos')
plt.xlabel('Investimento %')
plt.ylabel('Quantidade de analfabetos %')
plt.legend()
plt.savefig("graficoanalfa3.png")

# Mostrar o gráfico
plt.show()


### Gráfico analfabetismo 4
# Criar o gráfico
plt.figure(figsize=(10, 6))

# Plotar a primeira variável com bolinhas
plt.plot(df_analfa4["investimentos"], df_analfa4['15-18'], 'o', color='blue', label='15-18 anos')

# Calcular e plotar a linha de regressão para a primeira variável
slope1, intercept1, _, _, _ = linregress(df_analfa4["investimentos"], df_analfa4['15-18'])
regressao1 = slope1 * df_analfa4["investimentos"] + intercept1
plt.plot(df_analfa4["investimentos"], regressao1, linestyle='--', color='blue')

# Plotar a segunda variável com bolinhas
plt.plot(df_analfa4["investimentos"], df_analfa4["40-60"], 'o', color='green', label='40-60 anos')

# Calcular e plotar a linha de regressão para a segunda variável
slope2, intercept2, _, _, _ = linregress(df_analfa4["investimentos"], df_analfa4["40-60"])
regressao2 = slope2 * df_analfa4["investimentos"] + intercept2
plt.plot(df_analfa4["investimentos"], regressao2, linestyle='--', color='green')

# Adicionar títulos e legendas
plt.title('Diferença de 3 Anos')
plt.xlabel('Investimento %')
plt.ylabel('Quantidade de analfabetos %')
plt.legend()
plt.savefig("graficoanalfa4.png")

# Mostrar o gráfico
plt.show()
