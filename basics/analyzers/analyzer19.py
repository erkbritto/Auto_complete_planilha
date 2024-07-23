from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 53c4cb462309486897ff27e012cf0a91
class Analyzer19:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 6):
            return False
        if not (messages[1]["sender"] == 'bot' and "Seja bem-vindo(a) à Nio Digital!" in messages[1]["message"]):
            return False
        if not (messages[3]["sender"] == 'bot' and "Digite a opção desejada para" in messages[3]["message"]):
            return False
        if not (messages[5]["sender"] == 'bot' and "Devido a um problema técnico na geração das faturas" in messages[5]["message"]):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 10',  # Aqui você pode completar conforme necessário
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Contato finalizado por falta de dados corretos',
        }
