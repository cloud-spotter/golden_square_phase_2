class DiaryEntry:
    def __init__(self, title: str, contents: str):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title and contents")
        self._title: str = title
        self._contents: str = contents
        self._read_so_far = 0

    def format(self):
        return f"{self._title}: {self._contents}"

    def count_words(self):
        '''Returns a count of the words in a diary entry, including the title'''
        word_count = len(self.format().split())
        return f"Total words in this diary entry: {word_count}"

    def reading_time(self, wpm: int):
        if wpm == 0:
            raise Exception("Cannot calculate reading time for wpm of 0")
        contents_length = len(self._contents.split())
        time_in_min = round(contents_length / wpm)
        return time_in_min

    def reading_chunk(self, wpm: int, minutes: int):
        '''Returns a chunk of the contents that the user could read in the given number of minutes, as a string'''
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words = self._contents.split()
        words_to_read = wpm * minutes
        
        if self._read_so_far >= len(words):
            self._read_so_far = 0
        
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_to_read
        chunk_of_words = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_of_words)
