import playsound

class Music:
    def __init__(self, id, title, duration, file):
        self.id = id
        self.title = title
        self.duration = duration
        self.file = file
    def __str__(self):
        return f'ID : {self.id} | Name: {self.title} | Duration: {self.duration} | File location: {self.file}'

class MusicList:
    def __init__(self, music_list = []):
        self.music_list = music_list
    
    def add_music(self, music):
        self.music_list.append(music)
    
    def play_music(self, id):
        for music in self.music_list:
            if music.id == id:
                playsound


    
