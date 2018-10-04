# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:57:41 2018

@author: bruno
"""

import json



cardapio={}
comanda={}
with open('backup1.txt', 'r') as arquivo:

    cardapio = json.loads(arquivo.read())


print('Comanda eletrônica')
print('0 - sair')
print('1 – imprimir cardápio')
print('2 - adicionar item')
print('3 - remover item')
print('4 - imprimir comanda')
print('5 - modificar cardapio')

escolha= input('Faça sua escolha: ')

while escolha !='0':

    if escolha=='2' or escolha=='3':        
        item=input('qual o nome do item? ')
        
        if escolha == '2':            
            if item not in cardapio:                
                print('O item ', item ,' não está no cardápio')                
            else:                
                quantidade= int(input('qual a quantidade que deseja adicionar? '))                
                while quantidade<=0:                    
                    print('Não é possível adicionar quantidade não positiva')                    
                    quantidade= int(input('qual a quantidade que deseja adicionar? '))                    
                comanda[item]['quantidade']+=quantidade             
                print ('Quantidade atual de',item,':',comanda[item]['quantidade'])
            
       
        elif escolha == '3':            
            if item not in cardapio:               
                print('O item ', item ,' não está no cardápio')               
            else:               
                remover= int(input('qual a quantidade que deseja remover? ')) 
                if comanda[item]['quantidade']==0:
                    print('quantidade de', item ,' e 0. ')
                else: 
                    while remover<=0:                   
                        print('Não é possível remover quantidades não positivas')
                        remover= int(input('qual a quantidade que deseja remover? '))
                    while remover>comanda[item]['quantidade']:
                        print('Não é possível remover mais do que a quantidade presente na comanda')
                        print('a quantidade atual de', item,':',comanda[item]['quantidade'])
                        remover= int(input('qual a quantidade que deseja remover? '))
                    comanda[item]['quantidade']-=remover                
                print ('Quantidade atual de',item,':',comanda[item]['quantidade'])

    elif escolha == '1':
        print('O cardápio possui os seguintes itens:')
        for e in cardapio:
            print(e,cardapio[e]['preco'])
            
    elif escolha == '4':
        for e in cardapio:
            print(e,cardapio[e]['quantidade'])
            
    while escolha == '5':
        print('opcoes do cardapio ')
        print('0 - voltar ')
        print('1 - adicionar item')
        print('2 - remover item')
        print('3 - editar item')
        print('4 - ver cardapio')
        
        escolha_c=int(input('o que deseja fazer? '))
         
        if escolha_c==0:
            escolha='0'
        
        elif escolha_c== 1 or escolha_c== 2 or escolha_c== 3:
            
            item = input ('qual o nome do produto? ')
             
            if escolha_c ==1:
                if item in cardapio:
                    print('ja existe esse item no cardapio')
                else:
                           cardapio[item]={}
                           preco= float(input('qual o preco do item?  '))
                           if preco < 0:
                               print ('o preco deve ser positivo')
                           else:
                               cardapio[item]['preco']=preco
                               quantidade=int(input('qual a quantidade do novo produto?  '))
                               if quantidade<0:
                                   print('a quantidade deve ser positiva')
                               else:        
                                   cardapio[item]['quantidade']=quantidade

            elif escolha_c == 2:
                if item not in cardapio:
                    print ('este item nao existe no cardapio')
                else:
                    del cardapio[item]
            elif escolha_c==3:
                if item in cardapio: 
                    novo_preco=float( input('qual vai ser o novo preco do produto? '))
                    cardapio[item]['preco']=novo_preco
                    nova_quantidade=int(input ('qual a quantidade que deseja adicionar ou subtrair?'))
                    x=cardapio[item]['quantidade']
                    y=x+nova_quantidade
                    cardapio[item]['quantidade']=y   
                else:
                    print ("este produto nao existe")
                     

        
    else:
        print('comando invalido')
    
    print('Comanda eletrônica')
    print('0 - sair')
    print('1 – imprimir cardápio')
    print('2 - adicionar item')
    print('3 - remover item')
    print('4 - imprimir comanda')
    print('5 - modificar cardapio')


    escolha= input('o que mais voce deseja fazer?') 

print ('ate mais!!!')  



with open('backup1.txt', 'w') as arquivo:

    data = json.dumps(cardapio, sort_keys=True, indent=4)

    arquivo.write(data)    