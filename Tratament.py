import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
path = "./Dados/corona_tested.csv"

Data = pd.read_csv(path)

Data['corona_result'] = Data['corona_result'].replace(['negative'], '0')
Data['corona_result'] = Data['corona_result'].replace(['positive'], '1')
Data['corona_result'] = Data['corona_result'].replace(['other'], '2')
Data['gender'] = Data['gender'].replace(['male'], '0')
Data['gender'] = Data['gender'].replace(['female'], '1')
Data['gender'] = Data['gender'].replace([np.nan], '0')

cols = ['cough', 'fever', 'sore_throat', 'head_ache', 'corona_result', 'gender']
Data_filtered = Data[cols]
Data = Data_filtered[Data_filtered['corona_result'] != "2" ]
Data.to_csv('./Dados/AllData.csv', index = False)
#print(Data_filtered)

colsSimptoms = ['cough', 'fever', 'sore_throat', 'head_ache', 'gender']
colsResult = ['corona_result']

Data_N = Data_filtered[Data_filtered['corona_result'] == "0" ]
Data_Simptoms_N = Data_N[colsSimptoms]
#print(Data_Simptoms_N.sample(500))
#Data_Simptoms_N.to_csv('./Dados/Simptoms_N.csv', index = False)


Data_Results_N = Data_N[colsResult]
#Data_Results_N.to_csv('./Dados/Results_N.csv', index = False)

Data_S = Data_filtered[Data_filtered['corona_result'] == "1" ]
Data_Simptoms_S = Data_S[colsSimptoms]
#Data_Simptoms_S.to_csv('./Dados/Simptoms_S.csv', index = False)
Data_Results_S = Data_S[colsResult]
#Data_Results_S.to_csv('./Dados/Results_S.csv', index = False)
