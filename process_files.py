import os
import re
from data import data

def extract_numbers(input_string):
    # Usa regex para encontrar todos os números na string
    numbers = re.findall(r'\d+', input_string)
    # Converte os números encontrados para inteiros
    numbers = [int(num) for num in numbers]
    return numbers[0]

def updateContent(file_name, content):
    id = content.split("\n")[4].split(" ")[1]
    # Atualiza o conteúdo do arquivo
    content = content.replace("\"selectedOption\": '',", f"\"selectedOption\": '{data[id][0]}',")
    content = content.replace("\"customerJourney\": '',", f"\"customerJourney\": '{data[id][1]}',")
    return content

def process_files(directory):
    # Itera sobre todos os arquivos no diretório especificado
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        # Verifica se é um arquivo (não um diretório)
        if os.path.isfile(file_path):
            # Lê o conteúdo do arquivo
            with open(file_path, 'r') as file:
                content = file.read()
            
            # Atualiza o conteúdo usando a função updateContent
            updated_content = updateContent(file_name, content)
            
            # Sobrescreve o conteúdo original com o conteúdo atualizado
            with open(file_path, 'w') as file:
                file.write(updated_content)
            # print(f"Arquivo {file_name} foi atualizado com sucesso.")

if __name__ == "__main__":
    # Diretório que contém os arquivos a serem processados
    directory_path = 'basics/analyzers_whatsapp'
    process_files(directory_path)
