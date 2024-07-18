from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# c0890c557a474679acfabf130c607db3
class Analyzer20:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 20):
            return False
        
        if not (messages[1]["sender"] == 'bot' and "Por favor, anote seu protocolo de atendimento" in messages[1]["message"]):
            return False
        
        if not (messages[3]["sender"] == 'bot' and "Em que posso ajudar?" in messages[3]["message"]):
            return False
        
        if not (messages[5]["sender"] == 'bot' and "Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o que deseja consultar." in messages[5]["message"]):
            return False
        
        if not (messages[7]["sender"] == 'bot' and "Te ajudo em algo mais?" in messages[7]["message"]):
            return False
        
        if not (messages[9]["sender"] == 'bot' and "Digite a op\u00e7\u00e3o desejada para" in messages[9]["message"]):
            return False
        
        if not (messages[11]["sender"] == 'bot' and "O seu c\u00f3digo de rastreio \u00e9 o" in messages[11]["message"]):
            return False
        
        if not (messages[13]["sender"] == 'bot' and "Tivemos um problema para entender sua solicita\u00e7\u00e3o" in messages[13]["message"]):
            return False
        
        if not (messages[15]["sender"] == 'bot' and "Seja bem-vindo(a) \u00e0 Nio Digital!" in messages[15]["message"]):
            return False
        
        if not (messages[17]["sender"] == 'bot' and "Em que posso ajudar?" in messages[17]["message"]):
            return False
        
        if not (messages[19]["sender"] == 'bot' and messages[0]["message"].startswith("*Digite a op\u00e7\u00e3o desejada para")):
            return False

        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return  {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou 4 opções do menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
