import sqlite3
import time
import datetime

con = sqlite3.connect('Carteira.db')

def restart():
    print('REINICIANDO...')
    print('--------------')
    programa()

def fim():
    fim = str(input('DESEJA REALIZAR OUTRA OPERAÇÂO? (s/n) '))
    if fim == 's' or fim == 'S':
        programa()
    else:
        con.close()
        exit()

def update_table_valor(valor, mod):
    print('--------------')
    for linha in con.cursor().execute('''SELECT * FROM moviment WHERE cod = (SELECT MAX(cod) FROM moviment)'''):
        lista = linha
    return lista

def update_table_rec(rec, mod):
    print('--------------')
    for linha in con.cursor().execute('''SELECT * FROM moviment WHERE cod = (SELECT MAX(cod) FROM moviment)'''):
        lista = linha
    return lista

def update_table_consul(mod):
    print('--------------')
    for linha in con.cursor().execute('''SELECT * FROM moviment WHERE cod = (SELECT MAX(cod) FROM moviment WHERE mod = {})'''.format(mod)):
        lista = linha
    return lista

def update_table_filter():
    for linha in con.cursor().execute('''SELECT cred FROM moviment WHERE cod = (SELECT MAX(cod) FROM moviment WHERE mod = {})'''.format(mod)):
        lista = linha
    return lista

def consul_table_filter():
    for linha in con.cursor().execute('''SELECT valor FROM moviment WHERE cod = (SELECT MAX(cod) FROM moviment WHERE mod = 1)'''):
        lista = linha
    return lista

def format_number(valor,mod):
    valor = valor.replace(',','.')
    valor = float(valor)
    if mod == 1:
        valor = valor/2
    valor = round(valor,2)
    return valor

def validacao_valor(valor, mod):
    val = str(input('FOI DESCONTADO R${} DA SUA CARTEIRA?(s/n) '.format(valor)))
    if val == 's' or val == 'S':
        lista_valor = list(update_table_valor(valor, mod))
        cod = lista_valor[0]
        cred =lista_valor[3]
        cod = cod + 1
        cred = cred - valor
        if cred < 3.10 and cred >= 1.55:
            print('ATENÇÃO!!!! VOCÊ SÓ TEM MAIS UMA PASSAGEM! (integrado)')
        elif cred < 1.55:
            print('ATENÇÃO!!!! VOCÊ NÃO TEM PASSAGEM! (integrado)')
            if cred >= 1.35:
                print('VOCÊ TEM UMA PASSAGEM! (não-integrado)')
            else:
                print('VOCÊ NÃO TEM PASSAGEM ALGUMA!')
        date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d-%m-%Y %H:%M:%S'))
        print('INSERINDO DADOS...')
        con.cursor().execute('INSERT INTO moviment (cod, mod, valor, cred, date) VALUES (?,?,?,?,?)',(cod, mod, valor, cred, date))
        con.commit()
        print('DADOS ATUALIZADOS!')
        fim()
        
    else:
        restart()

def validacao_rec(rec, mod):
    val = str(input('FOI RECARREGADO R${} NA SUA CARTEIRA?(s/n) '.format(rec)))
    if val == 's' or val == 'S':
        lista_rec = list(update_table_rec(rec, mod))
        cod = lista_rec[0]
        cred = lista_rec[3]
        cod = cod + 1
        cred = cred + rec
        date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d-%m-%Y %H:%M:%S'))
        print('INSERINDO DADOS...')
        con.cursor().execute('INSERT INTO moviment (cod, mod, valor, cred, date) VALUES (?,?,?,?,?)',(cod, mod, rec, cred, date))
        con.commit()
        print('DADOS ATUALIZADOS!')
        fim()
        
    else:
        restart()

def programa():
    print('----------------')
    print('-MINHA CARTEIRA-')
    print('----------------')
    print('1. USO')
    print('2. RECARGA')
    print('3. CONSULTA')
    menu_1 = str(input('ESCOLHA UMA AÇÂO: '))
    print('--------------')

    if menu_1 == '1':
        mod = 1
        print('USO-DESCONTO')
        print('--------------')
        print('1. INTEGRADO')
        print('2. NÃO-INTEGRADO')
        print('3. OUTRO')
        print('--------------')
        menu_2 = str(input('QUAL TIPO DE TRANSPORTE? '))
        print('--------------')

        if menu_2 == '1':
            valor = 1.55
            saldo = list(update_table_filter())
            saldo = saldo[0]
            if valor<=saldo:
                validacao_valor(valor, mod)
            else:
                print('VOCÊ NÃO TEM CRÉDITOS SUFICIENTES!')
                fim()
        elif menu_2 == '2':
            valor = 1.35
            saldo = list(update_table_filter())
            saldo = saldo[0]
            if valor<=saldo:
                validacao_valor(valor, mod)
            else:
                print('VOCÊ NÃO TEM CRÉDITOS SUFICIENTES!')
                fim()
        elif menu_2 == '3':
            valor = str(input('QUAL VALOR DA INTEIRA? R$'))
            valor = format_number(valor, mod)
            saldo = list(update_table_filter())
            saldo = saldo[0]
            if valor<=saldo:
                validacao_valor(valor, mod)
            else:
                print('VOCÊ NÃO TEM CRÉDITOS SUFICIENTES!')
                fim()
        else:
            print('COMANDO INVALIDO')
            restart()

    elif menu_1 == '2':
        mod = 2
        print('RECARGA-ACRÉSCIMO')
        print('--------------')
        print('1. R$10')
        print('2. R$15')
        print('3. R$20')
        print('4. R$25')
        print('5. OUTRO VALOR')
        print('--------------')
        menu_3 = str(input('QUAL VALOR DA RECARGA? '))
        print('--------------')

        if menu_3 == '1':
            rec = 10
            validacao_rec(rec, mod)
        elif menu_3 == '2':
            rec = 15
            validacao_rec(rec, mod)
        elif menu_3 == '3':
            rec = 20
            validacao_rec(rec, mod)
        elif menu_3 == '4':
            rec = 25
            validacao_rec(rec, mod)
        elif menu_3 == '5':
            valor = str(input('ESCREVA O VALOR: R$'))
            rec = format_number(valor, mod)
            validacao_rec(rec, mod) 
        else:
            print('COMANDO INVALIDO')
            restart()

    elif menu_1 == '3':
        print('CONSULTA')
        print('--------------')
        list_filter = list(consul_table_filter())
        valor = list_filter[0]
                                      
        if valor == 0:
            print('FAÇA UMA RECARGA E USE A CARTEIRA PARA TER UM HISTÓRICO!')
            fim()
        else:
            mod = 1
            consul_uso = list(update_table_consul(mod))
            mod = 2
            consul_rec = list(update_table_consul(mod))
            cod_uso = consul_uso[0]
            ult_valor = consul_uso[2] #ultima valorifa paga
            saldo_uso = consul_uso[3]
            valor_date = consul_uso[4] #data da ultima valorifa paga
            cod_rec = consul_rec[0]
            rec_valor = consul_rec[2] #valor da ultima recarga
            saldo_rec = consul_rec[3] #saldo da carteira
            rec_date = consul_rec[4] #data da ultima recarga
            if cod_uso > cod_rec:
                saldo = saldo_uso
                if ult_valor == 1.55:
                    bus = 'Integrada'
                elif ult_valor == 1.35:
                    bus = 'Não-Integrada'
                else:
                    bus = 'Não especificada'                
            elif cod_uso < cod_rec:
                saldo = saldo_rec
                if ult_valor == 1.55:
                    bus = 'Integrada'
                elif ult_valor == 1.35:
                    bus = 'Não-Integrada'
                else:
                    bus = 'Não especificada'
                    
            print ('SUA ULTIMA VIAGEM FOI EM {}, UMA LINHA {} NO VALOR DE R${}.'.format(valor_date, bus, ult_valor))
            print ('SUA ÚLTIMA RECARGA FOI EM {}, NO VALOR DE R${}, SEU SALDO É R${}.'.format(rec_date, rec_valor, saldo))
            print('--------------')
            fim()
        
    else:
        print('COMANDO INVALIDO')
        restart()

programa()
