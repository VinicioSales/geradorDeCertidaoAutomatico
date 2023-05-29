import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Gerador de Certidão')
        self.attributes('-fullscreen', True)

        # Criar o frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.configure(width=500, height=500)

        # Obter a resolução da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular as coordenadas para o centro da tela
        center_x = (screen_width - self.main_frame.winfo_reqwidth()) // 2
        center_y = (screen_height - self.main_frame.winfo_reqheight()) // 2

        # Posicionar o frame principal no centro da tela
        self.main_frame.place(x=center_x, y=center_y)


if __name__ == '__main__':
    app = App()
    app.mainloop()
