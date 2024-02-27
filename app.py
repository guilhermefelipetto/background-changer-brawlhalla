import os
import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.font import Font
from image_utils import verificar_tamanho, substituir_imagens

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Substituidor de Imagens by aimcold")

        self.diretorio_brawlhalla = None  # Variavel para pegar o diretorio do jogo
        
        self.root.geometry('500x300')  # Tamanho da janela

        # Proibe o usuario de aumentar a janela ou por em tela cheia
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', False)

        self.setup_ui()

    def setup_ui(self):
        # Botao para selecionar o diretorio do jogo
        self.btn_selecionar_diretorio = tk.Button(self.root, text="Selecionar Diretório do Jogo", command=self.selecionar_diretorio, width=25, height=1)
        self.btn_selecionar_diretorio.pack(pady=10)

        # Botao para selecionar a imagem
        self.selecao_btn = tk.Button(self.root, text="Selecionar Imagem", command=self.escolher_imagem, width=25, height=1)
        self.selecao_btn.pack()

        # Botao para abrir o tutorial
        self.btn_tutorial = tk.Button(self.root, text="Ver Tutorial", command=self.tutorial, width=25, height=1)
        self.btn_tutorial.pack(pady=10)

        # Label para exibir o texto 'teste'
        self.label_teste = tk.Label(self.root, text="Diretorio do jogo:")
        self.label_teste.pack(pady=10)

        # Text widget para exibir o caminho do diretório selecionado
        self.text_caminho = tk.Text(self.root, height=1, wrap='none')  # wrap='none' para desabilitar quebra de linha automática
        self.scrollbar_horizontal = tk.Scrollbar(self.root, orient='horizontal', command=self.text_caminho.xview)
        self.text_caminho.config(xscrollcommand=self.scrollbar_horizontal.set)
        self.text_caminho.pack(fill='x')
        self.scrollbar_horizontal.pack(fill='x')
        
    
    def tutorial(self):
        url_video = 'https://youtu.be/hdXtK3JhFes'
        webbrowser.open(url_video)
    
    def selecionar_diretorio(self):
        diretorio = filedialog.askdirectory(title='Selecione o diretório do Brawlhalla')
        if diretorio:
            self.diretorio_brawlhalla = os.path.join(diretorio, 'mapArt', 'Backgrounds')
            self.text_caminho.delete('1.0', tk.END)  # Limpa o texto existente
            self.text_caminho.insert('1.0', f"> {self.diretorio_brawlhalla}")
            self.selecao_btn['state'] = tk.NORMAL  # Habilita o botão de selecionar imagem

    def escolher_imagem(self):
        # Verifica que o diretorio do jogo foi definido
        if not self.diretorio_brawlhalla:
            messagebox.showerror('Erro', 'Por favor, selecione o diretorio do jogo primeiro.')
            return

        while True:  # Inicia um loop infinito
            imagem_substituta = filedialog.askopenfilename(
                title='Selecione a imagem',
                filetypes=(('JPEG files', '*.jpg'), ('JPEG files', '*.jpeg'), ('PNG files', '*.png'))
            )
            # Verifica se o usuario cancelou a selecao de arquivo
            if not imagem_substituta:  # Se nenhum arquivo foi selecionado (cancelado)
                break  # Sai do loop, encerrando a função sem fazer mais nada

            if verificar_tamanho(imagem_substituta):
                substituir_imagens(imagem_substituta, self.diretorio_brawlhalla)
                messagebox.showinfo("Concluído", "As imagens foram substituídas com sucesso.")
                break  # Sai do loop após a substituicao bem-sucedida
            else:
                resposta = messagebox.askyesno("Tamanho da imagem incorreto",
                                            "A imagem selecionada nao tem o tamanho preferido de 2048x1151. "
                                            "Deseja continuar mesmo assim?")
                if resposta:
                    substituir_imagens(imagem_substituta, self.diretorio_brawlhalla)
                    messagebox.showinfo("Concluído", "As imagens foram substituídas com sucesso.")
                    break  # Sai do loop apos a substituição bem-sucedida
                # Se o usuario clicar em "Nao", o loop continua, pedindo uma nova seleção de imagem


    def run(self):
        self.root.mainloop()