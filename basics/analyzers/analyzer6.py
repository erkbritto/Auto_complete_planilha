from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# c3356bfc3ae543bd8af32adc27993d8b
class Analyzer6 :
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 4):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("N\u00e3o conseguimos localizar o CPF informado")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        
        isCPF = messages[2]["message"].isdigit() and len(messages[2]["message"]) == 11

        return {
            "selectedOption": 'CPF enviado incorretamente/Inexistente (Não localizado na Orbitall)' if isCPF else 'CPF enviado incorretamente (pontos e traços)',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'Contato finalizado por falta de dados corretos',
        }
