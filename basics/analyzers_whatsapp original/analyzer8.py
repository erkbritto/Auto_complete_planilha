from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# e5f4ad28459e49bb82d639f180c683ac

class Analyzer8 :
    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == 2):
            return False

        if not (messagesBot[1]["sender"] == "bot" and messagesBot[1]["message"].startswith("Desculpe n\u00e3o entendi. Retornaremos para o in\u00edcio.")):
            return False

        return True

    def getQualifications(
            self,
            messagesBot: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'nao qualificado',
        }
