fruta =input('digite uma palavra:  ')
cont = 0
for caracter in fruta:
      if caracter == 'a':
        cont+=1    
if cont <0:
    print('tem e na palavra')
else:
    print ('nao tem e na palavra')
