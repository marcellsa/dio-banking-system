def display_statement(balance, /, *, account_statement):
    print("\n==============={ EXTRATO }===============")
    print(
        "Não foram realizadas movimentações."
        if not account_statement
        else account_statement
    )
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("==========================================")
