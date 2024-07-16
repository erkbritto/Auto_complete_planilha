from typing import List, Any
import openpyxl

class HelperXlsx:
    def read(self, filename: str) -> List[Any]:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        data = []

        for row in sheet.iter_rows(values_only=True):
            data.append(row)

        return data

    def write(self, filename: str, data: List[Any]):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        for row in data:
            sheet.append(row)

        workbook.save(filename)

# Exemplo de uso:
# helper = HelperXlsx()
# data = helper.read('example.xlsx')
# helper.write('output.xlsx', data)
