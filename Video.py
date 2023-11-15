class Playlist:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.url = '//www.youtube.com/playlist?list=' + self.id
        self.videos = []
        self.videos_count = 0

    def add_videos(self, list):  # function adds videos to playlist; counts amount of videos;
        # list is a list of all videos from that playlist
        self.videos_count = len(list)
        for i in list:
            self.videos.append(i)


class Video:
    
    def __init__(self, name, id, desc, playlist_id, position):  # position starts from 0
        self.name = name
        self.id = id
        self.desc = desc  # video description
        self.pl = playlist_id  # video location i.e. playlist
        self.url = 'https://www.youtube.com/watch?v=' + id + '&list=' + playlist_id + '&index=' + str(position + 1)

        if self.desc == '#shorts':  # makes two categories of videos
            self.sense = False
        else:
            self.sense = True

    # def get_stuff(self, *args):
    #     z = []
    #     if name in args:
    #         z.append(self.name)
    #     if url in args:
    #         z.append(self.url)
    #     if desc in args:
    #         z.append(self.desc)
    #     return z
