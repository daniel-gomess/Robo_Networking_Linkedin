import customtkinter as ctk
from tkinter import messagebox
from app import login_linkedin, buscar_e_conectar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criar janela principal
login = ctk.CTk()
login.title('Login do LinkedIn')
login.geometry('500x400')

# Elementos da interface
label_email = ctk.CTkLabel(login, text="Email")
label_email.pack(pady=10)
campo_email = ctk.CTkEntry(login, placeholder_text="Digite seu email do LinkedIn", width=300)
campo_email.pack(pady=5)

label_senha = ctk.CTkLabel(login, text="Senha")
label_senha.pack(pady=10)
campo_senha = ctk.CTkEntry(login, placeholder_text="Digite sua senha do LinkedIn", show='*', width=300)
campo_senha.pack(pady=5)

label_termo = ctk.CTkLabel(login, text="Termo de Pesquisa")
label_termo.pack(pady=10)
campo_termo = ctk.CTkEntry(login, placeholder_text="Ex: Desenvolvedor Python", width=300)
campo_termo.pack(pady=5)

# Função de login
def ao_clicar_login(event=None):
    email_usuario = campo_email.get()
    senha_usuario = campo_senha.get()
    termo_busca = campo_termo.get()

    if email_usuario and senha_usuario and termo_busca:
        try:
            driver, wait = login_linkedin(email_usuario, senha_usuario)
            if driver:
                login.destroy()  # Fecha a interface gráfica
                buscar_e_conectar(driver, wait, termo_busca)
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao realizar login:\n{e}")
    else:
        messagebox.showwarning("Campos obrigatórios", "⚠️ Por favor, preencha todos os campos.")

# Botão de login
botao_login = ctk.CTkButton(login, text="Login", command=ao_clicar_login)
botao_login.pack(pady=15)

# Atalho para tecla ENTER
login.bind('<Return>', ao_clicar_login)

# Iniciar interface
login.mainloop()
