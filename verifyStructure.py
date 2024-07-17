import re
from abc import ABC, abstractmethod
from typing import List, Dict
from basics.find_ticket_by_id import Message
from basics.qualification import Qualification

# Definição da classe abstrata para analisar chatbots
class ChatbotAnalyzer(ABC):
    @abstractmethod
    def isValid(self, messages: List[Dict[str, str]]) -> bool:
        pass

    @abstractmethod
    def getQualifications(self, messages: List[Dict[str, str]]) -> Dict[str, str]:
        pass

class Analyzer1:
    def isValid(self, messages: List[Message]) -> bool:
        if not messages or len(messages) != 8:
            return False
        
        cpf_pattern = re.compile(r'^\d{11}$')
        for chat in messages:
            if 'sender' not in chat or 'message' not in chat:
                return False
            message = chat['message'].strip().lower()
            if any(char.isdigit() for char in message) and not cpf_pattern.match(message):
                return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        selected_options = ''
        for chat in messages:
            message = chat['message'].strip().lower()
            if message.isdigit():
                option = int(message)
                if 0 <= option <= 10:
                    selected_options += str(option)

        num_options = len(selected_options)
        if num_options == 0:
            selected_option_text = "Sem opções selecionadas"
        elif num_options == 1:
            selected_option_text = "Selecionou apenas 1 opção"
        elif num_options <= 8:
            selected_option_text = f"Selecionou {num_options} opções no menu"
        else:
            selected_option_text = "Acima de 8 opções no menu"

        finalization_text = "Não encontrou opção de finalização de contato"
        for chat in messages:
            message = chat['message'].strip().lower()
            if "sem interação" in message and "sem resposta" in message:
                finalization_text = "Sem interação - Sem resposta do cliente"
                break
            elif "falta de dados corretos" in message:
                finalization_text = "Contato finalizado por falta de dados corretos"
                break
            elif "contato encerrado" in message and "script de finalização" in message:
                finalization_text = "Contato encerrado com script de finalização"
                break

        return Qualification(
            selectedOption=selected_option_text,
            customerJourney=selected_options,
            finalizationOfTheContract=finalization_text
        )

