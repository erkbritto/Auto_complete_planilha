from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 005713f499b24eb1a2091c482fe1bc9d
class Analyzer15:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 16):
            return False
        
        # Verificar o protocolo de atendimento e o CPF
        if not (messages[1]["sender"] == 'bot' and "Por favor, anote seu protocolo de atendimento" in messages[1]["message"]):
            return False
        
        if not (messages[3]["sender"] == 'bot' and "Digite a op\u00e7\u00e3o desejada para" in messages[3]["message"]):
            return False
        
        if not (messages[5]["sender"] == 'bot' and "Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o que deseja consultar." in messages[6]["message"]):
            return False
        
        if not (messages[7]["sender"] == 'bot' and "Aqui est\u00e1 a sua \u00faltima fatura dispon\u00edvel" in messages[8]["message"]):
            return False
        
        if not (messages[9]["sender"] == 'bot' and "Digite a op\u00e7\u00e3o desejada para" in messages[10]["message"]):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[0]["message"].startswith("*Tudo bem. Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Valor m\u00ednimo da fatura\n2 - \u00daltimas transa\u00e7\u00f5es\n3 - Segunda via da fatura\n4 - Informa\u00e7\u00e3o de pagamento\n5 - Diverg\u00eancia no valor do desconto em folha\n0 - Retornar ao menu anterior")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 3 opções do menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
