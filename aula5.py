                                                                                    # # a = 10 ---> atribuicao de valor, variavel.
                                                                                    # # a == 10 ---> igualdade, dado em true or false
                                                                                    #
                                                                                    # # igual a: ==
                                                                                    #
                                                                                    # print(10==2)
                                                                                    # print(2==2)
                                                                                    # print(2==2.0)
                                                                                    # print(2=='2')
                                                                                    #
                                                                                    # # Diferente de: !=
                                                                                    # print(10 != 2)
                                                                                    # print(2 != 2)
                                                                                    # print(10 != 2)
                                                                                    # print(1000 != 100*10)
                                                                                    # print(100 != int('100'))
                                                                                    #
                                                                                    # # Maior que: >
                                                                                    # print(10>2)
                                                                                    # print(0>2)
                                                                                    # # print('100' > 10) da erro no programa se fizer assim
                                                                                    # print('senha123' > '123')
                                                                                    #
                                                                                    # # Menor que:
                                                                                    # print(10 < 2)
                                                                                    # print(10 < 2 + 9)
                                                                                    # print('palavra pequena' < 'palavra grande')
                                                                                 #
                                                                                    # # Maior ou igual:
                                                                                    # print(10 >= 2)
                                                                                    # print(2 >= 2)
                                                                                    #
                                                                                    # #Menor ou igual
                                                                                    # print(10 <= 12)
                                                                                    # print(100 <= 12)
                                                                                    #
                                                                                    # #OPERADORES LÓGICOS
                                                                                    #
                                                                                    # #and:
                                                                                    # condicao_1 = 10 > 0
                                                                                    # condicao_2 = 2 == 2
                                                                                    # print(condicao_1 and condicao_2)
                                                                                    #
                                                                                    # autentic_user = True
                                                                                    # autentic_password = True
                                                                                    # libera_user = autentic_user and autentic_password
                                                                                    # print(libera_user)
                                                                                    #
                                                                                    # #or:
                                                                                    # dinheiro = False
                                                                                    # cartao = True
                                                                                    # pagamento = dinheiro or cartao
                                                                                    # print(pagamento)
                                                                                    #
                                                                                    # print(5 > 2 or 3 <=2)
                                                                                    #
                                                                                    # #not
                                                                                    #
                                                                                    # print(not True)
                                                                                    # print(not False)
                                                                                    #
                                                                                    # caixa_cheia = True
                                                                                    # encher_caixa =  not caixa_cheia
                                                                                    # print(encher_caixa)

                                                                                    # print(not 10 > 5 and 20 % 2 == 0 or 8 >= 4)

# codigo_produto = input('Informe o código do produto: ').upper()
#
# quantidade_minima = 1000
#
# quantidade_maxima = 2500
#
#                                                                                             # print(quantidade_estoque < quantidade_minima)
# if codigo_produto == 'LED20':
#     quantidade_estoque = int(input(f'Informe a quantidade de {codigo_produto} em estoque: '))
#     if quantidade_estoque < quantidade_minima:
#         print(f'Compre {quantidade_minima - quantidade_estoque} unidades do produto {codigo_produto}. ')
#
#     elif quantidade_estoque > quantidade_maxima:
#         unidades_venda = quantidade_estoque - quantidade_maxima
#         print(f'Venda {unidades_venda} unidades de {codigo_produto}.')
#
#     else:
#         print(f'Não há necessidade de compra do produto {codigo_produto}.')
# else:
#     print(f'{codigo_produto} não existe em nosso sistema')

#######################################################################################

# sol = True
# calor = True
# 
# if sol and calor:
#     print('Bora para praia!')
# elif sol and not calor:
#     print('Bora para o parque!')
# elif not sol and calor:
#     print('Bora para a piscina!')
# elif not sol and not calor:
#     print('off')
#
# #######################################################################################
#
# ano = input('Entre com o ano: ')
#
# if int(ano[-2:]) % 4 == 0:
#     print(f'O ano de {ano} é bissexto.')
# else:
#     print(f'O ano de {ano} não é bissexto.')
#
# #######################################################################################
#
# tempo_prova = float(input('Entre com o tempo (em segundos) na prova dos 100 metros livres: '))
#
# if tempo_prova < 75:
#     print('Classificatórias Estaduais.')
# elif 75 < tempo_prova <= 85:
#     print('Repescagem, prova na proxima semana')
# else:
#     print('Obrigado pela participação, infelizmente você não avança com esse tempo. Boa sorte na próxima.')
#
# ##########################################################################################