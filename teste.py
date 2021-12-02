import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

TamTeste = 50

path_Simptoms_S = "./Dados/Simptoms_S.csv"
Data_Simptoms_S = pd.read_csv(path_Simptoms_S)
path_Results_S = "./Dados/Results_S.csv"
Data_Results_S = pd.read_csv(path_Results_S)
path_Simptoms_N = "./Dados/Simptoms_N.csv"
Data_Simptoms_N = pd.read_csv(path_Simptoms_N)
path_Results_N = "./Dados/Results_N.csv"
Data_Results_N = pd.read_csv(path_Results_N)
path_AllData = "./Dados/AllData.csv"
Data = pd.read_csv(path_AllData)

'''
DICIONARIO DE COLUNAS

Para a tabela de AllData teremos:

|   TOSSE   |   FEBRE   |   DOR DE GARGANTA |   DOR DE CABECA   |   GENERO  |   TESTE DE COVID  |
|   0 ou 1  |   0 ou 1  |       0 ou 1      |       0 ou 1      |   0 ou 1  |       0 ou 1      |


Para a tabela de Simptoms teremos:

|   TOSSE   |   FEBRE   |   DOR DE GARGANTA |   DOR DE CABECA   |   GENERO  |
|   0 ou 1  |   0 ou 1  |       0 ou 1      |       0 ou 1      |   0 ou 1  |


Para a tabela de Results teremos: 

|   TESTE DE COVID  |
|       0 ou 1      |

'''

print("=================================================")
print("                 TAMANHO TESTE                   ")
print("=================================================")
print(TamTeste)
print("=================================================")


teste = Data.sample(TamTeste)
#print(teste)

teste_x = teste[["cough", "fever", "sore_throat", "head_ache", "gender"]]
teste_y = teste[["corona_result"]]