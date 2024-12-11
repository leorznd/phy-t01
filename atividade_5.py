aluno = input('insira o nome do aluno: ').title()
n1 = float(input(f'insira a primeira nota de {aluno}: '))
n2 = float(input(f'insira a segunda nota de {aluno}: '))
media = (n1 + n2) / 2
mensagem1 = ('Aprovado')
mensagem2 = ('Reprovado')
if media >= 7:
    print(mensagem1)