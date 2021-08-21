# Análise de dados de Diabetes
import os
import pandas as pd

# Leitura dos diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'data')


# List Compreension do dataset
file_names = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]

# listando o dataset
for i in file_names:
    df = pd.read_csv(os.path.join(DATA_DIR, i))

# Apresentando as informações do Dataset
print('\n ************ Informações sobre o Dataset ********** \n')
print('Diretórios: \n')
print('Meu diretório do projeto é: ', BASE_DIR)
print('Meu diretório de dados é: ', DATA_DIR)
print('Este é o meu Dataset: \n', df.head(5))



