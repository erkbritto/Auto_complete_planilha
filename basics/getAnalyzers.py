from typing import List  # Importa o tipo List para anotações de tipo
from basics.analyzers.analizer1 import Analyzer1  # Importa a classe Analyzer1 do módulo especificado

def getAnalyzers() -> List[Analyzer1]:  # Define a função que retorna uma lista de instâncias de Analyzer1
    return [
        Analyzer1()  # Cria uma instância de Analyzer1 e a adiciona à lista
    ]
