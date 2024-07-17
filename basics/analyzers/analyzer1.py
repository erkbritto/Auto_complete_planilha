from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

MESSAGE_SORRY_START = "Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 14062024808a565334. ㅤ\nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."
MESSAGE_NOT_FOUND_CPF1 = "Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?"
MESSAGE_NOT_FOUND_CPF2 = "Que pena, mas não consegui localizar o CPF informado, peço que confirme a infirmação e nos contacte novamente, ok?\nNio Digital agradece, até logo!"

class Analyzer1 :
    def isValid(self, messages: List[Message]) -> bool:
        
        return len(messages) == 6 and (messages[1]["message"] == MESSAGE_SORRY_START) and (messages[3]["message"] == MESSAGE_NOT_FOUND_CPF1) and (messages[5]["message"] == MESSAGE_NOT_FOUND_CPF2)

    def getQualifications(self, messages: List[Message]) -> Qualification:
        isCPF = messages[4]["message"].isdigit() and len(messages[4]["message"]) == 11
        return {
            "selectedOption": 'CPF enviado incorretamente/Inexistente (Não localizado na Orbitall' if isCPF else 'CPF enviado incorretamente (pontos e traços)',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'Contato finalizado por falta de dados corretos',
        }
