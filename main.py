# Lista que guarda as pessoas cadastradas
# Mantive como global para simplificar o projeto
pessoas = []


def menu():
    print('••' *15)
    print('Sistema de Cadastro de Pessoas')
    print('••' *15)
    print()
    print('1 - Cadastrar pessoa')
    print('2 - Listar pessoas')
    print('3 - Editar pessoa')
    print('4 - Excluir pessoa')
    print('0 - Sair')


def cadastrar_pessoa():
    print()
    print('----Cadastro de Pessoa----')
    print()

    nome = input('Nome: ').strip().title()
    idade = input('Idade: ').strip()
    email = input('Email: ').strip()

    pessoa = {
        'nome': nome,
        'idade': idade,
        'email': email
    }

    pessoas.append(pessoa)
    print()
    print('Pessoa cadastrada com sucesso!')


def listar_pessoas():
    if not pessoas:
        print()
        print('Nenhuma pessoa cadastrada.')
        return

    print()
    print('----Lista de Pessoas----')
    print()
    for i, pessoa in enumerate(pessoas, start=1):
        print(f"{i}. {pessoa['nome']} | {pessoa['idade']} anos | {pessoa['email']}")


def editar_pessoa():
    listar_pessoas()

    if not pessoas:
        return

    try:
        print()
        indice = int(input('Digite o número da pessoa que deseja editar: ')) - 1

        if indice < 0 or indice >= len(pessoas):
            print('Pessoa inválida.')
            return

        pessoa = pessoas[indice]

        print()
        print('Deixe em branco se não quiser alterar o campo.')

        nome = input(f"Nome ({pessoa['nome']}): ").strip()
        idade = input(f"Idade ({pessoa['idade']}): ").strip()
        email = input(f"Email ({pessoa['email']}): ").strip()

        if nome:
            pessoa['nome'] = nome.title()
        if idade:
            pessoa['idade'] = idade
        if email:
            pessoa['email'] = email

        print()
        print('Dados atualizados com sucesso!')
        print()

    except ValueError:
        print('Entrada inválida. Digite um número.')


def excluir_pessoa():
    listar_pessoas()

    if not pessoas:
        return

    try:
        indice = int(input('\nDigite o número da pessoa que deseja excluir: ')) - 1

        if indice < 0 or indice >= len(pessoas):
            print('Pessoa inválida.')
            return

        pessoas.pop(indice)
        print()
        print('Pessoa removida com sucesso!')
        print()

    except ValueError:
        print('Entrada inválida. Digite um número.')


def main():
    while True:
        menu()
        print()
        opcao = input('Escolha uma opção: ').strip()
        print()

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '0':
            print('\nSaindo do sistema. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente.')


    
main()

