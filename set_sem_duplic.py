# set não é indexado
numeros = [1, 2, 2, 3, 3, 3, 4, 5, 5] 
#sem_duplicatas = set(numeros)
#sem_duplicatas = list(sem_duplicatas)
sem_duplicatas = list(set(numeros)) 
#Mesmo resultado, metodos diferentes
print(sem_duplicatas)

#------- outro set

conjunto = set() 
conjunto.add(1) 
conjunto.add(2) 
conjunto.add(3) 
conjunto.update([4, 5, 6]) # adiciona + de um elemento
print(conjunto)
