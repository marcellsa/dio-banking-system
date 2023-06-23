from create_account import create_account
from create_user import create_user
from deposit import deposit
from display_accounts import display_accounts
from dsplay_statement import display_statement
from menu import menu
from withdraw import withdraw


def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    bank_statement = ""
    withdrawal_numbers = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            value = float(input("Informe o valor do depósito: "))

            balance, bank_statement = deposit(balance, value, bank_statement)

        elif option == "s":
            value = float(input("Informe o valor do saque: "))

            balance, bank_statement = withdraw(
                saldo=balance,
                valor=value,
                extrato=bank_statement,
                limite=limit,
                numero_saques=withdrawal_numbers,
                limite_saques=WITHDRAWAL_LIMIT,
            )

        elif option == "e":
            display_statement(balance, account_statement=bank_statement)

        elif option == "nu":
            create_user(users)

        elif option == "nc":
            numero_conta = len(accounts) + 1
            conta = create_account(AGENCY, numero_conta, users)

            if conta:
                accounts.append(conta)

        elif option == "lc":
            display_accounts(accounts)

        elif option == "q":
            break

        else:
            print(
                """Operação inválida, por favor selecione
                novamente a operação desejada."""
            )


main()
