palavra = str(input('digite:  ') )
cont  = 0
for c in palavra:
    if c == 'a' or c=='e' or c=='i' or c=='o' or c=='u' :
        cont = cont + 1
print(cont)
