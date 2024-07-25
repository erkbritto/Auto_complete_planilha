from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 6e5b790644aa42fb91305ad4b2f68728

class Analyzer105 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 168):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[21]["sender"] == "bot" and messagesClient[21]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[23]["sender"] == "bot" and messagesClient[23]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[25]["sender"] == "bot" and messagesClient[25]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[27]["sender"] == "bot" and messagesClient[27]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[29]["sender"] == "bot" and messagesClient[29]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[31]["sender"] == "bot" and messagesClient[31]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[33]["sender"] == "bot" and messagesClient[33]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[35]["sender"] == "bot" and messagesClient[35]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[37]["sender"] == "bot" and messagesClient[37]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[39]["sender"] == "bot" and messagesClient[39]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[41]["sender"] == "bot" and messagesClient[41]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[43]["sender"] == "bot" and messagesClient[43]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[45]["sender"] == "bot" and messagesClient[45]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[47]["sender"] == "bot" and messagesClient[47]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[49]["sender"] == "bot" and messagesClient[49]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[51]["sender"] == "bot" and messagesClient[51]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[53]["sender"] == "bot" and messagesClient[53]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[55]["sender"] == "bot" and messagesClient[55]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[57]["sender"] == "bot" and messagesClient[57]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[59]["sender"] == "bot" and messagesClient[59]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[61]["sender"] == "bot" and messagesClient[61]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[63]["sender"] == "bot" and messagesClient[63]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[65]["sender"] == "bot" and messagesClient[65]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[67]["sender"] == "bot" and messagesClient[67]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[69]["sender"] == "bot" and messagesClient[69]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[71]["sender"] == "bot" and messagesClient[71]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[73]["sender"] == "bot" and messagesClient[73]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[75]["sender"] == "bot" and messagesClient[75]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[77]["sender"] == "bot" and messagesClient[77]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[79]["sender"] == "bot" and messagesClient[79]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[81]["sender"] == "bot" and messagesClient[81]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[83]["sender"] == "bot" and messagesClient[83]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[85]["sender"] == "bot" and messagesClient[85]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[87]["sender"] == "bot" and messagesClient[87]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[89]["sender"] == "bot" and messagesClient[89]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[91]["sender"] == "bot" and messagesClient[91]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[93]["sender"] == "bot" and messagesClient[93]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[95]["sender"] == "bot" and messagesClient[95]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[97]["sender"] == "bot" and messagesClient[97]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[99]["sender"] == "bot" and messagesClient[99]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[101]["sender"] == "bot" and messagesClient[101]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[103]["sender"] == "bot" and messagesClient[103]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesClient[105]["sender"] == "bot" and messagesClient[105]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[107]["sender"] == "bot" and messagesClient[107]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesClient[109]["sender"] == "bot" and messagesClient[109]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[111]["sender"] == "bot" and messagesClient[111]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[113]["sender"] == "bot" and messagesClient[113]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[115]["sender"] == "bot" and messagesClient[115]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[117]["sender"] == "bot" and messagesClient[117]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[119]["sender"] == "bot" and messagesClient[119]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[121]["sender"] == "bot" and messagesClient[121]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[123]["sender"] == "bot" and messagesClient[123]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[125]["sender"] == "bot" and messagesClient[125]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[127]["sender"] == "bot" and messagesClient[127]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[129]["sender"] == "bot" and messagesClient[129]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[131]["sender"] == "bot" and messagesClient[131]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[133]["sender"] == "bot" and messagesClient[133]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[135]["sender"] == "bot" and messagesClient[135]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[137]["sender"] == "bot" and messagesClient[137]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[139]["sender"] == "bot" and messagesClient[139]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[141]["sender"] == "bot" and messagesClient[141]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[143]["sender"] == "bot" and messagesClient[143]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[145]["sender"] == "bot" and messagesClient[145]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[147]["sender"] == "bot" and messagesClient[147]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[149]["sender"] == "bot" and messagesClient[149]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[151]["sender"] == "bot" and messagesClient[151]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[153]["sender"] == "bot" and messagesClient[153]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a su")):
            return False
    
        if not (messagesClient[155]["sender"] == "bot" and messagesClient[155]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[157]["sender"] == "bot" and messagesClient[157]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[159]["sender"] == "bot" and messagesClient[159]["message"].startswith("Devido a um problema técnico na geração das faturas, estamos excepcionalmente recebendo os pagamento")):
            return False
    
        if not (messagesClient[161]["sender"] == "bot" and messagesClient[161]["message"].startswith("Tivemos um problema para entender sua solicitação por favor tente novamente")):
            return False
    
        if not (messagesClient[163]["sender"] == "bot" and messagesClient[163]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[165]["sender"] == "bot" and messagesClient[165]["message"].startswith("Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?")):
            return False
    
        if not (messagesClient[167]["sender"] == "bot" and messagesClient[167]["message"].startswith("Que pena, mas não consegui localizar o CPF informado, peço que confirme a infirmação e nos contacte ")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": 'Opção 10',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Contato encerrado com script de finalização.',
        }
    