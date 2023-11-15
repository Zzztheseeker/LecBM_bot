import os
api_key = os.environ.get('API_KEY')
from googleapiclient.discovery import build
#creating a service object called 'youtube'
youtube = build('youtube', 'v3', developerKey=api_key)
#creating a request to the youtube API
request = youtube.channels().list(
    part='statistics',
    id='UC95pxYA1WsVxh9GKJ59lfpQ'
)
#get a response by executing the request
response = request.execute()
print(response)


youtube.close()