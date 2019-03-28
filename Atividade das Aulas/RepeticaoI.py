
#Exercicios da aula 13
#By: Danniel Cristie..

'''
 #Questão 1
print('\t\tQuestão 01\n\tLeia 10 números e informe o maior.')
cont = 0
maior = 0
while(cont < 10):
	cont+=1
	num = int(input('Digite o numero %i: '%cont))
	if num >maior:
		maior = num
print('O maior numero é %i' %maior)	
'''
'''
 #Questão 2
print('\t\tQuestão 02\n\tImprima os múltiplos positivos de 7 e inferiores a 1000.')
cont = 0
while(cont<=1000):
	cont+=7
	print(cont)
	
'''
'''
 #Questão 3
print('\t\tQuestão 03\n\tMostre os números ímpares entre 1 e 100.')
cont = -1
while(cont<100):
	cont+=2
	print(cont)

'''	


# Mesmos exercicios com o laço de repetição FOR
'''
 #Questão 1
print('\t\tQuestão 01\n\tLeia 10 números e informe o maior.')
maior = 0
for cont in range(1,11,1):
	num = int(input('Digite o numero %i: ' %cont))
	if num > maior:
		maior = num
print('\tO maior numero é %i'%maior)
	
'''

'''

 #Questão 2
print('\t\tQuestão 02\n\tImprima os múltiplos positivos de 7 e inferiores a 1000.')

for i in range(0,1000,7):
	print(i)

'''

'''
 #Questão 3
print('\t\tQuestão 03\n\tMostre os números ímpares entre 1 e 100.')

for i in range(1,100,2):
	print(i)

'''




