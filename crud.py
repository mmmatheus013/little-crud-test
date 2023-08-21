from validations import validar_nome, validar_email, validar_cpf, validar_dates, extrair_numeros
from database import cursor, connection
def cadastrar_pessoa(nome, email, cpf):

    if not validar_nome(nome):
        print("nome inválidos. Não foi possível cadastrar.")
        return False
    if not validar_email(email):
        print("Email inválidos. Não foi possível cadastrar.")
        return False
    if not validar_dates('email_cliente', email):
        print("Email Existente. Não foi possível cadastrar.")
        return False
    if not validar_cpf(extrair_numeros(cpf, '')):
        print("CPF inválidos. Não foi possível cadastrar.")
        return False
    if not validar_dates('cpf_cliente', cpf):
        print("cpf Existente. Não foi possível cadastrar.")
        return False
    consulta = "INSERT INTO custom (nm_cliente, email_cliente, cpf_cliente) VALUES (%s, %s, %s)"
    valores = (nome, email, extrair_numeros(cpf, ''))
    cursor.execute(consulta, valores)
    connection.commit()
    print("Cadastro realizado com sucesso!")



# Função para obter os dados do usuário:
def obter_dados():
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    return nome, email, cpf


# função read:
def listar_read():
    consulta = "SELECT * FROM custom"
    cursor.execute(consulta)
    custom = cursor.fetchall()
    for pessoa in custom:
        print("ID:", pessoa[0])
        print("Nome:", pessoa[1])
        print("Email:", pessoa[2])
        print("CPF:", pessoa[3])
        print("-" * 20)


# Função para editar usuario:
def atualizar_custom(id, nome, email, cpf):
    if validar_cpf(cpf):
        consulta = "UPDATE custom SET nm_cliente = %s, email_cliente = %s, cpf_cliente = %s WHERE id_cliente = %s"
        valores = (nome, email, cpf, id)

        cursor.execute(consulta, valores)
        connection.commit()

        print("Cadastro atualizado com sucesso!")
    else:
        print("CPF inválidos. Não foi possível cadastrar.")



# Função del
def deletar_id(id):
    consulta = "DELETE FROM custom WHERE id_cliente = %s"
    valor = (id,)
    cursor.execute(consulta, valor)
    connection.commit()

    print("Cadastro deletado com sucesso!")


