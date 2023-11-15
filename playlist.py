import os
import re #importing regular expressions for recognizing patterns in list of durations(see vid_response)
from datetime import timedelta #for quick processing values from (hours, minutes, seconds) instead of using math
from googleapiclient.discovery import build

api_key = os.environ.get('API_KEY')

#PL_id='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I'
#channel_id='UC95pxYA1WsVxh9GKJ59lfpQ'
youtube = build('youtube', 'v3', developerKey=api_key)
pl_request = youtube.playlistItems().list(
    part='contentDetails',
    playlistId='PLCHxbklCcsObnQuG4EdnPID3DTDvWVD6I'
)
pl_response = pl_request.execute() #returns first 5 videos in playlist
#creating a list of videoIds
vid_ids = []
for item in pl_response['items']: #returns only videoIds of first 5 videos in playlist
    vid_ids.append(item['contentDetails']['videoId'])

#create string - comma separated list of videoIds
list_of_videos = ','.join(vid_ids)

vid_request = youtube.videos().list(
    part='contentDetails',
    id=list_of_videos
) #cant request more than 50 vids at once
vid_response = vid_request.execute() #returns characteristics of first 5 videos from playlist

#setting duration patterns for duration in contentDetails using re module
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M') #d is for digit; d+ captures one ore more digits; FIY see vid_response.txt
seconds_pattern = re.compile(r'(\d+)S')
time_total = 0
for item in vid_response['items']:
    duration = item['contentDetails']['duration']
    #recognizing duration patterns in our duration object
    hours = hours_pattern.search(duration)   #returns complicated result, for ex:<re.Match object; span=(2, 4), match='1H'>
    minutes = minutes_pattern.search(duration)
    seconds = seconds_pattern.search(duration)

    hours = int(hours.group(1)) if hours else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1))
    #calculating the total amount of seconds (first 5 videos from channel) using datetime module
    video_seconds = timedelta(
        hours = hours,
        minutes = minutes,
        seconds = seconds
    ).total_seconds()
    time_total += video_seconds #this is the duration of first 5 videos from playlist in total

print(time_total)

youtube.close()