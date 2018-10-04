# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 23:51:43 2018

@author: bruno
"""

import json



comanda = {}
cardapio = {}


try:
    with open('cardapio.txt', 'r') as cardapio:
     cardapio = json.loads(cardapio.read())
    with open('comanda.txt', 'r') as comanda:
     comanda = json.loads(comanda.read())
except: FileNotFoundError

menu = True
while menu:
    print('Comanda eletrônica')
    
    print('0 - sair')
    
    print('1 – Cadápio')
    
    print('2 - Comanda')
    
    escolha_1= input('Qual a sua escolha: ')
#    while escolha_1 != '0' or escolha_1 != '1' or escolha_1 != '2':
#        print ('comando invalido')
#        print()
#        print('Comanda eletrônica') 
#        print('0 - sair')    
#        print('1 – Cadápio')    
#        print('2 - Comanda')
#        escolha_1= input('Qual a sua escolha: ')
        
    mexer_no_menu = True
    while mexer_no_menu:
        if escolha_1=='0':
            print('\nAté mais !')
            menu = False
            break        
        if escolha_1=='1':
            print('0 - Voltar')
            print('1 - Imprimir Cardápio')
            print('2 - Adicionar item ao cardápio')
            print('3 - Remover item do cardápio')
            print('4 - Alterar preço de algum item')
            
            escolha_11 = input('Qual a sua ecolha: ')
            
#            while escolha_11!= '0' or escolha_11 != '1' or escolha_11 != '2' or escolha_11 != '3' or escolha_11 != '4':
#                print('comando invalido')
#                print()
#                print('0 - Voltar')
#               print('1 - Imprimir Cardápio')
#                print('2 - Adicionar item ao cardápio')
#                print('3 - Remover item do cardápio')
#                print('4 - Alterar preço de algum item')
#                escolha_11 = input('Qual a sua ecolha: ')
                
            while True:
                if escolha_11=='0':
                    mexer_no_menu = False
                    break
                if escolha_11=='1':
                    print('\nCardápio:')
                    if len(cardapio)==0:
                        print('\nNão há nada no cardápio!\nAdicione algum produto')
                        break
                    else:
                        for produto,preco in cardapio.items():
                            print('{0} (R${1:.2f})'.format(produto, preco))
                        break
                if escolha_11=='2':
                    NomeProduto = input('\nNome do produto: ')
                    PrecoProduto = float(input('Preço do produto: '))
                    while PrecoProduto < 0:
                        print('o preco nao pode ser negativo')
                        PrecoProduto = float(input('Preço do produto: '))
                    cardapio[NomeProduto]=PrecoProduto
                    print('\nNovo item adicionado ao cardápio:\n{0} (R${1:.2f})'.format(NomeProduto, cardapio[NomeProduto]))
                    break
                if escolha_11=='3':
                    NomeProduto = input('\nNome do produto que será removido: ')
                    if NomeProduto not in cardapio:
                        print('\nEste produto não está no cardápio')
                        break
                    else:
                        cardapio.pop(NomeProduto)
                        if len(cardapio)!=0:
                            print("\n'{0}' foi removido do cardápio".format(NomeProduto))
                            break
                        else:
                            print('\nCardápio vazio.\nAdicione algum produto')
                            break
                if escolha_11=='4':
                    NomeProduto = input('\nNome do produto: ')
                    if NomeProduto not in cardapio:
                        print('\nProduto não encontrado no cardápio')
                        break
                    else:
                        preco = float(input('\nNovo preço do produto: '))
                        cardapio[NomeProduto]=preco
                        print("\n'{0}' Novo preço: R${1:.2f}".format(NomeProduto, cardapio[NomeProduto]))
                        break
        if escolha_1=='2':
            if len(cardapio)==0:
                print('\nNão há nada no cardapio.\nAdicione algum produto para utilizar a comanda')
                break
            else:
                x = int(input("Qual a mesa:"))
                while x > 0 :
                    print('0 - Voltar')
                    print('1 - Adicionar item à comanda')
                    print('2 - Remover item da comanda')
                    print('3 - Imprimir comanda')
                    escolha_12 = input('Faça sua escolha: ')
                    if escolha_12 == '0':
                        break
                    if escolha_12 == '1':
                        NomeProduto = input('\nProduto à adicionar: ')
                        if NomeProduto not in cardapio:
                            print('\nItem não encontrado no cardápio')
'''
while escolha !='0':

    if escolha=='4' or escolha=='2' or escolha=='3':

        item = input('nome da loja:')

        if escolha == '2':

            if item in cardapio:

                print ('esta loja ja existe')

            else:

                cardapio[item]={}

                print (item,'foi adicionada')

        elif escolha == '3':

            if item not in cardapio:

                print('este item nao pode ser deletada... pois ele ja nao existe! ;)')

            else:

                del cardapio[item]

                print ('{} foi deletado com sucesso'.format(item))            

        while escolha == '4':

            if item not in cardapio:

                print('esta loja nao existe ,digite o nome correto da loja, ou "0" para sair.')

                nome_loja=input('em qual loja gostaria de entrar? ')
                
                if nome_loja == '0':
                    escolha = '0'
                else:
                    nome_loja=nome_loja

            else:

                print('Controle da loja ')

                print('0 - sair da loja ', nome_loja)

                print('1 - adicionar item')

                print('2 - remover item')

                print('3 - editar produto')

                print('4 - ver estoque')

                dloja=int(input('o que deseja fazer? '))

                if dloja == 0 :

                    escolha = '0'

                elif dloja== 1 or dloja== 2 or dloja== 3:

                    item = input ('qual o nome do produto? ')

                    if dloja == 1:

                        if item in lojas[nome_loja]:

                            print ('ja existe um item com este nome na loja ',nome_loja)

                        else:

                            lojas[nome_loja][item]={}

                            preco= float(input('qual o preco do produto?  '))

                            if preco < 0:

                                print ('o preco deve ser positivo')

                            else:

                                lojas[nome_loja][item]['preco']=preco

                                quantidade=int(input('qual a quantidade do novo produto?  '))

                                if quantidade<0:

                                    print('a quantidade deve ser positiva')

                                else:
                                

                                    lojas[nome_loja][item]['quantidade']=quantidade

                    elif dloja == 2:

                        if item not in lojas:

                            print ('este item nao existe no estoque')

                        else:

                            del lojas[nome_loja][item]

                    elif dloja==3:
                        
                        if item in lojas[nome_loja]:
                        
                            novo_preco=float( input('qual vais ser o novo preco do produto? '))
    
                            lojas[nome_loja][item]['preco']=novo_preco
 
                            nova_quantidade=int(input ('qual a quantidade que deseja adicionar ou subtrair?'))
 
                            x=lojas[nome_loja][item]['quantidade']

                            y=x+nova_quantidade

                            lojas[nome_loja][item]['quantidade']=y
                        
                        else:
                            print ("este produto nao existe")

                elif dloja==4:

                    faltando={}

                    m_total=0

                    for w in lojas[nome_loja]:

                        print ('{0}: quantidade={1}  preco=R${2}'.format(w,lojas[nome_loja][w]['quantidade'],lojas[nome_loja][w]['preco']))

                        if lojas[nome_loja][w]['quantidade'] < 0:

                            faltando[w]= lojas[nome_loja][w]['quantidade']

                        else:

                            x=w

                    for w in  faltando:

                        print('!!!!a quantidade de {0} no estoque e {1}!!!!'.format(w,faltando[w]))

                    for e in lojas[nome_loja]:

                        unitario=lojas[nome_loja][e]['preco']*lojas[nome_loja][e]['quantidade']

                        m_total += unitario

                    print('o valor monetario total do estoque e: ',m_total)

            

               

                else:

                    print ('este comando nao e valido')

    elif escolha == '1':

        for e in lojas:

            print(e)

    else:

        print('comando invalido')

    print('Controle de lojas')

    print('0 - sair')

    print('1 - adicionar loja')

    print('2 - remover loja')

    print('3 - entrar em uma loja')

    print('4 - ver lojas')

    

    escolha= input('o que mais voce deseja fazer:') 

    

    



print ('ate mais!!!')  



with open('backup1.txt', 'w') as arquivo:

    data = json.dumps(lojas, sort_keys=True, indent=4)

    arquivo.write(data)
'''
