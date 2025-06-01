import customtkinter as ctk
from app import login_linkedin, buscar_e_conectar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LinkedIn - Networking")
        self.geometry("400x600")

        self.label_email = ctk.CTkLabel(self, text="Email")
        self.label_email.pack(pady=2)
        self.entry_email = ctk.CTkEntry(self, width=300)
        self.entry_email.pack(pady=2)

        self.label_senha = ctk.CTkLabel(self, text="Senha")
        self.label_senha.pack(pady=2)
        self.entry_senha = ctk.CTkEntry(self, show="*", width=300)
        self.entry_senha.pack(pady=2)

        self.label_termo = ctk.CTkLabel(self, text="Termo de Pesquisa")
        self.label_termo.pack(pady=2)
        self.entry_termo = ctk.CTkEntry(self, width=300)
        self.entry_termo.pack(pady=2)

        self.button_iniciar = ctk.CTkButton(self, text="Iniciar Conexões", command=self.iniciar_conexoes)
        self.button_iniciar.pack(pady=20)

        self.textbox_log = ctk.CTkTextbox(self, width=350, height=300)
        self.textbox_log.pack(pady=10)

    def log(self, mensagem):
        self.textbox_log.insert("end", mensagem + "\n")
        self.textbox_log.see("end")
        self.update()

    def iniciar_conexoes(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        termo = self.entry_termo.get()

        if email and senha and termo:
            driver, wait = login_linkedin(email, senha, self.log)
            if driver and wait:
                buscar_e_conectar(driver, wait, termo, self.log, limite_conexoes=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
