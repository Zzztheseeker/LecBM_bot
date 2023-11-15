#this is an extended version of playlist.py with all the videos from channel (compared to just first 5 videos)
#to do so we're using pageTokens
import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('API_KEY')

#PL_id='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I'
#channel_id='UC95pxYA1WsVxh9GKJ59lfpQ'
youtube = build('youtube', 'v3', developerKey=api_key)
#setting duration patterns for duration (see video contentDetails) using re module
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

#creating a while-loop which keeps grabbing pages until where are no more left
nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I',
        maxResults=50,  # to make more results per page, so we dont make too many API requests
        pageToken=nextPageToken
    )
    pl_response = pl_request.execute()
    #creating a list of videoIds
    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    #create string - comma separated list of videoIds
    list_of_videos = ','.join(vid_ids)
    print(list_of_videos)
    print()

    vid_request = youtube.videos().list(
        part='contentDetails',
        id=list_of_videos
    )
    vid_response = vid_request.execute()

    time_total = 0
    for item in vid_response['items']:
        duration = item['contentDetails']['duration']
        #recognizing duration patterns in our duration object
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1))
        #calculating the total amount of seconds using datetime module
        video_seconds = timedelta(
            hours = hours,
            minutes = minutes,
            seconds = seconds
        ).total_seconds()
        time_total += video_seconds #this is the duration of our playlist in seconds
    #updating pages
    nextPageToken = pl_response.get('nextPageToken')
    if not nextPageToken:
        break

print(time_total)

youtube.close()
