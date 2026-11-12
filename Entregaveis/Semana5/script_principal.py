# Sistema de Análise de Dados

import re
import csv

# Exceção personalizada
class FormatoInvalidoError(Exception):
    pass

# Validações com regex
def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(padrao, email) is not None

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return re.match(padrao, cpf) is not None

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\) \d{5}-\d{4}$"
    return re.match(padrao, telefone) is not None

def validar_data(data):
    padrao = r"^\d{2}/\d{2}/\d{4}$"
    return re.match(padrao, data) is not None

# Programa principal
def main():
    nome_arquivo = "dados.csv"
    registros = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                try:
                    email = linha["email"]
                    cpf = linha["cpf"]
                    telefone = linha["telefone"]
                    data = linha["data"]

                    if not validar_email(email):
                        raise FormatoInvalidoError("E-mail inválido.")

                    if not validar_cpf(cpf):
                        raise FormatoInvalidoError("CPF inválido.")

                    if not validar_telefone(telefone):
                        raise FormatoInvalidoError("Telefone inválido.")

                    if not validar_data(data):
                        raise FormatoInvalidoError("Data inválida.")

                    registros.append([email, cpf, telefone, data, "Válido"])

                except KeyError as erro:
                    print(f"Coluna ausente no CSV: {erro}")

                except FormatoInvalidoError as erro:
                    registros.append([
                        linha.get("email", ""),
                        linha.get("cpf", ""),
                        linha.get("telefone", ""),
                        linha.get("data", ""),
                        f"Inválido - {erro}"
                    ])

    except FileNotFoundError:
        print("Erro: arquivo dados.csv não encontrado.")

    except ValueError as erro:
        print(f"Erro de valor: {erro}")

    finally:
        print("Análise finalizada.\n")

    # Estatísticas
    total = len(registros)
    validos = 0

    for registro in registros:
        if registro[4] == "Válido":
            validos = validos + 1

    invalidos = total - validos

    # Relatório final
    print("===== RELATÓRIO =====")

    for registro in registros:
        print(f"Email: {registro[0]}")
        print(f"CPF: {registro[1]}")
        print(f"Telefone: {registro[2]}")
        print(f"Data: {registro[3]}")
        print(f"Status: {registro[4]}")
        print("----------------------")

    print(f"Total de registros: {total}")
    print(f"Registros válidos: {validos}")
    print(f"Registros inválidos: {invalidos}")

main()