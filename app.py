import os
import shutil
import string
import tkinter as tk
import tkinter.ttk as tkk
import webbrowser
from tkinter import colorchooser, filedialog, messagebox

from PIL import Image, ImageTk

from scripts.image_utils import (redimensionar_imagem,
                                 restaurar_imagens_originais,
                                 substituir_imagens, verificar_tamanho)


class App:
    def __init__(self):
        # pre-inicializacao
        self.root = tk.Tk()
        self.root.title("Substituidor de Imagens by aimcold")
        self.detected_color = None
        self.selected_color = None

        self.root.geometry('1000x320')  
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', False)

        # inicializacao
        self.setup_ui()
        
        # pos-inicializacao
        self.diretorio_brawlhalla = self.buscar_diretorio_jogo()

    def setup_ui(self):
        # Notebook para abas
        self.notebook = tkk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Frames para abas diferentes
        self.frame_background = tk.Frame(self.notebook)
        self.frame_stage = tk.Frame(self.notebook)

        # Adicionando as abas ao notebook
        self.notebook.add(self.frame_background, text='Backgrounds')
        self.notebook.add(self.frame_stage, text='Stages')

        # ------------------------------ #
        # --- CODIGO ABA BACKGROUNDS --- #
        # ------------------------------ #

        # Frame para os botões à esquerda
        self.frame_botoes_backgrounds = tk.Frame(self.frame_background)
        self.frame_botoes_backgrounds.pack(side='left', fill='y')

        self.btn_selecionar_diretorio = tk.Button(self.frame_botoes_backgrounds, text="Buscar diretório do jogo", command=self.buscar_diretorio_jogo, width=25, height=1)
        self.btn_selecionar_diretorio.pack(pady=10)

        self.selecao_btn = tk.Button(self.frame_botoes_backgrounds, text='Selecionar Imagem', command=self.escolher_imagem, width=25, height=1)
        self.selecao_btn.pack()

        self.btn_tutorial = tk.Button(self.frame_botoes_backgrounds, text='Ver Tutorial', command=self.tutorial, width=25, height=1)
        self.btn_tutorial.pack(pady=10)

        self.opcao_redimensionar = tk.BooleanVar()
        self.checkbox_redimensionar = tk.Checkbutton(self.frame_botoes_backgrounds, text='Redimensionar antes de substituir', variable=self.opcao_redimensionar, onvalue=True, offvalue=False)
        self.checkbox_redimensionar.pack()

        self.btn_substituir = tk.Button(self.frame_botoes_backgrounds, text='Substituir Imagens', command=self.comando_substituir_imagens_com_opcao, width=25, height=1)
        self.btn_substituir.pack(pady=10)

        self.label_dir = tk.Label(self.frame_botoes_backgrounds, text='Diretorio do jogo:')
        self.label_dir.pack()

        self.text_caminho = tk.Text(self.frame_botoes_backgrounds, height=1, wrap='none')
        self.scrollbar_horizontal = tk.Scrollbar(self.frame_botoes_backgrounds, orient='horizontal', command=self.text_caminho.xview)
        self.text_caminho.config(xscrollcommand=self.scrollbar_horizontal.set)
        self.text_caminho.pack(fill='x')
        self.scrollbar_horizontal.pack(fill='x')

        self.btn_restaurar_img = tk.Button(self.frame_botoes_backgrounds, text='Restaurar Imagens Originais', command=self.restaurar_imagens_originais, width=25, height=1)
        self.btn_restaurar_img.pack(pady=10)

        # Frame para a imagem à direita
        self.frame_imagem = tk.Frame(self.frame_background)
        self.frame_imagem.pack(side='right', fill='both', expand=True)

        self.img_preview_label = tk.Label(self.frame_imagem, text='Preview do Background:')
        self.img_preview_label.pack()

        self.label_imagem = tk.Label(self.frame_imagem)
        self.label_imagem.pack()

        # ------------------------- #
        # --- CODIGO ABA STAGES --- #
        # ------------------------- #

        # Forçar a seleção inicial da aba "Backgrounds"
        self.notebook.select(self.frame_background)
        
        # Frame to the buttons on the left
        self.frame_botoes_stage = tk.Frame(self.frame_stage)
        self.frame_botoes_stage.pack(side='left', fill='y')
        
        # Button to restore original stages
        self.btn_restore_stages = tk.Button(self.frame_botoes_stage, text="Restore Original Stages", command=self.restaurar_imagens_originais, width=25, height=1)
        self.btn_restore_stages.pack(pady=10)
        
        self.target_color_label = tk.Label(self.frame_botoes_stage, text="Nenhuma Cor Detectada", width=25)
        self.target_color_label.pack(pady=10)
        
    # ------------------------ #
    # Metodos para Backgrounds #
    # ------------------------ #
    
    def buscar_diretorio_jogo(self):
        letras_unidade = (letra for letra in string.ascii_uppercase if letra >= 'C')

        possiveis_caminhos = [
            'Program Files (x86)\\Steam\\steamapps\\common\\Brawlhalla\\mapArt\\Backgrounds',
            'SteamLibrary\\steamapps\\common\\Brawlhalla\\mapArt\\Backgrounds'
        ]

        for letra_unidade in letras_unidade:
            for caminho in possiveis_caminhos:
                caminho_completo = f'{letra_unidade}:\\{caminho}'
                if os.path.exists(caminho_completo):
                    self.diretorio_brawlhalla = caminho_completo
                    self.atualizar_interface_apos_selecao_background()
                    self.selecao_btn['state'] = 'normal'
                    return self.diretorio_brawlhalla

        messagebox.showwarning('Atenção', 'Não foi possível encontrar o diretório do jogo automaticamente.')

        self.btn_selecionar_diretorio['state'] = 'normal'

    def atualizar_interface_apos_selecao_background(self):
        if self.diretorio_brawlhalla:
            self.btn_selecionar_diretorio['state'] = 'disabled'
            self.text_caminho['state'] = 'normal'  
            self.text_caminho.delete('1.0', tk.END)  
            self.text_caminho.insert('1.0', f'> {self.diretorio_brawlhalla}')
            self.text_caminho['state'] = 'disabled'  
            self.selecao_btn['state'] = 'normal'
        
    def tutorial(self):
        url_video = 'https://youtu.be/nzBUVY051dA'
        webbrowser.open(url_video)
        
        self.text_caminho.delete('1.0', tk.END)  
        self.text_caminho.insert('1.0', f'> {self.diretorio_brawlhalla}')
        self.selecao_btn['state'] = tk.NORMAL

    def escolher_imagem(self):
        if not self.diretorio_brawlhalla:
            messagebox.showerror('Erro', 'Por favor, selecione o diretorio do jogo primeiro.')
            print(self.diretorio_brawlhalla)
            return

        while True:  
            imagem_substituta = filedialog.askopenfilename(
                title='Selecione a imagem',
                filetypes=(('JPEG files', '*.jpg'), ('JPEG files', '*.jpeg'), ('PNG files', '*.png'))
            )
            if not imagem_substituta:
                break

            try:
                img = Image.open(imagem_substituta)
                img.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(img)
                self.label_imagem.config(image=photo)
                self.label_imagem.image = photo

                self.imagem_selecionada = imagem_substituta
                self.btn_substituir['state'] = 'normal'

                if not verificar_tamanho(imagem_substituta):
                    resposta = messagebox.askyesno("Tamanho da imagem incorreto",
                                                "A imagem selecionada nao tem o tamanho preferido de 2048x1151. "
                                                "Deseja continuar mesmo assim?")
                    if not resposta:
                        self.imagem_selecionada = None
                        self.btn_substituir['state'] = 'disabled'
                        return

                messagebox.showinfo('Imagem Selecionada', 'A imagem foi carregada com sucesso.')
                break

            except Exception as e:
                messagebox.showerror('Erro', f'Falha ao carregar imagem: {e}')
                
    def comando_substituir_imagens_com_opcao(self):
        imagem_para_substituir = None

        if self.opcao_redimensionar.get() and hasattr(self, 'imagem_selecionada') and self.imagem_selecionada:
            try:
                temp_image_path = redimensionar_imagem(self.imagem_selecionada)
                imagem_para_substituir = temp_image_path
            except Exception as e:
                messagebox.showerror('Erro', f'Falha ao redimensionar imagem: {e}')
                return
        elif hasattr(self, 'imagem_selecionada') and self.imagem_selecionada:
            imagem_para_substituir = self.imagem_selecionada

        if imagem_para_substituir and self.diretorio_brawlhalla:
            try:
                substituir_imagens(imagem_para_substituir, self.diretorio_brawlhalla)
                if self.opcao_redimensionar.get():
                    shutil.rmtree(os.path.dirname(imagem_para_substituir))
                messagebox.showinfo('Concluído', 'As imagens foram substituídas com sucesso.')
            except Exception as e:
                messagebox.showerror('Erro', f'Falha ao substituir imagens: {e}')
        else:
            messagebox.showerror('Erro', 'Operação Inválida. Verifique se a imagem foi selecionada e o diretório do jogo definido.')
    
    def restaurar_imagens_originais(self):
        if not self.diretorio_brawlhalla:
            messagebox.showwarning('Aviso', 'Por favor, busque o diretório do jogo antes de restaurar os backgrounds.')
            return

        try:
            dir_backgrounds_originais = 'original_backgrounds'
            restaurar_imagens_originais(self.diretorio_brawlhalla, dir_backgrounds_originais)
            messagebox.showinfo('Concluído', 'Imagens restauradas com sucesso.')
        except Exception as e:
            messagebox.showerror('Erro', str(e))

    def run(self):
        self.root.mainloop()
