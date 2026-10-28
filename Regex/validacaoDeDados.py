import re

def validarEmail(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validarCpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))

def validarTelefone(telefone):
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    return bool(re.match(padrao, telefone))

def validarData(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(padrao, data))


#TESTES
print(validarEmail("vinicius@email.com"))
print(validarCpf("565.414.231-85"))
print(validarTelefone("(98) 95214-5468"))
print(validarData("2026-10-30"))
