import socket
import re
from database import cursor
# validar nome:
def validar_nome(nome):
    if len(nome) > 100:
        return False
    if len(nome) < 2:
        return False
    return True

# validação email
def validar_email(email):
    print(email)
    if len(email) > 100:
        return False
    if len(email) < 5:
        return False
    #validar formato de email
    pattern = r"^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)$"
    match = re.match(pattern, email)
    if not match:
        return False
    #validar dominio
    dominio = match.group(1)
    try:
        mx_records = socket.getaddrinfo(dominio, None, socket.AF_UNSPEC, socket.SOCK_STREAM, socket.IPPROTO_TCP,
                                        socket.AI_CANONNAME)

        if not mx_records:
            return False

    except socket.gaierror:
        return False
    return True

# validação cpf *
def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    if cpf == '00000000000' or cpf == '11111111111' or \
            cpf == '22222222222' or cpf == '33333333333' or \
            cpf == '44444444444' or cpf == '55555555555' or \
            cpf == '66666666666' or cpf == '77777777777' or \
            cpf == '88888888888' or cpf == '99999999999':
        return False

        # Cálculo do 1º dígito verificador
    soma = sum([int(cpf[i]) * (10 - i) for i in range(9)])
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        d1 = 0
    else:
        d1 = resto

    # Cálculo do 2º dígito verificador
    soma = sum([int(cpf[i]) * (11 - i) for i in range(10)])
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        d2 = 0
    else:
        d2 = resto

    return d1 == int(cpf[9]) and d2 == int(cpf[10])
    return True


# extrair numeros string:
def extrair_numeros(text, to_replace):
    text = text.replace(to_replace, '')
    digits = '0123456789'
    new_text = ''
    for char in text:
        if char in digits:
            new_text += char

    return new_text


# validação de dados existentes:
def validar_dates(coluna, valor):
    consulta = f"SELECT * FROM custom WHERE {coluna}='{valor}' LIMIT 1"
    cursor.execute(consulta)
    custom = cursor.fetchone()
    if custom:
        return False

    return True