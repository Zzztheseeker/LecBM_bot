import os
import pickle
from Video import Video, Playlist
from googleapiclient.discovery import build
api_key = os.environ.get('API_KEY')

#PL_id='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I'
#channel_id='UC95pxYA1WsVxh9GKJ59lfpQ'
# Creating a service
youtube = build('youtube', 'v3', developerKey=api_key)

# parsing channel
ch_request = youtube.playlists().list(
    part='contentDetails, snippet',
    channelId='UC95pxYA1WsVxh9GKJ59lfpQ',
    maxResults=50,
)
ch_response = ch_request.execute()
# # creating a list of playlists from channel
pl_list = []  # # this would be our list of playlists from channel
for item in ch_response['items']:
    plpl = Playlist(item['snippet']['title'],item['id'])  # making playlist as object <class 'Playlist'>
    pl_list.append(plpl)

# parsing playlist
for playlist in pl_list:
    pl_request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist.id,
        maxResults=50
    )
    pl_response = pl_request.execute()
    # creating a list of objects <class 'Video'>
    vids_from_pl = []
    for item in pl_response['items']:
        descript = item['snippet']['description']
        # handling video descriptions
        if '#shorts' in descript:
            descript = '#shorts'
        else:
            code = descript.find('https://')
            if code != -1:
                new_code = descript.find('Ходите на лекции.')
                if new_code != -1:
                    code = new_code
                    new_code = descript.find('Максим Тадей')
                    if new_code != -1:
                        code = new_code - 3
                descript = descript[:code-1]
        vivi = Video(item['snippet']['title'], item['snippet']['resourceId']['videoId'], descript, playlist.id, item['snippet']['position'])  # making video as object <class 'Video'>
        vids_from_pl.append(vivi)
    playlist.add_videos(vids_from_pl)

youtube.close()

# putting our list of playlists in .pkl file
with open('coded_list.pkl', 'wb') as f:
    pickle.dump(pl_list, f)