import os

IFQ_USERNAME = os.environ['IFQ_USERNAME']
IFQ_PASSWORD = os.environ['IFQ_PASSWORD']

OC_URL = os.environ['OC_URL']
OC_USERNAME = os.environ['OC_USERNAME']
OC_PASSWORD = os.environ['OC_PASSWORD']

OC_FILE_PATTERN = 'Newspapers/Il fatto quotidiano/{day:%Y}/ilfatto{day:%Y%m%d}.pdf'

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
