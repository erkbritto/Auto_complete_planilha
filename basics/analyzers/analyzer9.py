from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification
#99a0a6113bc444df9f63114a500958ef
class Analyzer9:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 4):
            return False
        
        if not (messages[1]["sender"] == 'bot' and "Desculpe n\u00e3o entendi. Retornaremos para o in\u00edcio." in messages[1]["message"]):
            return False
        
        if not (messages[3]["sender"] == 'bot' and "N\u00e3o conseguimos localizar o CPF informado, digite-o novamente, mas apenas os n\u00fameros, ok?" in messages[3]["message"]):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
