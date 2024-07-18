from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# a3436e09b33c4029838d7062445bf2bc
MESSAGE_WELCOME = "Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 14062024a3436e09b3. ㅤ\nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."
MESSAGE__CAN_I_HELP_YOU = "Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a sua fatura\n3 - Bloqueio, desbloqueio, 2ª via ou outras informações\n4 - Não reconhecimento de compras ou saques\n5 - Contestação de taxas\n6 - Elogio, sugestão ou reclamação\n7 - Atualização cadastral\n8 - Informações sobre entrega do cartão\n9 - Aplicativo Nio Digital\n10 - Problemas no Boleto/Pagamento da Fatura\n0 - Outros assuntos"

class Analyzer2 :

    def isValid(self, messages: List[Message]) -> bool:

        if not(len(messages) == 4):
            return False

        if not(messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!")):
            return False

        if not (messages[3]["sender"] == "bot" and messages[3]["message"].startswith("Ótimo. Em que posso ajudar?")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney":'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
