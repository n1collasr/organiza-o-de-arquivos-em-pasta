import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='selecione uma pasta')

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais = {
    'imagens': [".png", ".jpg"],
    "musicas": [".mp3"],
    "documentos": [".pdf", ".rar", ".txt" ".bmp"]
}

for arquiuvo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{arquiuvo}/{arquiuvo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquiuvo}", f"{caminho}/{pasta}/{arquiuvo}")