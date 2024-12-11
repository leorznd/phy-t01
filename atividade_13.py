contatos = { 'leonardo' : ['7777-7777'],
             'vinicius' : ['5555-5555'],
             'izabela' :  ['9999-9999'],
}
contatos.update({'joao' : ['1111-1111']})
print(contatos)

del contatos ['izabela']
print(contatos)

contatos.update({'leonardo' : ['7777-0000']})
print(contatos)

print(contatos.keys())