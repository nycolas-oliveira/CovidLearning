from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score as AS
print("*************************************************")
print("                INICIANDO INPUTS                 ")
print("*************************************************")
from treino import *
from teste import *


modelo = LinearSVC()
modelo.fit(treino_x, treino_y)


print("*************************************************")
print("                  INICIANDO ALEX                 ")
print("*************************************************")
print("->Olá, Eu sou Alex!")


resp = modelo.predict(teste_x)
print("->Hum, recebi alguns casos!")
print("->Analizando...")

#print(resp)
cont = 1
for i in resp: 
    if cont < 10:
        visualCont = "0" + str(cont)
    else:
        visualCont = cont
    if(i == 1):
        print(visualCont, " - COVID")
    else:
        print(visualCont, " - SEM COVID")
    cont = cont + 1

print("*************************************************")
print("               CALCULANDO ACERTOS                ")
print("*************************************************")

Percentual = AS(teste_y, resp)*100

print("->Terminei as predições, com base nos dados de res-")
print("posta acertei ", Percentual, "% dos casos.")

print("*************************************************")
print("                 ENCERRANDO ALEX                 ")
print("*************************************************")