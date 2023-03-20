#-*- coding: utf-8 -*-

#importando o pandas, numpy e matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#carregando a planilha do excel em um dataFrame do Pandas
dataframe = pd.read_excel('C:/Users/Leo/Desktop/tcc_python/python-RCM/rcmPython.xlsx', sheet_name='GERAL')

#verificando que a tabela foi importada com sucesso
#print(dataframe)
print(f'O DataFrame possui {dataframe.shape[0]} linhas e {dataframe.shape[1]} colunas')

#extraindo informações para saber se temos valores nulos.
#print(dataframe.info())

#criando novos df a partir do dataframe original
dataframe['Maquina'] = dataframe['Maquina'].astype(str) #alterando valor da coluna maquina para string

machine0 = dataframe.query('Maquina == "0"')
machine1 = dataframe.query('Maquina == "1"')
machine2 = dataframe.query('Maquina == "2"')
machine3 = dataframe.query('Maquina == "3"')
machine4 = dataframe.query('Maquina == "4"')
machine5 = dataframe.query('Maquina == "5"')
machine6 = dataframe.query('Maquina == "6"')
print(machine0, machine1, machine2, machine3,machine4,machine5, machine6)
        

                

# crie uma nova coluna com dados de data e hora
#df['DataHora'] = pd.to_datetime(df['Data'].astype(str) + ' ' + df['Total'].astype(str))

'''''''''
#analise rapida dos dados
print(df.head())
print(df.tail())
print(df.describe())

print(df.isna().sum())
print(df['Status'].value_counts())

plt.hist(df['Total'], bins=20)
plt.xlabel('Horas de manutenção')
plt.ylabel('Frequência')
plt.show()

plt.boxplot(df['Total'])
plt.ylabel('Horas de manutenção')
plt.show()''''''
'''#verificando se os dados foram carregados corretamente
'''df.head()
#selecionando as colunas relevantes para análise
tabela = df[['Data', 'Equipamento','Maquina', 'Turno', 'Setor', 'Manutencao', 'Origem', 'Descricao', 'Classificacao', 'Causa', 'Inicio', 'Termino', 'Total', 'Status', 'Servico', 'Maquina Parada']]


#analisando as informações

tabela.describe()'''
