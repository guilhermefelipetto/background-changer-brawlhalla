from PIL import Image
import os
import shutil

def verificar_tamanho(imagem_path):
    with Image.open(imagem_path) as img:
        return img.size == (2048, 1151)


def substituir_imagens(imagem_substituta, diretorio):
    if os.path.exists(diretorio):
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            caminho_completo = os.path.join(diretorio, arquivo)
            if arquivo.endswith(('.jpg', '.jpeg', '.png')) and not arquivo == imagem_substituta:
                shutil.copy(imagem_substituta, caminho_completo)
    else:
        raise FileNotFoundError("Diretório não encontrado.")


def redimensionar_imagem(imagem_path, largura=2048, altura=1151):
    with Image.open(imagem_path) as img:
        img_redimensionada = img.resize((largura, altura), Image.Resampling.LANCZOS)
        img_redimensionada.save(imagem_path)
