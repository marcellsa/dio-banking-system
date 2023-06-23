def withdraw(
    *,
    balance,
    value,
    account_statement,
    limit,
    withdrawal_numbers,
    withdrawal_limit,
):
    excedeu_saldo = value > balance
    excedeu_limite = value > limit
    excedeu_saques = withdrawal_numbers >= withdrawal_limit

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif value > 0:
        balance -= value
        account_statement += f"Saque:\t\tR$ {value:.2f}\n"
        withdrawal_numbers += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return balance, account_statement
