from random import randint
print('Escolhendo um valor aleatorio.')
segredo = randint(1,10)
escolha = -1
while (segredo != escolha):
    print('\nEscolha valor entre 1 a 10. digite 0 para desistir.')
    escolha=int(input())
    if segredo == escolha:
        print ('Parabnes! voce acertou.')
    elif segredo == 0:
        print ('Perdeu.! voce desistiu.')
        break
    else:
        print('Errou tente novamente.')
