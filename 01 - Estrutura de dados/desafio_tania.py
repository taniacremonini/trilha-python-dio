from datetime import datetime

print("Escolha e digite as opções abaixo !:")

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(" Valor inválido. Tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print(" Valor inválido. Digite um valor positivo.")
        elif excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"O valor máximo por saque é R${limite:.2f}.")
        elif excedeu_saques:
            print("Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "3":
        print("\n" + "="*35 )
        print ("           EXTRATO BANCÁRIO")
        print("="*35)

        if not extrato:
         print("Nenhuma movimentaçaõ encontrada! ")
        else:
         print(extrato)
         print ("-"*35)
         print (f"\nSaldo: R$ {saldo:.2f}")
         print (f"Data/Hora: {datetime.now() .strftime('%d/%m/%y %H:%M:%S ')}")
         print ("="*35 + "\n")

    elif opcao == "4":
        print("Saindo do sistema bancário. Obrigado por usar!")
        break
    else:
      print("Opção Invalida. Tente novamente")