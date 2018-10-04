# -*- coding: utf-8 -*-

"""

Created on Mon Sep 24 15:27:59 2018



@author: felip

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
    mexer_no_menu = True
    while mexer_no_menu:
        if escolha_1=='0':
            print('\nAté mais !')
            menu = False
            break        
        elif escolha_1=='1':
            print('0 - Voltar')
            print('1 - Imprimir Cardápio')
            print('2 - Adicionar item ao cardápio')
            print('3 - Remover item do cardápio')
            print('4 - Alterar preço de algum item')
            
            escolha_11 = input('Qual a sua ecolha: ')
            while True:
                if escolha_11=='0':
                    mexer_no_menu = False
                    break
                elif escolha_11=='1':
                    print('\nCardápio:')
                    if len(cardapio)==0:
                        print('\nNão há nada no cardápio!\nAdicione algum produto')
                        break
                    else:
                        for produto,preco in cardapio.items():
                            print('{0} (R${1:.2f})'.format(produto, preco))
                        break
                elif escolha_11=='2':
                    NomeProduto = input('\nNome do produto: ')
                    PrecoProduto = float(input('Preço do produto: '))
                    cardapio[NomeProduto]=PrecoProduto
                    print('\nNovo item adicionado ao cardápio:\n{0} (R${1:.2f})'.format(NomeProduto, cardapio[NomeProduto]))
                    break
                elif escolha_11=='3':
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
                elif escolha_11=='4':
                    NomeProduto = input('\nNome do produto: ')
                    if NomeProduto not in cardapio:
                        print('\nProduto não encontrado no cardápio')
                        break
                    else:
                        preco = float(input('\nNovo preço do produto: '))
                        cardapio[NomeProduto]=preco
                        print("\n'{0}' Novo preço: R${1:.2f}".format(NomeProduto, cardapio[NomeProduto]))
                        break
        elif escolha_1=='2':
            if len(cardapio)==0:
                print('\nNão existe nenhum item no cardapio.\nAdicione algum produto ao cardápio para utilizar a comanda')
                break
            else:
                m = int(input("Qual a mesa:"))
                while m > 0 :
                    print('0-Voltar')
                    print('1-Adicionar item na comanda')
                    print('2-Remover algum item da comanda')
                    print('3-Imprimir comanda')
                    escolha_12 == input('Qual a sua escolha: ')
                    if escolha_12 == '0':
                        break
                    elif escolha_12 == '1':
                        NomeProduto = input('n\Produto a ser adicionado: ')
                        if Nomeproduto not in cardapio:
                            print('n\Item não encontrado no cardápio')
                        else:
                            while True:
                                QuantidadeProduto = int(input('n\Quantidade deste produto a ser adicionada: '))
                                if QuantidadeProduto < 0:
                                    print('n\A quantidade adicionada não pode ser negativa: ')
                                else:
                                    if NomeProduto in comanda:
                                        comanda[NomeProduto] += QuantidadeProduto
                                        print('n\A quantidade atual é de {0}: {1}'.format(NomeProduto, int(comanda[NomeProduto])))
                                        break
                                    else:
                                        comanda[NomeProduto] = QuantidadeProduto
                                        print('n\A quantidade atual é de {0}: {1}'.format(NomeProduto, int(QuantidadeProduto)))
                                        break
                    elif escolha_12 == '2':
                        NomeProduto = input('n\Produto à ser removido: ')
                        if NomeProduto not in comanda:
                            print("\nO item '{0}' não está na comanda".format(NomeProduto))
                        else:
                            removeq = True
                            while removeq:         
                                while True:
                                    QuantidadeProduto = int(input('\nQuantidade a ser removida: '))
                                    if QuantidadeProduto < 0:
                                        print("\nA quantidade a ser removida não pode ser negativa")
                                        break
                                    elif QuantidadeProduto >comanda[NomeProduto]:
                                        print('\nNão é possivel remover mais do que há na comanda')
                                        break
                                    else:
                                        comanda[NomeProduto] -= QuantidadeProduto
                                        if comanda[NomeProduto]==0:
                                            print('\nA quantidade atual é de {0}: {1}'.format(NomeProduto, int(comanda[NomeProduto])))
                                            print("\nRemovendo da comanda...".format(NomeProduto))
                                            comanda.pop(NomeProduto)
                                            removeq = False
                                            break
                                        else:
                                            print('\nA quantidade atual é de {0}: {1}'.format(NomeProduto, int(comanda[NomeProduto])))
                                            removeq = False
                                            break
                    elif escolha_12=='3':
                            if len(comanda)==0:
                                print('\nNão há nada na comanda')
                            else: 
                                SomaTot = 0
                                print('n\Comanda'.upper())
                                for chave, valor in comanda.items():
                                    soma = valor*cardapio[chave]
                                    print("\n'{0}': {1}\n   Preço Unitário: R${2:.2f}\n   Preço total: R${3:.2f}".format(chave, int(valor), cardapio[chave],soma))
                                    SomaTot+=soma
                                dezporcento = SomaTot+(0.1*Somatot)
                                print('\nTOTAL: R${0:.2f}\nTOTAl Com os 10%: R${1:.2f}'.format(Somatot,dezporcento))
update_1 = json.dumps(cardapio, sort_keys = True)
with open('cardapio.txt','w') as cardapio: 
    cardapio.write(update_1)
update_2 = json.dumps(comanda, sort_keys = True) 
with open('comanda.txt','w') as comanda: 
    comanda.write(update_2)
                                    
                                                