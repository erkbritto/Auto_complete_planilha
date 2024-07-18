from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 28983256acce45cc9527fee959a3539d
class Analyzer14:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 5):
            return False
        
        if not (messages[1]["sender"] == 'bot' and "Por favor, anote seu protocolo de atendimento" in messages[1]["message"]):
            return False
        
        if not (messages[3]["sender"] == 'bot' and "Digite a op\u00e7\u00e3o desejada para" in messages[3]["message"]):
            return False
        
        
        if not (messages[4]["sender"] == 'bot' and messages[0]["message"].startswith("Devido a um problema t\u00e9cnico na gera\u00e7\u00e3o das faturas, estamos excepcionalmente recebendo os pagamentos via PIX.\n\nChave PIX: 11.460.609/0001-60 \nNio Meios de Pagamento\n\nImportante: Obrigat\u00f3rio inserir no campo observa\u00e7\u00e3o do PIX o CPF do titular do cart\u00e3o.\n\nOriente o cliente a enviar o comprovante de pagamento, nome completo e CPF para o e-mail: comprovantes@niodigital.com.br.\n\nPrazo para baixa do pagamento em at\u00e9 3 dias \u00fateis, mesmo sendo realizado\u00a0via\u00a0PIX.\n.\n. \u3164\nTe ajudo em algo mais? (Sim ou N\u00e3o)")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 10',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
