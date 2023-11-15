import pickle
from Video import Playlist, Video
with open('coded_list.pkl', 'rb') as f:
    file = pickle.load(f)
for i in range(len(file)):
    pl = file[i]
    for video in pl.videos:
        print(video.desc, ' ___ ', video.sense)

