import os
from basics.find_ticket_in_json import find_ticket_in_json
from gerar_get_analyzers import gerar_get_analyzers
from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# Função para gerar o código Python
def generate_code(interactionId, messages, numeroAnalyzer):
    # Cabeçalho do arquivo gerado
    code = f'''from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# {interactionId}

class Analyzer{numeroAnalyzer} :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == {len(messages)}):
            return False
    '''

    # Loop através das mensagens para criar as condições de validação
    for i, message in enumerate(messages):
        if message['sender'] == 'bot':
            text = message['message'].replace("\n", "\\n")
            # Determina o texto de condição com base no início da mensagem
            condition_text = (
                "Seguem as informações solicitadas"
                if text.startswith("Seguem as informações solicitadas")
                else 'Aqui está a sua última fatura disponível'
                if text.startswith('Aqui está a sua última fatura disponível')
                else 'Por favor aguarde um instante enquanto processamos sua solicitação'
                if text.startswith('Por favor aguarde um instante enquanto processamos sua solicitação')
                else 'O seu código de rastreio é o'
                if text.startswith('O seu código de rastreio é o')
                else text[:100]
            )
            # Adiciona a condição ao código
            condition = f'''
        if not (messagesClient[{i}]["sender"] == "bot" and messagesClient[{i}]["message"].startswith("{condition_text}")):
            return False
    '''
            code += condition

    # Adiciona a finalização da função isValid e a função getQualifications
    code += '''
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": '',
        }
    '''
    return code

def createScripts(interactionId):
    # Imprime o ID da interação para o usuário
    print(f"Creating scripts with interaction ID: {interactionId}")

    # Incrementa o número do analisador com base no número de arquivos existentes
    numeroAnalyzer = contar_arquivos('basics/analyzers_autopilot_usuario') + 1

    # Obtém as mensagens a partir do interactionId
    messages = find_ticket_in_json(interactionId)

    # Gera o código Python com base nas mensagens
    code = generate_code(interactionId, messages, numeroAnalyzer)

    # Especifica o nome do arquivo e o diretório de saída
    output_dir = 'basics/analyzers_autopilot_usuario'
    filename = f'analyzer{numeroAnalyzer}.py'
    output_path = os.path.join(output_dir, filename)

    # Certifique-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Escreve o conteúdo no arquivo
    with open(output_path, 'w') as file:
        file.write(code)

    # Gera os analisadores
    gerar_get_analyzers(numeroAnalyzer)

    # Imprime a localização do arquivo salvo
    print(f'Arquivo salvo em {output_dir}/{filename}')

# Função para contar o número de arquivos em uma pasta
def contar_arquivos(pasta):
    try:
        # Conta apenas arquivos, ignorando diretórios
        return len([arquivo for arquivo in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, arquivo))])
    except FileNotFoundError:
        return 0
    except Exception as e:
        return str(e)

# Ponto de entrada do script
if __name__ == "__main__":
    # Solicita o ID da interação ao usuário
    interactionId = input("Digite o interactionId: ")
    createScripts(interactionId)
