
# Sistema de Autenticação
senha_correta = "1234"
tentativas = 0
acesso = False

while tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas = tentativas + 1

    if senha == senha_correta:
        print("Acesso permitido.")
        acesso = True
        break
    else:
        print("Senha incorreta.")

if acesso == False:
    print("Acesso bloqueado após 3 tentativas.")