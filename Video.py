class Video:
    
    def __init__(self, name, Id, desc, playlist_id, position):  # position starts from 0
        self.nameU = name
        self.name = name.lower()
        self.desc = desc.lower()
        self.descU = desc
        self.pl_id = playlist_id  # video location i.e. playlist
        self.url = 'https://www.youtube.com/watch?v=' + Id + '&list=' + playlist_id + '&index=' + str(position + 1)
        
        
        if self.desc == '#shorts':  # makes two categories of videos
            self.sense = False
        else:
            self.sense = True
        
 

