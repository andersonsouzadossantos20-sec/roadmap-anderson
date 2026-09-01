from pathlib import Path
import dpkt


#fazer a logica de ler e tratar erros
def pegar_arquivo(arquivo):
    if arquivo.is_file():
        f = open(arquivo, "rb")
        dados = dpkt.pcapng.Reader(f)
        print("arquivo lido com sucesso")
        return dados
    else:
        with open(arquivo, "rb") as ar:
            print("nao e uma url")
            return None
