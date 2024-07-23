from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 96f976b9034a4e2bb5405a6a15ee9a59

class Analyzer168 :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 2):
            return False
    
        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Olá Encontramos uma dificuldade em entender a sua solicitação. Vou transferir para um especialista. ")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": 'nao qualificado',
        }
    