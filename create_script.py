import os
from basics.find_ticket_in_json import find_ticket_in_json
from gerar_get_analyzers import gerar_get_analyzers

# Função para gerar o código Python
def generate_code(interactionId, messages, numeroAnalyzer):
    code = f'''from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# {interactionId}

class Analyzer{numeroAnalyzer} :

    def isValid(
        self,
        messagesBot: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesBot) == {len(messages)}):
            return False
    '''

    for i, message in enumerate(messages):
        if message['sender'] == 'bot':
            text = message['message'].replace("\n", "\\n")
            condition = f'''
        if not (messagesBot[{i}]["sender"] == "bot" and messagesBot[{i}]["message"].startswith("{((text[:100] if not text.startswith("Por favor aguarde um instante enquanto processamos sua solicitação.") else "Por favor aguarde um instante enquanto processamos sua solicitação.") if not(text.startswith("O seu código de rastreio é o")) else "O seu código de rastreio é o") if not text.startswith("Seguem as informações solicitadas:") else "Seguem as informações solicitadas:"}")):
            return False
    '''
            code += condition

    code += '''
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
    '''
    return code

def createScripts(interactionId):
    
    # Sua implementação da função createScripts
    print(f"Creating scripts with interaction ID: {interactionId}")
    
    numeroAnalyzer = contar_arquivos('basics/analyzers_whatsapp') + 1

    # Lista de mensagens (ocultada)
    messages = find_ticket_in_json(interactionId)
    
    # Gerar o código Python com base nas mensagens
    code = generate_code(interactionId,messages, numeroAnalyzer)

    # Especifica o nome do arquivo e o diretório de saída
    output_dir = 'basics/analyzers_whatsapp'
    filename = f'analyzer{numeroAnalyzer}.py'
    output_path = os.path.join(output_dir, filename)

    # Certifique-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Escreve o conteúdo no arquivo
    with open(output_path, 'w') as file:
        file.write(code)
        
    gerar_get_analyzers(numeroAnalyzer)

    print(f'Arquivo salvo em {output_dir}/{filename}')

def contar_arquivos(pasta):
    try:
        return len([arquivo for arquivo in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arquivo))])
    except FileNotFoundError:
        return "Pasta não encontrada"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    interactionId = input("Digite o interactionId: ")
    createScripts(interactionId)
