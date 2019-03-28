pasta='C:\\Users\\Aluno\\Documents\\Danniel\\'
arquivo = 'test.txt'
endereco = pasta+arquivo
arq = open (endereco,'w')
print  ('Danniel', file=arq)

arq.close()
