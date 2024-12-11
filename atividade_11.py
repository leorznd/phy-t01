

frutas = ['uva', 'maçã', 'kiwi', 'caju', 'banana' ]
print(frutas)

print('Primeira: ', frutas[0])
print('Ultima: ', frutas[-1])


frutas.extend(['abacaxi', 'manga', 'caqui'])


print(frutas)

del frutas [1]
print(frutas)
print(frutas.count('banana'))
frutas.sort()
print(frutas)