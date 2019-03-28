def soma_recursiva (N):
    if (N==1):
        return 1
    else:
        return N*soma_recursiva (N-1)

print (soma_recursiva(950))
