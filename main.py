print ("Seja bem vindo(a) ao sistema de login!")
print ("Vamos começar")
print ("-" * 50)
nome = input("NOME COMPLETO: ")   #INPUT PARA DIGITAR O NOME DO USUAÁRIO
print("Olá, {}, tudo bem?".format(nome))
idade = int(input("IDADE: "))   #INPUT PARA DEFINIR A IDADE DO USUÁRIO

# Se o usuário tiver 17 anos ou menos o programa não ira prosseguir
if idade <= 17:     
    print("Voce não tem idade o suficiente para fazer login no site!")
    exit()   

# Se o usuário tiver 18 anos ou mais o programa ira prosseguir
else:
    print("Voce tem idade o suficiente para fazer o login!")
    email = input("EMAIL: ")
