import requests
from typing import List, Literal, TypedDict
from basics.get_token import get_token, update_token
from basics.find_session_id import find_session_id
import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo de som
pygame.mixer.music.load("tf_nemesis.mp3")

url = "https://api.talkdeskapp.com/virtual-agent/monitor/conversations/session"

class Message(TypedDict):
    sender: Literal["bot", "client"]
    message: str



def find_ticket_by_id(id) -> List[Message]:
    while True:
        print(f"find_ticket_by_id({id})")
        try:
            interactionId = find_session_id(id)
                
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                "authorization": get_token(),
                "priority": "u=1, i",
                "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Linux\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "Referer": "https://prd-cdn-talkdesk.talkdesk.com/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            }

            response = requests.get(f"{url}/{interactionId}", headers=headers)
            data = response.json()
            messages: List[Message] = []

            if not 'session' in data:
                raise Exception('Error', id, data)

            segments = data['session']['segments']
            
            for segment in segments:
                messages.append(Message({
                    "sender": "client",
                    "message": segment['message']
                }))
                
                messages.append(Message({
                    "sender": "bot",
                    "message": segment['response']
                }))

            return messages
        except Exception as e:
            # Reproduzir o som
            pygame.mixer.music.play()

            print('Token inválido. Atualizando...', e)
            update_token()