#PROBLEMA DE CLASSIFICAÇÃO BINÁRIA

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

tamTreino = 1000
#from Tratament import Data

path_Simptoms_S = "./Dados/Simptoms_S.csv"
Data_Simptoms_S = pd.read_csv(path_Simptoms_S)
path_Results_S = "./Dados/Results_S.csv"
Data_Results_S = pd.read_csv(path_Results_S)
index_S = Data_Results_S.index
path_Simptoms_N = "./Dados/Simptoms_N.csv"
Data_Simptoms_N = pd.read_csv(path_Simptoms_N)
path_Results_N = "./Dados/Results_N.csv"
Data_Results_N = pd.read_csv(path_Results_N)
index_N = Data_Results_N.index
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



number_of_Index_S = len(index_S)
number_of_Index_N = len(index_N)

print("=================================================")
print("                 QTD POSITIVOS                   ")
print("=================================================")
print(number_of_Index_S)


print("=================================================")
print("                 QTD NEGATIVOS                   ")
print("=================================================")
print(number_of_Index_N)

print("=================================================")
print("                 TAMANHO TREINO                  ")
print("=================================================")
print(tamTreino)


#print(Data_Simptoms_S)

treino = Data.sample(tamTreino)
#print(treino)
#Classificação Com ou Sem Covid
#treino_x = Data_Simptoms_S.iloc[:, [0, 1, 2, 3, 4]].head(500) #+ Data_Simptoms_N.head(500)
#Data_Simptoms_frames = [Data_Simptoms_S, Data_Simptoms_N]
#Data_Simptoms = pd.concat(Data_Simptoms_frames)

#treino_x = Data_Simptoms[["cough", "fever", "sore_throat", "head_ache", "gender"]].sample(500)
treino_x = treino[["cough", "fever", "sore_throat", "head_ache", "gender"]]
#conv_arrx = treino_x.values
#treino_x = conv_arrx
#print(treino_x)
#treino_y = Data_Results_S.iloc[:, 0].head(500) #+ Data_Results_S.head(500)

#Data_Results_frames = [Data_Results_S, Data_Results_N]
#Data_Results = pd.concat(Data_Results_frames)


#treino_y = Data_Results[["corona_result"]].sample(500)
treino_y = treino[["corona_result"]]
#treino_y = treinoLINHAS_y.transpose()

#split matrix into 3 columns each into 1d array
#conv_arr = treino_y.values

#arr1 = np.delete(conv_arr,[1],axis=1) 

#arr1 = arr1.ravel()

#treino_y = arr1
#print(treino_y)


