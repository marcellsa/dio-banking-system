menu = """

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

=> """

balance = 0
limit = 500
statement = ""
number_of_withdrawals = 0
WITHDRAWALS_LIMIT = 3

while True:
    option = input(menu)

    if option == "1":
        value = float(input("Informe o valor do déposito: "))

        if value > 0:
            balance += value
            statement += f"Depósito realizado no valor de: R$ {value:.2f}\n"
        else:
            print("Ops! O valor informado é inválido.")

    elif option == "2":
        value = float(input("Informe valor do saque: "))

        if value > balance:
            print("Ops! Saldo insuficiente.")

        elif value > limit:
            print("Ops! Valor do saque excedeu o limite.")

        elif number_of_withdrawals >= WITHDRAWALS_LIMIT:
            print("Ops! Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            statement += f"Saque: R$ {value:.2f}"
            number_of_withdrawals += 1

        else:
            print("Ops! O valor informado é inválido.")

    elif option == "3":
        print("\n---------{ EXTRATO }---------")
        print(
            "Movimentações não foram realizadas."
            if not statement
            else statement
        )
        print(f"\nSaldo: R$ {balance:.2f}")
        print("-------------------------------")

    elif option == "0":
        break

    else:
        print("Ops, por favor selecione novamente a operação desejada.")
