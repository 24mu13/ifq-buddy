import logging
import requests

from app.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

class TelegramNotifier:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.token = TELEGRAM_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID

    def send(self, msg):
        params = {
            'chat_id': self.chat_id,
            'text': msg
        }
        res = requests.get(
            f'https://api.telegram.org/bot{self.token}/sendMessage',
            params=params
        )
        self.logger.info(f'Telegram API invoked with result code {res.status_code}')
