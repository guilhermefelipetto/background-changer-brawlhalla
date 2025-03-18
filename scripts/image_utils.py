from PIL import Image
import os
import shutil
import tempfile

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
        temp_dir = tempfile.mkdtemp()
        temp_image_path = os.path.join(temp_dir, os.path.basename(imagem_path))
        img_redimensionada = img.resize((largura, altura), Image.Resampling.LANCZOS)
        img_redimensionada.save(temp_image_path)
        return temp_image_path

def restaurar_imagens_originais(dir_backgrounds, dir_backgrounds_originais):
    if not os.path.isdir(dir_backgrounds):
        raise FileNotFoundError("Pasta de backgrounds não encontrada.")
    
    # Exclui todas as imagens na pasta de backgrounds
    for item in os.listdir(dir_backgrounds):
        caminho_item = os.path.join(dir_backgrounds, item)
        if os.path.isfile(caminho_item) and item.endswith(('.jpg', '.jpeg', '.png')):
            os.remove(caminho_item)
    
    # Copia todas as imagens da nova pasta para a pasta de backgrounds
    for item in os.listdir(dir_backgrounds_originais):
        caminho_item_origem = os.path.join(dir_backgrounds_originais, item)
        caminho_item_destino = os.path.join(dir_backgrounds, item)
        if os.path.isfile(caminho_item_origem):
            shutil.copy(caminho_item_origem, caminho_item_destino)
