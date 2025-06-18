import time
from tkinter import Tk, Label, Button, Toplevel, Entry, messagebox

""""print ("-" * 50)
print ("Seja bem vindo(a) ao sistema de login!")
print ("Vamos começar")
print ("-" * 50)
nome = input("NOME COMPLETO: ")   #INPUT PARA DIGITAR O NOME DO USUÁRIO
print(f"Olá, {nome}, tudo bem?")
while True:
    idade = int(input("IDADE: "))   #INPUT PARA DEFINIR A IDADE DO USUÁRIO

# Se o usuário tiver 17 anos ou menos o programa não ira prosseguir
    if idade <= 17:     
        print("Você não tem idade o suficiente para fazer login no site!")
        print("Por favor, insira uma idade válida (18 anos ou mais).")   
    else:
        break # Sai do loop quando a idade for válida

# Se o usuário tiver 18 anos ou mais o programa ira prosseguir
print("Você tem idade o suficiente para fazer o login!")
print ("-" * 50)
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
print ("-" * 50)
escolhas = (1,2,3)
print(f'''Olá {nome},Você confirma as informações?
[1]Não. 
[2]Sim. 
[3]Alterar as informações.''')
escolha = int(input("Escreva a escolha: "))
print ("-" * 50)
print("Carregando...")
time.sleep(1)
print("Carregamento concluído!")

if escolha == 1:
    print ("-" * 50)
    print("Que pena, até mais...")
    exit()

elif escolha == 2:
    print ("-" * 50)
    print (f"Seja bem vindo(a), {nome}.")
    print (f"EMAIL: {email}")
    print (f"SENHA: {"*" * len(str(senha))}")

elif escolha == 3:
    print ("-" * 50)
    print("Vamos alterar as suas informações.")

    # Verificando o email com 3 tentativas
    email_correto = False
    for tentativa in range(3): #Permite 3 tentativas
        confirmar_email = input("Digite o email anterior: ")
        if confirmar_email == email:
            print("Você digitou o email anterior corretamente!")
            email_correto = True
            break
        else: 
            print("Email incorreto!")
            if tentativa < 2: # Mostra apenas se houver mais tentativas
                print(f"Voce tem mais {2 - tentativa} tentativa(s).")

    if not email_correto:
        print("Número máximo de tentativas excedido para o email.")
        exit() 

    # Verificação da senha com tentativas
    senha_correta = False
    for tentativa in range(3): # Permite 3 tentativas
        try:
            confirmar_senha = int(input("Digite a senha anterior: "))
            if confirmar_senha == senha:
                print("Você digitou a senha corretamente!")
                senha_correta = True 
                break
            else:
                print("Senha incorreta!")
                if tentativa < 2: # Mostra apenas se tiver mais tentativas
                    print(f"Você tem mais {2 - tentativa} tentativa(s).")
        except ValueError:
            print("A senha deve conter apenas números")
            if tentativa < 2: 
                print(f"Você tem mais {2 - tentativa} tentativa(s).")
    if not senha_correta: 
        print("Número máximo de tentativas excedido para a senha.")
        exit()

    # Se chegou até aqui, ambas as verificações passaram 
    print ("-" * 50)
    print("Carregando...")
    time.sleep(1)
    print("Carregamento concluído!")
    print ("-" * 50)
    print("Agora você pode realizar as alterações.")
    print ("-" * 50)
    print("Realize as alterações")
    novo_nome = input("NOME COMPLETO: ")

    while True: 
        nova_idade = int(input("IDADE: "))
        if nova_idade <= 17:
            print("Você não tem idade o suficiente para fazer o login no site!")
            print("Por favor, insira uma idade válida (18 anos ou mais).")
        else:
            break

    print("Você tem idade o suficiente para fazer o login!")
    print ("-" * 50)
    print("Digite agora o novo email")
    novo_email = input("EMAIL: ")   

    print("Digite agora a sua nova senha apenas com númneros.")
    while True:
        try:
            nova_senha = int(input("SENHA: "))  
            break
        except ValueError:
            print("ERRO: A senha deve conter apenas números. Tente novamente.")
            
print ("-" * 50)
print("Carregando...")
time.sleep(1)
print("Carregamento concluído!")

# Atualizando as informações
nome = novo_nome
idade = nova_idade
email = novo_email
senha = nova_senha

print ("-" * 50)
print ("Informações atualizadas com sucesso!")
print ("-" * 50)
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
print ("-" * 50)
print("Carregando...")
time.sleep(1)
print("Carregamento concluído!")

if escolha_login == 1:
    print ("-" * 50)
    print("Que pena, até a próxima.")
    exit()

elif escolha_login == 2:
    print ("-" * 50)
    print("ABA AINDA EM DESENVOLVIMENTO")

elif escolha_login == 3:
    print ("-" * 50)
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
                    print("Carregando...")
                    time.sleep(1)
                    print("Carregamento concluído!")
                    print("-" * 50)
                    print("LOGIN EFETUADO COM SUCESSO!")
                    print("-" * 50)
                    print(f"Seja bem vindo(a) {nome}.")
                    print (f"EMAIL: {email}")
                    print (f"SENHA: {"*" * len(str(senha))}")
                    print("-" * 50)
                    break
                else:
                    tentativas -= 1
                    if tentativas > 0:
                        print(f"Senha incorreta. Tentativas restantes: {tentativas}")
                    else:
                        print("Você excedeu o número de tentativas. Tente mais tarde.")
            except ValueError:
                print("ERRO: A senha deve conter apenas números. Tente novamente!")"""


nome_registrado = None
senha_registrada = None

def criar_perfil():
    global nome_registrado, senha_registrada, janela # Permite modificar a váriavel global

    # Esconde a janela principal temporariamente
    janela.withdraw() 

    # Criar uma nova janela para o registro
    janela_registro = Toplevel(janela) #sustitui a janela já presente
    janela_registro.title("Registro")
    janela_registro.geometry("300x200") # Tamanho da janela

    # Quando fechar a janela de registro, mostra a príncipal novamente
    janela_registro.protocol("WM_DELETE_WINDOW", lambda: [janela_registro.destroy(), janela.deiconify()])

    # Label e Entry para o nome 
    Label(janela_registro, text="Digite o seu nome: ").pack(pady=10)
    entrada_nome = Entry(janela_registro)
    entrada_nome.pack(pady=5)

    Label(janela_registro, text="Digite sua senha: ").pack(pady=10)
    entrada_senha = Entry(janela_registro, show="*")
    entrada_senha.pack(pady=5)

    # Botão para confirmar
    def confirmar_registro():
        global nome_registrado, senha_registrada
        nome = entrada_nome.get()
        senha = entrada_senha.get()

        if nome and senha: # Verifica se o nome e a senha não estão vázios
            nome_registrado = nome # Armazena o nome registrado
            senha_registrada = senha # Armazena a senha registrada
            messagebox.showinfo("Sucesso", f"Olá, {nome}! Registro concluído.")
            janela_registro.destroy()
            janela.deiconify() # Mostra a janela príncipal novamente
        else:
            messagebox.showerror("Erro!", "Preencha o nome e a senha de forma válida.")

    Button(janela_registro, text="Confirmar", command=confirmar_registro).pack(pady=15) 


def login_perfil():
    if nome_registrado and senha_registrada is None:
        messagebox.showerror("Erro", "Nenhum usuário registrado ainda.")
        return

    # Esconde a janela príncipal 
    janela.withdraw()

    # Criar uma janela para o login
    janela_login = Toplevel(janela)
    janela_login.title("Login")
    janela_login.geometry("300x200")

    # Quando fechar a janela de login, mostra a príncipal novamente
    janela_login.protocol("WM_DELETE_WINDOW", lambda: [janela_login.destroy(), janela.deiconify()])

    # Label e Entry para o nome
    Label(janela_login, text="Digite o seu nome: ").pack(pady=10)
    entrada_nome_login = Entry(janela_login)
    entrada_nome_login.pack(pady=5)

    Label(janela_login, text="Digite a sua senha: ").pack(pady=10)
    entrada_senha_login = Entry(janela_login)
    entrada_senha_login.pack(pady=5)

    # Botão para confirmar
    def confirmar_login():
        nome_login = entrada_nome_login.get()
        senha_login = entrada_senha_login.get()
        if nome_login == nome_registrado and senha_login == senha_registrada:
            messagebox.showinfo("Sucesso!", f"Bem-vindo(a) de volta, {nome_login}!")
            janela_login.destroy()
            janela.deiconify() # Mostra a janela príncipal novamente
        else:
            messagebox.showerror("Erro!", "Por favor, digite um nome ou senha já registrados.")

    Button(janela_login, text="Confirmar", command=confirmar_login).pack(pady=15)


# Criação da janela
janela = Tk() # Cria a janela 
janela.geometry("300x200") 
janela.title("Tela Inicial") # Define o título da janela

# Configuração da janela de cadastro do usuário
titulo_inicial = Label(janela, text="Inicio")
titulo_inicial.grid(column=0, row=0, pady=10)

texto_orientacao = Label(janela, text="Escolha se você quer realizar um registro ou login")
texto_orientacao.grid(column=0, row=1, pady=10)

botao_registro = Button(janela, text="Registro", command=criar_perfil) # Botão de criação de perfil
botao_registro.grid(column=0, row=2, pady=10)

botao_login = Button(janela, text="Login", command=login_perfil) # Botão de login em um perfil já existente
botao_login.grid(column=0, row=3, pady=10)

texto_registro = Label(janela, text="")




# Finalizando o programa
janela.mainloop() # Exibe a janela e a mantem exibida sem fechar




