import textwrap


def display_accounts(accounts):
    for account in accounts:
        row = f"""\
            Agência:\t{account['agencia']}
            C/C:\t\t{account['numero_conta']}
            Titular:\t{account['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(row))
