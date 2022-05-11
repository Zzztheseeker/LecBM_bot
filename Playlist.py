class Playlist:
    def __init__(self, name, Id):
        self.name = name.lower()
        self.Id = Id
        self.url = '//www.youtube.com/playlist?list=' + self.Id
        self.videos = []
        self.videos_count = 0
        
    
    def add_videos(self, list_vid):  # function adds videos to playlist; counts amount of videos;
            # list is a list of all videos from that playlist
            self.videos_count = len(list_vid)
            for i in list_vid:
                self.videos.append(i)    