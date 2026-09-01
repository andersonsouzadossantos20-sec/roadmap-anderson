from leitor import pegar_arquivo
from pathlib import Path
from unpacket import desempacotar
import time

caminho = input("url ou arquivo? ")
arquivo = Path(caminho)

def app(arquivo):
   dados_lido = pegar_arquivo(arquivo)
   desempacotar(dados_lido) 

if __name__ == "__main__":
    app(arquivo)
