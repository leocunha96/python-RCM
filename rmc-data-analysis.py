#-*- coding: utf-8 -*-

#importando o pandas, numpy e matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para converter tempo em segundos
def to_seconds(value):
    if isinstance(value, pd.Timestamp):
        return value.total_seconds() / 60.0
    else:
        return value
    
# Função para converter tempo em minutos    
def to_minutes(x):
    if isinstance(x, pd.Timestamp):
        return x.hour*60 + x.minute + x.second/60
    else:
        return x
    
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
#print(machine0, machine1, machine2, machine3,machine4,machine5, machine6)
        
#verificando se há valores nulos em nosso conjunto de dados usando a função isnull(). A função sum() é utilziada para contar o número total de valores nulos em cada coluna.

#print('Todas as maquinas:')
#print(machine0.isnull().sum(),'\n')

#print('Maquina 1:')
#print(machine1.isnull().sum(),'\n')

#print('Maquina 2:')
#print(machine2.isnull().sum(),'\n')

#print('Maquina 3:')
#print(machine3.isnull().sum(),'\n')

#print('Maquina 4:')
#print(machine4.isnull().sum(),'\n')

#print('Maquina 5:')
#print(machine5.isnull().sum(),'\n')

#print('Maquina 6:')
#print(machine6.isnull().sum(),'\n')

#eliminando valores linhas que possuam valores nulos, criando uma copia

machine0_notNull = machine0.copy() #criando uma copia do dataframe para não perder ou sobreescrever os dados
machine0_notNull.dropna(axis=0, inplace=True) # axis=0 indica  remove as linhas e o parâmetro inplace=True modifica o dataframe original machine0.

machine1_notNull = machine1.copy()
machine1_notNull.dropna(axis=0, inplace=True)
#print(machine1_notNull.isnull().sum(),'\n')

machine2_notNull = machine2.copy()
machine2_notNull.dropna(axis=0, inplace=True)
#print(machine2_notNull.isnull().sum(),'\n')

machine3_notNull = machine3.copy()
machine3_notNull.dropna(axis=0, inplace=True)
#print(machine3_notNull.isnull().sum(),'\n')

machine4_notNull = machine4.copy()
machine4_notNull.dropna(axis=0, inplace=True)
#print(machine4_notNull.isnull().sum(),'\n')

machine5_notNull = machine5.copy()
machine5_notNull.dropna(axis=0, inplace=True)
#print(machine5_notNull.isnull().sum(),'\n')

machine6_notNull = machine6.copy()
machine6_notNull.dropna(axis=0, inplace=True)
#print(machine6_notNull.isnull().sum(),'\n')

#usando o método describe() do Pandas para obter algumas informações sobre cada coluna do dataframe em analise.
print(machine0_notNull.describe())

# Converte o tempo total de manutenção em segundos
machine0_notNull['Total'] = machine0_notNull['Total'].apply(to_minutes)
machine1_notNull['Total'] = machine1_notNull['Total'].apply(to_minutes)

# Cria histograma para machine0
machine0_notNull['Total_Minutes'] = machine0_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60) #criar uma nova coluna Total_seconds que contém o tempo total em segundos e plotar o histograma usando essa coluna.
plt.hist(machine0_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine0')
plt.show()

# Cria histograma para machine1
machine1_notNull['Total_Minutes'] = machine1_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60)
plt.hist(machine1_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine1')
plt.show()

# Cria histograma para machine2
machine2_notNull['Total_Minutes'] = machine2_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60)
plt.hist(machine2_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine2')
plt.show()

# Cria histograma para machine3
machine3_notNull['Total_Minutes'] = machine3_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60)
plt.hist(machine3_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine3')
plt.show()

# Cria histograma para machine4
machine4_notNull['Total_Minutes'] = machine4_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60)
plt.hist(machine4_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine4')
plt.show()

# Cria histograma para machine5
machine5_notNull['Total_Minutes'] = machine5_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60)
plt.hist(machine5_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine5')
plt.show()

# Cria histograma para machine6
machine6_notNull['Total_Minutes'] = machine6_notNull['Total'].apply(lambda x: (x.hour*3600 + x.minute*60 + x.second)/60)
plt.hist(machine6_notNull['Total_Minutes'], bins=20)
plt.xlabel('Tempo Total (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma do tempo total de manutenção da machine6')
plt.show()



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
