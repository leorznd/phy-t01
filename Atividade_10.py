opcao = input('Bem vindo ao Menu. Digite 1 para Depósito, 2 para Saque ou "s" para Sair: ')
saldo = 0
while opcao == str(1) or str(2):
    if opcao == str(1):
        deposito = float(input('Insira o valor que deseja depositar: '))
        saldo = saldo + deposito
        opcao = input('O que deseja fazer agora? ')
        continue
    elif opcao == str(2):
        if saldo == 0:
            opcao = input('Você não possui saldo suficiente para saque. Tente outra opção: ')
            continue
        else:
            saque = float(input('Insira o valor que deseja sacar: '))
            if saldo - saque < 0:
                opcao = input('Você não tem saldo suficiente para saque, tente outra opção ou outro valor de saque: ')
            else:
                saldo = saldo - saque
                opcao = input('O que deseja fazer agora? ')
                continue
    elif opcao == 's':
        print(f'Seu saldo final é de R${saldo:.2f}'.replace('.',',') + '. Obrigado por utilizar nossos serviços!')
        break