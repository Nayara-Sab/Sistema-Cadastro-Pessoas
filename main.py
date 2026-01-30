# Lista global que armazena todas as pessoas cadastradas
# Cada pessoa será representada por um dicionário
pessoas = []


def menu():
    """
    Exibe o menu principal do sistema com as opções disponíveis.
    """
    print("\n--- Sistema de Cadastro de Pessoas ---")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Editar pessoa")
    print("4 - Excluir pessoa")
    print("0 - Sair")


def cadastrar_pessoa():
    """
    Solicita os dados do usuário e cadastra uma nova pessoa na lista.
    """
    print("\n--- Cadastro de Pessoa ---")

    # Entrada do nome, removendo espaços extras e colocando a primeira letra maiúscula
    nome = input("Nome: ").strip().title()

    # Entrada da idade (como string)
    idade = input("Idade: ").strip()

    # Entrada do email
    email = input("Email: ").strip()

    # Cria um dicionário com os dados da pessoa
    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    # Adiciona a pessoa à lista de pessoas
    pessoas.append(pessoa)

    print("\nPessoa cadastrada com sucesso!")


def listar_pessoas():
    """
    Exibe todas as pessoas cadastradas.
    """
    # Verifica se a lista está vazia
    if not pessoas:
        print("\nNenhuma pessoa cadastrada.")
        return

    print("\n--- Lista de Pessoas ---")

    # Percorre a lista de pessoas e exibe cada uma
    # enumerate serve para mostrar a numeração começando do 1
    for i, pessoa in enumerate(pessoas, start=1):
        print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Email: {pessoa['email']}")


def editar_pessoa():
    """
    Permite editar os dados de uma pessoa já cadastrada.
    """
    listar_pessoas()

    # Se não houver pessoas, encerra a função
    if not pessoas:
        return

    try:
        # Solicita o número da pessoa e ajusta o índice para começar em 0
        indice = int(input("\nDigite o número da pessoa que deseja editar: ")) - 1

        # Verifica se o índice é válido
        if indice < 0 or indice >= len(pessoas):
            print("Pessoa inválida.")
            return

        # Acessa a pessoa escolhida
        pessoa = pessoas[indice]

        print("\nDeixe em branco para manter o valor atual.")

        # Solicita novos valores
        novo_nome = input(f"Nome ({pessoa['nome']}): ").strip().title()
        nova_idade = input(f"Idade ({pessoa['idade']}): ").strip()
        novo_email = input(f"Email ({pessoa['email']}): ").strip()

        # Atualiza apenas os campos que foram preenchidos
        if novo_nome:
            pessoa["nome"] = novo_nome
        if nova_idade:
            pessoa["idade"] = nova_idade
        if novo_email:
            pessoa["email"] = novo_email

        print("\nPessoa editada com sucesso!")

    except ValueError:
        # Captura erro caso o usuário digite algo que não seja número
        print("Entrada inválida.")


def excluir_pessoa():
    """
    Remove uma pessoa da lista.
    """
    listar_pessoas()

    # Se não houver pessoas, encerra a função
    if not pessoas:
        return

    try:
        # Solicita o número da pessoa e ajusta o índice
        indice = int(input("\nDigite o número da pessoa que deseja excluir: ")) - 1

        # Verifica se o índice é válido
        if indice < 0 or indice >= len(pessoas):
            print("Pessoa inválida.")
            return

        # Remove a pessoa da lista
        pessoas.pop(indice)
        print("\nPessoa excluída com sucesso!")

    except ValueError:
        print("Entrada inválida.")


def main():
    """
    Função principal que controla o funcionamento do sistema.
    """
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            editar_pessoa()
        elif opcao == "4":
            excluir_pessoa()
        elif opcao == "0":
            print("\nSaindo do sistema. Até mais! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Ponto de entrada do programa
# Chama a função principal para iniciar o sistema
if __name__ == "__main__":
    main()
