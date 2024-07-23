import os

def process_files_in_directory(directory):
    # Lista todos os arquivos na pasta especificada
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Verifica se é um arquivo
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                # Lê todas as linhas do arquivo
                lines = file.readlines()
                
                # Verifica se o arquivo tem pelo menos 5 linhas
                if len(lines) >= 5:
                    # Obtém a quinta linha (índice 4)
                    fifth_line = lines[4].strip()
                    print(f"Arquivo: {filename} - Quinta linha: {fifth_line}")
                else:
                    print(f"Arquivo: {filename} - Não tem 5 linhas")

def main():
    # Define o diretório onde os arquivos estão localizados
    directory = 'basics/analyzers_whatsapp'
    
    # Chama a função para processar os arquivos no diretório
    process_files_in_directory(directory)

if __name__ == "__main__":
    main()
