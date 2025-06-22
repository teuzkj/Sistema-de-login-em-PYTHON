import time
from tkinter import Tk, Label, Button, Toplevel, Entry, Frame, messagebox


nome_registrado = None
idade_registrada = None
senha_registrada = None
email_registrado = None

def criar_perfil():
    global nome_registrado, idade_registrada, email_registrado, senha_registrada, janela # Permite modificar a váriavel global

    # Esconde a janela principal temporariamente
    janela.withdraw() 

    # Criar uma nova janela para o registro
    janela_registro = Toplevel(janela) #sustitui a janela já presente
    janela_registro.title("Registro")
    janela_registro.geometry("400x500") # Tamanho da janela

    # centraliza os elementos
    frame_principal = Frame(janela_registro)
    frame_principal.pack(pady= 20, padx=20, fill="both", expand=True)

    def voltar_inicio():
        janela_registro.destroy()
        janela.deiconify()

    # Quando fechar a janela de registro, mostra a príncipal novamente
    janela_registro.protocol("WM_DELETE_WINDOW", voltar_inicio)

    # Botão para confirmar - Definido antes de ser usado
    def confirmar_registro():
        global nome_registrado, idade_registrada, email_registrado, senha_registrada
        nome = entrada_nome.get().strip()
        idade = entrada_idade.get().strip()
        email = entrada_email.get().strip()
        senha = entrada_senha.get().strip()

        if nome and idade and email and senha: # Verifica se o nome, email e a senha não estão vázios
            nome_registrado = nome # Armazena o nome registrado
            idade_registrada = idade # armazena a idade registrada
            email_registrado = email # armazena a senha registrada
            senha_registrada = senha # Armazena a senha registrada
            messagebox.showinfo("Sucesso", f"Olá, {nome}! Registro concluído.")
            janela_registro.destroy()
            janela.deiconify() # Mostra a janela príncipal novamente
        else:
            messagebox.showerror("Erro!", "Preencha todas as informações de forma válida.")

    # Frame para os campos de entrada
    frame_campos_registro = Frame(frame_principal)
    frame_campos_registro.pack(fill="both", expand=True)

    # Label e Entry para o nome, email e senha dentro do frame_campos
    Label(frame_campos_registro, text="Nome completo: ", font=fonte_botao).pack(pady=10)
    entrada_nome = Entry(frame_campos_registro)
    entrada_nome.pack(pady=5, fill="x")

    Label(frame_campos_registro, text="Idade: ", font=fonte_botao).pack(pady=10)
    entrada_idade = Entry(frame_campos_registro)
    entrada_idade.pack(pady=5, fill="x")

    Label(frame_campos_registro, text="Email: ", font=fonte_botao).pack(pady=10)
    entrada_email = Entry(frame_campos_registro)
    entrada_email.pack(pady=5, fill="x")

    Label(frame_campos_registro, text="Senha: ", font=fonte_botao).pack(pady=10)
    entrada_senha = Entry(frame_campos_registro, show="*")
    entrada_senha.pack(pady=5, fill="x")

    # Frame para os botões
    frame_botoes = Frame(frame_principal)
    frame_botoes.pack(side="bottom", pady=20, fill="x")

    # Botão Confirmar e voltar
    Button(frame_botoes, text="Confirmar", command=confirmar_registro, font=fonte_botao).pack(side="left", padx=10, expand=True, fill="x")
    Button(frame_botoes, text="Voltar", command=voltar_inicio, font=fonte_botao).pack(side="right", padx=10, expand=True, fill="x") 

def login_perfil():
    if nome_registrado and email_registrado and senha_registrada is None:
        messagebox.showerror("Erro", "Nenhum usuário registrado ainda.")
        return

    # Esconde a janela príncipal 
    janela.withdraw()

    # Criar uma janela para o login
    janela_login = Toplevel(janela)
    janela_login.title("Login")
    janela_login.geometry("300x500")

    # Frame principal
    frame_principal = Frame(janela_login)
    frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

    # Quando fechar a janela de login, mostra a príncipal novamente
    janela_login.protocol("WM_DELETE_WINDOW", lambda: [janela_login.destroy(), janela.deiconify()])

    # Botão para confirmar login - Definido antes de ser usado
    def confirmar_login():
        email_login = entrada_email_login.get().strip()
        senha_login = entrada_senha_login.get().strip()
        if email_login == email_registrado and senha_login == senha_registrada:
            messagebox.showinfo("Sucesso!", f"Bem vindo(a) de volta, {nome_registrado}!")
            janela_login.destroy()
            janela.deiconify() # Mostra a janella principal novamente
        else:
            messagebox.showerror("Erro!", "Por favor, digite um nome ou senha já registrados.")

    # Frame para os campos de entrada 
    frame_campos_login = Frame(frame_principal)
    frame_campos_login.pack(fill="both", expand=True)

    # Label e Entry para o email e a senha
    Label(frame_campos_login, text="Email: ", font=fonte_botao).pack(pady=10)
    entrada_email_login = Entry(frame_campos_login)
    entrada_email_login.pack(pady=5, fill="x")

    Label(frame_campos_login, text="Senha: ", font=fonte_botao).pack(pady=10)
    entrada_senha_login = Entry(frame_campos_login, show="*")
    entrada_senha_login.pack(pady=5, fill="x")

    # Frame para os botões (Na parte inferior)
    frame_botoes_login = Frame(frame_principal)
    frame_botoes_login.pack(side="bottom", pady=20, fill="x")

    # Botão confirmar
    Button(frame_botoes_login, text="Confirmar", command=confirmar_login, font=fonte_botao).pack(side="left", padx=10, expand=True, fill="x")

    # Botão voltar 
    Button(frame_botoes_login, text="Voltar", command=lambda: [janela_login.destroy(), janela.deiconify()], font=fonte_botao).pack(side="right", padx=10, expand=True, fill="x")

# Criando fontes personalizadas
fonte_titulo = ("Arial", 14, "bold") # Fonte para o titulo
fonte_texto = ("Arial", 12) # Fonte para textos normais
fonte_botao = ("Arial", 12, "bold") # Fonte para os botões

# Criação da janela
janela = Tk() # Cria a janela 
janela.geometry("400x400") 
janela.title("Tela Inicial") # Define o título da janela

# Configurar a coluna 0 para expandir e centralizar
janela.columnconfigure(0, weight=1)

# Configuração da janela de cadastro do usuário
titulo_inicial = Label(janela, text="Inicio", font=fonte_titulo)
titulo_inicial.grid(column=0, row=0, pady=20)

# Texto de orientação
texto_orientacao = Label(janela, text="Escolha se você quer realizar um registro ou login", font=fonte_texto)
texto_orientacao.grid(column=0, row=1, pady=10)

# Botão de criação de perfil
botao_registro = Button(janela, text="Registro", command=criar_perfil, font=fonte_titulo, width=15) 
botao_registro.grid(column=0, row=2, pady=10)

# Botão de login em um perfil já existente
botao_login = Button(janela, text="Login", command=login_perfil, font=fonte_botao, width=15) 
botao_login.grid(column=0, row=3, pady=10)

texto_informações = Label(janela, text="Feito por: Matheus de Paula Azevedo", font=fonte_texto)
texto_informações.grid(column=0, row=4, pady=10)


# Finalizando o programa
janela.mainloop() # Exibe a janela e a mantem exibida sem fechar








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