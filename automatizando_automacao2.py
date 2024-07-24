import openpyxl
from create_script_user import createScripts

def main3():
    # Carrega o arquivo Excel
    workbook = openpyxl.load_workbook('output/file2.xlsx')  # json dos clientes
    sheet = workbook.active

    # Itera sobre as linhas da planilha
    for row in sheet.iter_rows(min_row=2, values_only=True):  # min_row=2 para pular o cabeçalho
        if row[16] is None:  # Verifica se a célula na coluna 17 está vazia
            interactionId = row[12]  # Extrai o interactionId da coluna 13
            createScripts(interactionId)  # Gera o script de analisador
            break  # Interrompe o loop após processar a primeira linha que atende à condição

if __name__ == "__main__":
    main3()
