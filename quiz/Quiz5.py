class SpotifyPlaylist:
    def __init__(self, name, initial_songs=None):
        self.name = name
        self.songs = initial_songs if initial_songs is not None else []
        self.current_song_index = 0  # To keep track of the current song being played

    def add(self, song):
        if song in SONGS:
            self.songs.append(song)
            return f'Added "{song}" to {self.name}'
        else:
            return f'"{song}" is not available.'

    def play_next(self):
        if self.songs:
            print(f'Playing: {self.songs[self.current_song_index]}')
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        else:
            print('No songs in the playlist to play.')

    def total_length(self):
        return sum(SONGS[song] for song in self.songs if song in SONGS)

