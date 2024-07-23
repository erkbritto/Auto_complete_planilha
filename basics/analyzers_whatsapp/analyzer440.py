from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 122837e5b3d24ee6a20100869756b5ca

class Analyzer440 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 2):
            return False
    
        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Encontramos uma dificuldade em entender a sua solicitação. Vou transferir para um especialista. Por ")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 0',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'nao qualificado',
        }
    