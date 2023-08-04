class MusicTracker:
    '''A class representing a music listening list tracker'''

    def __init__(self):
        self.listening_diary = []

    def add(self, track: str):
        if not isinstance(track, str):
            raise Exception("Please enter a string.")
        elif track in self.listening_diary:
            raise Exception("This track is already in your listening list.")
        else: 
            self.listening_diary.append(track)

    def listening_list(self):
        return self.listening_diary