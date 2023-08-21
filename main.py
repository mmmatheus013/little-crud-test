from crud import cadastrar_pessoa, listar_read, atualizar_custom, obter_dados, deletar_id
from database import cursor, connection
print()
print('-' * 10, "Sistema de Cadastro", '-' * 10)

# system
while True:
    print("\nOpções:")
    print("[1] - Cadastrar pessoa")
    print("[2] - Listar pessoas")
    print("[3] - Atualizar cadastro")
    print("[4] - Deletar cadastro")
    print("[0] - Sair")

    opcao = input("Escolha uma opção: ")
    # create
    if opcao == "1":
        nome, email, cpf = obter_dados()
        cadastrar_pessoa(nome, email, cpf)
    #  read
    elif opcao == "2":
        listar_read()
    # update
    elif opcao == "3":
        id = int(input("Digite o ID que deseja atualizar: "))
        nome, email, cpf = obter_dados()
        atualizar_custom(id, nome, email, cpf)
    #  delet
    elif opcao == "4":
        id = int(input("Digite o ID da pessoa que deseja deletar: "))
        deletar_id(id)
    elif opcao == "0":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# fechar conexao
cursor.close()
connection.close()