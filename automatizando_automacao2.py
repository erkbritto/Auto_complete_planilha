import openpyxl
from create_script import createScripts

def main():
    workbook = openpyxl.load_workbook('output/file3.xlsx')  # json dos clientes
    sheet = workbook.active

    # Itera sobre as linhas da planilha
    for row in sheet.iter_rows(min_row=2, values_only=True):  # min_row=2 para pular o cabeçalho
        if row[16] is None:  
            interactionId = row[12] 
            createScripts(interactionId)
            break


if __name__ == "__main__":
    main()
