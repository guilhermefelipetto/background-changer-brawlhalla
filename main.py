import tempfile
import atexit
import os

from app import App

def main():
    diretorio_temporario = tempfile.mkdtemp()

    app = App()
    app.run()

    atexit.register(limpar_diretorio_temporario, diretorio_temporario)


def limpar_diretorio_temporario(diretorio_temporario):
    for arquivo in os.listdir(diretorio_temporario):
        caminho_arquivo = os.path.join(diretorio_temporario, arquivo)
        os.remove(caminho_arquivo)


if __name__ == '__main__':
    main()
