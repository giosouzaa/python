import sys

saldo = 2000.0

opcao = int(input("Selecione uma opção: \n[1] Sacar\n[2] Extrato\n: "))

if opcao == 1:
    saque = float(input("Informe o valor do saque :"))
    if saldo>= saque:
        print("Realizando saque!")
    else:
        print("Saldo insuficiente!")

    # if ternário

    status = "Sucesso" if saldo >= saque else "Falha"
    print(f"{status} ao realizar o saque")

elif opcao == 2:
    print("Exibindo o extrato ...", saldo)
else:
    sys.exit("Opção inválida")


