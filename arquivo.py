import pandas as pd #analisar os dados de arquivos


#passo 4 - calcular os indicadores(faturamento e a quantidade de produtos)

######## tabela
tabela = pd.read_excel(r'C:\Users\Estudo - Workshop\Downloads\Vendas - Dez.xlsx')
faturamento = tabela['Valor Final'].sum()
qtd_produtos = tabela['Quantidade'].sum()
print(faturamento)
print(qtd_produtos)