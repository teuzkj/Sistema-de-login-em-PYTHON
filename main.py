print ("Seja bem vindo(a) ao sistema de login!")
print ("Vamos começar")
print ("-" * 50)
nome = input("NOME COMPLETO: ")   #INPUT PARA DIGITAR O NOME DO USUÁRIO
print(f"Olá, {nome}, tudo bem?")
while True:
    idade = int(input("IDADE: "))   #INPUT PARA DEFINIR A IDADE DO USUÁRIO

# Se o usuário tiver 17 anos ou menos o programa não ira prosseguir
    if idade <= 17:     
        print("Voce não tem idade o suficiente para fazer login no site!")
        print("Por favor, insira uma idade válida (18 anos ou mais).")   
    else:
        break # Sai do loop quando a idade for válida
# Se o usuário tiver 18 anos ou mais o programa ira prosseguir

print("Voce tem idade o suficiente para fazer o login!")
print("Digite agora o seu email")
email = input("EMAIL: ")
print("Digite a sua senha apenas com números.")
while True:
    try: 
        senha = int(input("SENHA: "))
        break
    except ValueError:
        print("ERRO: A senha deve conter apenas números. Tente novamente!")

# Confirmar informações do usuário
escolhas = (1,2,3)
print(f'''Olá {nome},Voce confirma as informações?
[1]Não. 
[2]Sim. 
[3]Alterar as informações.''')
escolha = int(input("Escreva a escolha: "))

if escolha == 1:
    print("Que pena, até mais...")
    exit()

elif escolha == 2:
    print (f"Seja bem vindo(a), {nome}.")
    print (f"EMAIL: {email}")
    print (f"SENHA: {"*" * len(str(senha))}")

elif escolha == 3:
    print ("Vamos alterar suas informações.")
    confirmar_email = input("Digite o email anterior: ")
    if confirmar_email == email:
        print("Voce digitou o email anterior corretamente!")
        confirmar_senha = int(input("Digite a senha anterior: "))
        if confirmar_senha == senha:
            print("Voce digitou a senha corretamente!")
            print("Agora voce pode realizar alterações.")
            print("Alterações")
            novo_nome = input("NOME COMPLETO: ")
            while True:
                nova_idade = int(input("IDADE: "))
                if nova_idade <= 17:
                    print("Voce não tem idade o suficiente para fazer login no site!")
                    print("Por favor, insira uma idade válida (18 anos ou mais).")  
                else:
                    break
            print("Voce tem idade o suficiente para fazer o login!")
            print("Digite agora o novo email")
            novo_email = input("EMAIL: ")
            print("Digite agora a sua nova senha apenas com números.")
            while True:
                try: 
                    nova_senha = int(input("SENHA: "))
                    break
                except ValueError:
                    print("ERRO: A senha deve conter apenas números. Tente novamente!")

        else: 
            print("Senha não encontrada em nosso sistema")
            exit()

    else:
        print("Email não encontrado em nosso sistema")
        exit()

    # Atualizando as informações
    nome = novo_nome
    idade = nova_idade
    email = novo_email
    senha = nova_senha

    print ("Informações atualizadas com sucesso!")
    print (f"Seja bem vindo(a), {nome}.")
    print (f"IDADE: {idade} \nEMAIL: {email} \nSENHA: {"*" * len(str(senha))} ")

# Escolher fazer login
print("-" * 50)
escolhas_login = (1,2,3)
print(f'''Olá {nome}, agora o que vamos fazer?
[1]Sair
[2]
[3]Login''')
escolha_login = int(input("Escreva a escolha: "))

if escolha_login == 1:
    print("Que pena, até a próxima.")
    exit()

elif escolha_login == 2:
    print("ABA AINDA EM DESENVOLVIMENTO")

elif escolha_login == 3:
    print("Digite agora email cadastrado")
    email_login = input("EMAIL: ")
    if email_login != email:
        print("Email não encontrado em nosso sistema. Tente novamente ou cadastre-se")
    else:
        print("Email encontrado em nosso sistema!")

        # verifica a senha com 3 tentativas
        tentativas = 3
        while tentativas > 0:
            try:
                senha_login = int(input("Digite a sua senha numérica: "))

                # login efeuado
                if senha_login == senha:
                    print("-" * 50)
                    print("LOGIN EFETUADO COM SUCESSO!")
                    print(f"Seja bem vindo(a) {nome}.")
                    break
                else:
                    tentativas -= 1
                    if tentativas > 0:
                        print(f"Senha incorreta. Tentativas restantes: {tentativas}")
                    else:
                        print("Voce excedeu o número de tentativas. Tente mais tarde.")
            except ValueError:
                print("ERRO: A senha deve conter apenas números. Tente novamente!")




