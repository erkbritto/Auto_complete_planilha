import json
from typing import Dict
from typing import List
from basics.find_ticket_by_id import Message

class JsonDataHandler:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_data(self, data: Dict[str, List[Message]]) -> None:
        with open(self.file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_data(self) -> Dict[str, List[Message]]:
        try:
            with open(self.file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
