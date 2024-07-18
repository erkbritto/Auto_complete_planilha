from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

MESSAGE_WELCOME = "Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 1106202437d0d050c0. ㅤ\nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."

class Analyzer3 :
    def isValid(self, messages: List[Message]) -> bool:
        
        if not (len(messages) == 2):
            return False

        if not ((messages[1]['sender'] == 'bot') and (messages[1]['message'].startswith("Seja bem-vindo(a) à Nio Digital!"))):
            return False

        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
