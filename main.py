from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score as AS
from treino import *
from teste import *


modelo = LinearSVC()
modelo.fit(treino_x, treino_y)


resp = modelo.predict(teste_x)


#print(resp)
for i in resp: 
    if(i == 1):
        print("COVID")
    else:
        print("SEM COVID")

print(AS(teste_y, resp))

