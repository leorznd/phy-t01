# # minha_lista = []
# # print(minha_lista)
# # print(type(minha_lista))
#
# # minha_lista =[10, 1.4, 'OI', True]
# #  for elemento in minha_lista:
# #      print(elemento)
# #
# # numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # # indice
# # print(numeros)
# # print(numeros[0])
# # print(numeros[5])
# # print(numeros[-1])
# #
# # # slicing
# # print(numeros[::-1])
# # print(numeros[2:8])
# # print(numeros[2:8:2])
# #
# frutas = ['laranja', 'uva']
#
# # metodos para inserção de elementos na lista
#
# nova_fruta = 'melancia'
#
# frutas.append(nova_fruta)
# print(frutas)
#
# # add mais itens por vez
#
# frutas.extend(['banana', 'maçã'])
# print(frutas)
#
# # print(frutas.count('uva'))
#
# for frutas in frutas
#     # print('f'{frutas.count(frutas)})` {frutas}  !!!!!!!  R E C O P I A R  !!!!!!!!!
#
# ultima_fruta = frutas.pop()
# print(ultima_fruta)
# print(frutas)
#
# frutas.remove('melancia')
# print(frutas)
# del frutas [2]
# print(frutas)
#
# frutas.sort()
# print(frutas)
# from traceback import format_list




                                                  # tuplas:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(numeros))
# print(max(numeros))
# print(min(numeros))
#
# minha_tupla = (1, 2, 3, 4, 5)
# print(minha_tupla)
# print(type(minha_tupla))
# print(len(minha_tupla))
#
# for i in minha_tupla:
#     print(i)
#
# print(sum(minha_tupla))
# print(max(minha_tupla))
# print(min(minha_tupla))
#
#
#
# lista_alunos = ['Joao', 'Maria', 'ana', 'davi']
# notas_alunos = [5, 7, 10, 9]
#
# print(list(enumerate(lista_alunos)))
#
# for posicao, nome in enumerate(lista_alunos):
#     if nome == 'Joao':
#         notas_alunos[posicao] = 7.5
#         print(notas_alunos)
#

#                                            DICIONARIOS:

meu_dicionario = {'a' : 1, 'b' : 2, 'c': 3}

print(type(meu_dicionario))
print(meu_dicionario['a'])

meu_dicionario['d'] = 4
print(meu_dicionario)
meu_dicionario['b'] = 5
print(meu_dicionario)
meu_dicionario.update({'e': 6,'f':7, 'g':8})
print(meu_dicionario)

print(meu_dicionario.items())
print(meu_dicionario.keys())
print(meu_dicionario.values())

for chave, valor in meu_dicionario.items():
    print(chave + '----' + str(valor))
print(sum(meu_dicionario.values()))

















