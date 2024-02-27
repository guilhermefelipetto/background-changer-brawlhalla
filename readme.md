# Background Changer - Brawlhalla

Background Changer para o Brawlhalla é um app simples desenvolvido em Python para automatizar a alteração do background dos mapas.

Nota: Você precisa ter o Python instalado e configurado na sua máquina!

## Configuração do Ambiente de Desenvolvimento

Para rodar este projeto localmente, você precisa seguir estes passos:

### 1. Clonar o Repositório

Primeiro, clone o repositório do projeto para a sua máquina local usando:

```bash
git clone https://github.com/guilhermefelipetto/background_changer_brawlhalla
cd background_changer_brawlhalla
```

### 2. Dentro do repositório, abra o terminal para criar um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

```bash
.\.venv\Scripts\activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Gere o arquivo executável da aplicação
```bash
pyinstaller --onefile -w main.py
```

### 6. Procure a pasta 'dist' no diretório 'background_changer_brawlhalla', nela contém o main.exe, o executável da sua aplicação
