#-*- coding: utf-8 -*-


#importando o pandas
import pandas as pd


#carregando a planilha do excel em um dataFrame do Pandas
df = pd.read_excel('C:/Users/Leo/Desktop/tcc_python/python-RCM/rcmPython.xlsx', sheet_name='GERAL')

#verificando se os dados foram carregados corretamente
df.head()

#selecionando as colunas relevantes para análise
equipamentos = df[['Data', 'Equipamento','Maquina', 'Turno', 'Setor', 'Manutencao', 'Origem', 'Descricao', 'Classificacao', 'Causa', 'Inicio', 'Termino', 'Total', 'Status', 'Servico', 'Maquina Parada']]

