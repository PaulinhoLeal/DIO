menu = """
Escolha a operação que deseja realizar!
[s] - Sacar
[d] - Depositar
[e] - Ver extrato
[q] - Sair
"""
limite = 0
saque=0.0
saldo = 0.0
deposito = 0.0
extrato=''
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao.upper() == 'S':
        valor = float(input('Digite o valor para sacar:  '))

        if saldo < valor :
            print('Saldo insuficiente')
        elif numero_saques==LIMITE_SAQUE:
            print('Número de saques diários excedido!')
        elif valor > 500:
            print('O valor de saque nao pode exceder R$ 500.00')
        elif  valor < 0 :
            print('valor inválido')
        else:
            saldo = saldo - valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
    elif opcao.upper() == 'D':
        valor = float(input('Digite o valor para depositar: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
    elif opcao.upper() == 'E': 
        print('#####EXTRATO#####')
        print(extrato)
        print(f'Saldo: R$ {saldo}')
    elif opcao.upper() == 'Q':
        
        break
    else:
        print('Selecione uma operação válida')
    



