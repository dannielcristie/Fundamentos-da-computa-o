
#Exercicios da aula 12
#By: Danniel Cristie..

'''
 #Questão 1
print('\t\tQuestão 01\n\tDado dois numeros, informe o maior.')

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

if a>b:
  print('o primeiro %d é maior que o segundo %d' %(a,b))
elif a==b:
  print('O primeiro %d é igual ao segundo %d' %(a,b))
else:
  print('o segundo %d é maior que o primeiro %d' %(b,a))
  
''' 
 
'''
  #Questão 2
print('\t\tQuestão 02\n\tLê do usuário 4 números inteiros e informa se há ou não um deles no intervalo entre 1 e 25, outro de 26 a 50, outro de 51 a 75 e um último de 76 a 100.')

a = int (input('Digite um numero: '))
b = int (input('Digite um numero: '))
c = int (input('Digite um numero: '))
d = int (input('Digite um numero: '))

if (1 <= a <= 25):
	print('%d esta entre 1 e 25' %a)
elif(26 <= a <= 50):
	print('%d esta entre 26 e 50' %a)
elif(51 <= a <= 75):
	print('%d esta entre 51 e 75' %a)
elif(51 <= a <= 75):
	print('%d esta entre 51 e 75' %a)
elif(76 <= a <= 100):
	print('%d esta entre 76 e 100' %a)
elif (a > 100):
	print('O numero %d fora do estipulado.'%a)


if (1 <= b <= 25):
	print('%d esta entre 1 e 25' %b)
elif(26 <= b <= 50):
	print('%d esta entre 26 e 50' %b)
elif(51 <= b <= 75):
        print('%d esta entre 51 e 75' %b)
elif(51 <= b <= 75):
        print('%d esta entre 51 e 75' %b)
elif(76 <= b <= 100):
	print('%d esta entre 76 e 100' %b)
elif (b > 100):
	print('O numero %d fora do estipulado.'%b)


if (1 <= c <= 25):
	print('%d esta entre 1 e 25' %c)
elif(26 <= c <= 50):
	print('%d esta entre 26 e 50' %c)
elif(51 <= c <= 75):
        print('%d esta entre 51 e 75' %c)
elif(51 <= c <= 75):
         print('%d esta entre 51 e 75' %c)
elif(76 <= c <= 100):
	print('%d esta entre 76 e 100' %c)
elif (c > 100):
	print('O numero %d fora do estipulado.'%c)



if (1 <= d <= 25):
	print('%d esta entre 1 e 25' %d)
elif(26 <= d <= 50):
	print('%d esta entre 26 e 50' %d)
elif(51 <= a <= 75):
        print('%d esta entre 51 e 75' %d)
elif(51 <= d <= 75):
        print('%d esta entre 51 e 75' %d)
elif(76 <= d <= 100):
	print('%d esta entre 76 e 100' %d)
elif (d > 100):
	print('O numero %d fora do estipulado.'%d)
            
'''

'''

 #Questão 3
print('\t\tQuestão 3\n\tRealiza saques com a menor quantidade de cédulas possíveis de um caixa eletrônico que dispõem apenas de notas de 1, 10 e 100 reais')

v = int(input(' Digite o valor que deseja sacar:  '))

if(1<=v<10):
  print(v,' cedulas de 1 Real')
  
elif(10<= v <100):
  d = v//10
  print(d,' cedulas de 10 reais')
  u = d*10
  un = v-u
  print(un,'cedulas de 1 real')
  
elif(v>=100):
  c = v//100
  print(c, ' cedulas de 100 reias')
  d = c*100
  d1 = v-d
  d2 = d1//10
  print(d2, ' cedulas de 10 reais')
  u = v-((c*100)+(d2*10))
  print(u, 'cedulas de 1 real.')

'''

