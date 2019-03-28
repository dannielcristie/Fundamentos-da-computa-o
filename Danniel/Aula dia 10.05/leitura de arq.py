pasta='C:\\Users\\Aluno\\Documents\\Danniel\\' 
arquivo = 'test.txt'
endereco = pasta+arquivo
arq = open (endereco,'r')

valor = arq.readlines()
print(valor)




'''
valor = arq.read()
print(valor)
valor = arq.read()
print(valor)
'''

#valor = arq.readline()
#valor = arq.readlines()
#print(valor)
'''
for linha in arq:
    print(linha)
'''
