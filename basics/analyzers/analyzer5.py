from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 371cc4ed5af147a8854ff0ac955f70e4
class Analyzer5 :
    
    def isValid(self, messages: List[Message]) -> bool:
        
        if not (len(messages) == 14):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and "Tudo bem. Digite a op\u00e7\u00e3o desejada para" in messages[7]["message"]):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[9]["message"].startswith("J\u00e1 faz mais de 5 dias que efetuou o pagamento da fatura?")):
            return False
        
        if not (messages[11]["sender"] == 'bot' and messages[11]["message"].startswith("Nesse caso, voc\u00ea dever\u00e1 aguardar")):
            return False
        
        if not (messages[13]["sender"] == 'bot' and messages[13]["message"].startswith("Tudo bem!\nNio Digital agradece e at\u00e9 logo!")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'Contato encerrado com script de finalização.',
        }
        
        
messages = [
        {
            "sender": "client",
            "message": "Oi"
        },
        {
            "sender": "bot",
            "message": "Seja bem-vindo(a) \u00e0 Nio Digital!\n\nSou o Al\u00ea, seu assistente virtual.\n\nPara obter informa\u00e7\u00f5es sobre os assuntos abaixo: \n\n- Adquirir o Cart\u00e3o Nio\n- Consultar o status da sua proposta\n- Informa\u00e7\u00f5es sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- \u00d3rg\u00e3os/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se voc\u00ea j\u00e1 \u00e9 cliente NIO Digital e deseja informa\u00e7\u00f5es sobre o seu Cart\u00e3o de Cr\u00e9dito Consignado, nosso hor\u00e1rio de atendimento com especialistas \u00e9 de segunda a sexta-feira, das 8h \u00e0s 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 13062024371cc4ed5a. \u3164\nPara iniciarmos seu atendimento, por favor informe o n\u00famero do seu CPF. (apenas n\u00fameros)."
        },
        {
            "sender": "client",
            "message": "01105764460"
        },
        {
            "sender": "bot",
            "message": "\u00d3timo. Em que posso ajudar?\n\u3164 *Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Limite dispon\u00edvel para utiliza\u00e7\u00e3o\n2 - Informa\u00e7\u00f5es sobre a sua fatura\n3 - Bloqueio, desbloqueio, 2\u00aa via ou outras informa\u00e7\u00f5es\n4 - N\u00e3o reconhecimento de compras ou saques\n5 - Contesta\u00e7\u00e3o de taxas\n6 - Elogio, sugest\u00e3o ou reclama\u00e7\u00e3o\n7 - Atualiza\u00e7\u00e3o cadastral\n8 - Informa\u00e7\u00f5es sobre entrega do cart\u00e3o\n9 - Aplicativo Nio Digital\n10 - Problemas no Boleto/Pagamento da Fatura\n0 - Outros assuntos"
        },
        {
            "sender": "client",
            "message": "2"
        },
        {
            "sender": "bot",
            "message": "Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o que deseja consultar."
        },
        {
            "sender": "client",
            "message": "3925"
        },
        {
            "sender": "bot",
            "message": "*Tudo bem. Digite a op\u00e7\u00e3o desejada para*:\n\n1 - Valor m\u00ednimo da fatura\n2 - \u00daltimas transa\u00e7\u00f5es\n3 - Segunda via da fatura\n4 - Informa\u00e7\u00e3o de pagamento\n5 - Diverg\u00eancia no valor do desconto em folha\n0 - Retornar ao menu anterior"
        },
        {
            "sender": "client",
            "message": "4"
        },
        {
            "sender": "bot",
            "message": "J\u00e1 faz mais de 5 dias que efetuou o pagamento da fatura? (Sim ou N\u00e3o)\u3164"
        },
        {
            "sender": "client",
            "message": "N"
        },
        {
            "sender": "bot",
            "message": "Nesse caso, voc\u00ea dever\u00e1 aguardar a compensa\u00e7\u00e3o banc\u00e1ria de 3 a 5 dias \u00fateis. \u3164\nTe ajudo em algo mais? (Sim ou N\u00e3o)"
        },
        {
            "sender": "client",
            "message": "N"
        },
        {
            "sender": "bot",
            "message": "Tudo bem!\nNio Digital agradece e at\u00e9 logo!"
        }
    ]