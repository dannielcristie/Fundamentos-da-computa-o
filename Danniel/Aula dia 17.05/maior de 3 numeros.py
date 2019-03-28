n1 = float(input( 'Digite o primeiro numero : '))
n2 = float(input( 'Digite o segundo numero : '))
n3 = float(input( 'Digite o terceiro numero : '))
if (n1>n2) and (n1>n3):
    print(  n1, 'E o  maior' )
elif (n1==n2):
    print (n1, 'e ', n2, 'iguas')
elif (n2>n1) and (n2>n3):
    print( n2, ' E o maior')
elif(n2==n1):
    print (n2, 'e ', n1, 'iguas')
elif(n3>n1) and (n3>n2):
    print( n3, 'E o maior')
elif(n3==n1):
    print(n3, 'e ', n1, 'iguas')
else:
    print( 'Numeros iguais')


