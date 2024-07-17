import requests
from basics.get_token import get_token

url = "https://api.talkdeskapp.com/virtual-agent/monitor/conversations"

def find_session_id(interactionId:str):

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
    
    params = {
        "filter": f"interaction_id like \"%{interactionId}%\" and (last_session_time ge \"2024-01-01T00:00:00-03:00[America/Sao_Paulo]\" and (last_session_time lt \"2024-07-15T23:59:59-03:00[America/Sao_Paulo]\" or (last_session_time lt \"2024-07-15T23:59:59-03:00[America/Sao_Paulo]\") ))",
        "order_by": "start_session_time:desc",
        "page": "1",
        "per_page": "1"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if not '_embedded' in data:
        raise Exception('Error', interactionId, data) 

    if len(data['_embedded']) == 0:
        raise Exception(f"Nenhum atendimento encontrado com o ID '{interactionId}'.")

    return data['_embedded'][0]['session_id']
