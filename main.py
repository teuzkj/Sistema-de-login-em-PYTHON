print ("Seja bem vindo(a) ao sistema de login!")
print ("Vamos começar")
print ("-" * 50)
nome = input("NOME COMPLETO: ")   #INPUT PARA DIGITAR O NOME DO USUÁRIO
print("Olá, {}, tudo bem?".format(nome))
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
        print("Erro: A senha deve conter apenas números. Tente novamente!")

# Confirmar informações do usuário
escolhas = (1,2,3)
print('''Olá {},Voce confirma as informações?
[1]Não. 
[2]Sim. 
[3]Alterar as informações.'''.format(nome))
escolha = int(input("Escreva a escolha: "))

if escolha == 1:
    print("Que pena, até mais...")
    exit()

elif escolha == 2:
    print ("Seja bem vindo(a), {}.".format(nome))
    print ("EMAIL: {}".format(email))
    print ("SENHA: {}".format(senha))

elif escolha == 3:
    print ("Vamos alterar suas informações.")
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
    nova_senha = int(input("SENHA: "))
    while True:
        try: 
            senha = int(input("SENHA: "))
            break
        except ValueError:
            print("Erro: A senha deve conter apenas números. Tente novamente!")

        # Atualizando as informações
    nome = novo_nome
    idade = nova_idade
    email = novo_email
    senha = nova_senha

    print ("Informações atualizadas com sucesso!")
    print ("Seja bem vindo(a), {}.".format(nome))
    print ("IDADE: {} \nEMAIL: {} \nSENHA: {} ".format(idade,email,senha))




