from filter_user import filter_user


def create_account(agency, account_number, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filter_user(cpf, users)

    if user:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agency,
            "numero_conta": account_number,
            "usuario": user,
        }

    print(
        """\n@@@ Usuário não encontrado,
        fluxo de criação de conta encerrado! @@@"""
    )
