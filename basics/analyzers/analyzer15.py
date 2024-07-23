from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 005713f499b24eb1a2091c482fe1bc9d

class Analyzer15:

    def isValid(self, messages: List[Message]) -> bool:
        if not(len(messages) == 16):
            return False
        
        # Corrigir as mensagens para refletir corretamente os exemplos fornecidos
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Desculpe não entendi.")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("Ótimo. Em que posso ajudar?")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("Por favor informe os 4 últimos dígitos")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and messages[7]["message"].startswith("*Tudo bem. Digite")):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[9]["message"].startswith("Aqui está a sua")):
            return False
        
        if not (messages[11]["sender"] == 'bot' and messages[11]["message"].startswith("*Digite a opção desejada para*")):
            return False
        
        if not (messages[13]["sender"] == 'bot' and messages[13]["message"].startswith("Por favor")):
            return False
        
        if not (messages[15]["sender"] == 'bot' and messages[15]["message"].startswith("*Tudo bem")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 3',
            "customerJourney": 'Selecionou 4 opções do menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
