import json
from datetime import date

from app.downloader import IFQDownloader
from app.uploader import OwncloudUploader
from app.notifier import TelegramNotifier

downloader = IFQDownloader()
uploader = OwncloudUploader()
notifier = TelegramNotifier()

def handle(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    # download today IFQ
    local_path = downloader.download(date.today())

    # upload to owncloud
    link = uploader.upload(local_path, date.today())

    # send message using telegram
    notifier.send(f"Il numero di oggi è disponibile qui: {link}")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
