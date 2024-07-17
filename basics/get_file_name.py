import os

def get_file_name() -> str:


    fileName:str = input("Caminho do arquivo: ")

    if not os.path.isfile(fileName):
        print(f"Arquivo '{fileName}' não encontrado.")
        exit(1)
        
    return fileName