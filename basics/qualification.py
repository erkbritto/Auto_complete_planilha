from typing import TypedDict
from typing import Literal

FinalizationOfTheContract = Literal[
    'Contato encerrado com script de finalização.',
    'Contato finalizado por falta de dados corretos',
    'Sem interação - Sem resposta do cliente',
]

class Qualification(TypedDict):

    selectedOption:Literal[
        'Opção 0',
        'Opção 1',
        'Opção 2',
        'Opção 3',
        'Opção 4',
        'Opção 5',
        'Opção 6',
        'Opção 7',
        'Opção 8',
        'Opção 9',
        'Opção 10',
        'Sem opção selecionada',
        'CPF enviado incorretamente/Inexistente (Não localizado na Orbitall)',
        'CPF enviado incorretamente (pontos e traços)',
    ]

    customerJourney:Literal[
        'Sem opções selecionadas',
        'Selecionou apenas 1 opção',
        'Selecionou 2 opções do menu',
        'Selecionou 3 opções do menu',
        'Selecionou 4 opções do menu',
        'Selecionou 5 opções do menu',
        'Selecionou 6 opções do menu',
        'Selecionou 7 opções do menu',
        'Acima de 8 opções no menu',
    ]

    finalizationOfTheContract:FinalizationOfTheContract
