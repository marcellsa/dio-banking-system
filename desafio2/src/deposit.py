def deposit(balance, value, account_statement, /):
    if value > 0:
        balance += value
        account_statement += f"Depósito:\tR$ {value:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return balance, account_statement
