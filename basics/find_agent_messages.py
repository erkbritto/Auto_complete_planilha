import requests
from typing import List

from basics.get_token import get_token, update_token
import pygame
from basics.find_ticket_by_id import Message

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo de som
pygame.mixer.music.load("tf_nemesis.mp3")

def find_agent_messages(interaction_id: str) -> List[Message]:
    while True:

        print(f"find_agent_messages({interaction_id})")
        try:
            url = f"https://api.talkdeskapp.com/cds/messages?interaction_id={interaction_id}&order_by=occur_at:asc&per_page=999"
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
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            data = response.json()
            messages: List[Message] = []
            if not '_embedded' in data:
                raise Exception('Error', id, data)
        
            chats = data['_embedded']['message']
            
            for message in chats:
                messages.append(Message({
                    "sender": 'client' if message['direction'] == 'INBOUND' else 'bot',
                    "message": message['content'],
                }))
            
            return messages

        except Exception as e:
            # Reproduzir o som
            pygame.mixer.music.play()

            print('Token inválido. Atualizando...', e)
            update_token()
