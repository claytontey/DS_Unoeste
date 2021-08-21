# Análise de dados de Diabetes
import os
from numpy.lib.utils import info
import pandas as pd
import numpy as np


# Leitura dos diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'data')


# List Compreension do dataset
file_names = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]

# listando o dataset
for i in file_names:
    df = pd.read_csv(os.path.join(DATA_DIR, i))

# Apresentando as informações do Dataset
#print('\n ************ Informações sobre o Dataset ********** \n')
#print('Diretórios: \n')
#print('Meu diretório do projeto é: ', BASE_DIR)
#print('Meu diretório de dados é: ', DATA_DIR)
#print('Este é o meu Dataset: \n', df.head(5))

# Iniciando o tratamento dos dados. True = 1 and False = 0
map_data = {True: 1, False: 0}
df['diabetes'] = df['diabetes'].map(map_data)
#print('\nAlteração de valores categóricos: \n', df.head(5))

# ******************* Amostras por classe **************************************************
sample0 = np.where(df.loc[df['diabetes'] == 0])
sample1 = np.where(df.loc[df['diabetes'] == 1])


# ******************* Quantidade de amostrar por classe **************************************
vl_paciente = len(df.loc[df['diabetes'] == 1])
vl_controle = len(df.loc[df['diabetes'] == 0])

# ******************* Dados Faltantes **************************************************
dt_feature = df.iloc[:,:-1]
dt_target = df.iloc[:, -1]

def information():
    print('\n ************ Informações sobre o Dataset ********** \n')
    print('Diretórios: \n')
    print('Meu diretório do projeto é: ', BASE_DIR)
    print('Meu diretório de dados é: ', DATA_DIR)
    print('\nAmostras da classe controle: ', vl_controle)
    print('Amostras da classe paciente: ', vl_paciente)
    print('Colunas com valores = 0: \n',(df==0).sum())
    print('O conjunto de dados possui %d linhas e %d colunas para : '%(len(df[:]), len(df.columns)))
    print('   %d pacientes, que correspondem a %.2f%% do conjunto de dados' %(vl_paciente, vl_paciente /(vl_paciente+vl_controle)*100))
    print('   %d controle, que correspondem a %.2f%% do conjunto de dados' %(vl_controle, vl_controle /(vl_controle+vl_paciente)*100))
    print('\n Valores faltantes: ', df.isnull().values.any())


# Chamando as funções
information()




