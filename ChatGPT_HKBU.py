import configparser
import requests

class HKBU_ChatGPT:
    def __init__(self, config_='./config.ini'):
        if isinstance(config_, str):
            self.config = configparser.ConfigParser()
            self.config.read(config_)
        elif isinstance(config_, configparser.ConfigParser):
            self.config = config_

    def submit(self, message):
        conversation = [{"role": "user", "content": message}]
        url = (
            self.config['CHATGPT']['BASICURL'] +
            "/deployments/" +
            self.config['CHATGPT']['MODELNAME'] +
            "/chat/completions/?api-version=" +
            self.config['CHATGPT']['APIVERSION']
        )
        headers = {
            'Content-Type': 'application/json',
            'api-key': self.config['CHATGPT']['ACCESS_TOKEN']
        }
        payload = {'messages': conversation}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response