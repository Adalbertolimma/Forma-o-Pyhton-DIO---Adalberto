#Desafio de Codigo - Sistema Bancario

menu= """
                Seja Bem vindo ao nosso sistema Bancario
                        Escolha a opção que deseja:
                         [1] Depositar
                         [2] Sacar
                         [3] Extrato
                         [4] Sair
"""
saldo=0
limite = 500
extrato= ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor= float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f" Depósito R${valor:.2f} \n"
            print(f"O valor R$:{valor} foi depósitado com sucesso!")
        else:
            print("Operação falhou! valor informado é invalido.")

    elif opcao == "2":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques =  numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Ovalor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: R${valor:.2f}\n"
            numero_saques +=1
            print(f"Confira seu Saque no valor de: R${valor}")


        else:
            print("Operação falhou! O valor informado é inválido")

    
    elif opcao == "3":
        print("\n ==============EXTRATO===============")
        print("Não Foram realizadas Movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "4":
        print("Obrigado por utilizar o nosso banco.  Tenha um ótimo dia!")
        break
        
    else: 
        print("Operação Inválida, por favor slecione novamente a opção desejada.")
        

