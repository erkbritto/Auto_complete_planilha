from basics.find_ticket_by_id import Message
from typing import List, Dict
from basics.qualification import Qualification

class Analyzer2 :
    def isValid(self, messages: List[Message]) -> bool:
        pass

    def getQualifications(self, messages: List[Message]) -> Qualification:
        pass


    def cpfNoResponse(conversation):
        #id usado como exemplo de tratativa : 37d0d050c0b24194a85dbdaa883e156d
        
        if len(conversation) < 3:
            return False
        
        # Verificar se a primeira mensagem é do usuário
        if conversation[0]['sender'] != 'user':
            return False
        
        # Verificar se a segunda mensagem é uma resposta automática do bot
        if conversation[1]['sender'] != 'bot' or not conversation[1]['text'].startswith('Mensagem padrão automática'):
            return False
        
        # Verificar se a terceira mensagem é uma solicitação de CPF do bot
        if conversation[2]['sender'] != 'bot' or 'CPF' not in conversation[2]['text']:
            return False
        
        # Verificar se não há resposta do usuário após a solicitação de CPF
        for mensagem in conversation[3:]:
            if mensagem['sender'] == 'user':
                return False
        
        return True

    # Exemplo de uso
    con_exemplo = [
        {'sender': 'user', 'text': 'Olá, eu preciso de ajuda.'},
        {'sender': 'bot', 'text': 'Mensagem padrão automática: Bem-vindo! Como posso ajudar?'},
        {'sender': 'bot', 'text': 'Por favor, forneça seu CPF para continuar.'},
        # Nenhuma mensagem do usuário após a solicitação de CPF
    ]


print(cpfNoResponse(con_exemplo))  # Deve retornar True