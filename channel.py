import os
api_key = os.environ.get('API_KEY')
from googleapiclient.discovery import build

PL_id='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I'
channel_id='UC95pxYA1WsVxh9GKJ59lfpQ'
youtube = build('youtube', 'v3', developerKey=api_key)
#creating a request to Youtube playlist
pl_request = youtube.playlistItems().list(
    part='snippet',
    playlistId='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I',
    maxResults=50
)
pl_response = pl_request.execute() #returns channel general description + first 5 playlists on channel

for item in pl_response['items']:
    print(item['snippet']['resourceId'])
    print()

#type(pl_response)) returns <class 'dict'>

youtube.close()