from filter_user import filter_user


def create_user(users):
    cpf = int(input("Informe o CPF (somente número): "))
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    name = input("Informe o nome completo: ")
    birthday = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    users.append(
        {
            "nome": name,
            "data_nascimento": birthday,
            "cpf": cpf,
            "endereco": address,
        }
    )

    print("=== Usuário criado com sucesso! ===")
