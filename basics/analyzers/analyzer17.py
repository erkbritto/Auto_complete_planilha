from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# d935804cff1640dcb6a1393dffaa4fce
class Analyzer17:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 10):
            return False        
        if not (messages[1]["sender"] == 'bot' and "Seja bem-vindo(a) à Nio Digital!" in messages[1]["message"]):
            return False
        if not (messages[3]["sender"] == 'bot' and "Digite a opção desejada para:" in messages[3]["message"]):
            return False
        if not (messages[5]["sender"] == 'bot' and "Por favor informe os 4 últimos dígitos do cartão que deseja consultar." in messages[5]["message"]):
            return False
        if not (messages[7]["sender"] == 'bot' and "Seguem as informações solicitadas:" in messages[7]["message"]):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        # Aqui você pode implementar a lógica para extrair qualificações com base nas mensagens
        return {
            "selectedOption": 'Opção 1',  # Exemplo: Aqui estou assumindo que a opção selecionada foi enviada pelo cliente
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
