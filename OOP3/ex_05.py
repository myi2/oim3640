class MusicLibrary:
    def __init__(self, owner):
        self.owner = owner
        self.tracks = []

    def __str__(self):
        return f"Music library of {self.owner}: {len(self.tracks)} tracks"

    def __add__(self, other):
        if isinstance(other, str):
            self.tracks.append(other)
            print(f"{other} has been added to the music library.")
        else:
            print("Error: Can only add tracks (strings) to the music library.")

    def add_track(self, track):
        self.tracks.append(track)
        print(f"{track} has been added to the music library.")

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            print(f"{track} has been removed from the music library.")
        else:
            print(f"{track} is not in the music library.")


#=====================================================================================


# Testing the class
library1 = MusicLibrary("Alice")
library2 = MusicLibrary("Bob")

print(library1)
print(library2)

library1.add_track("Bohemian Rhapsody")
library1.add_track("Stairway to Heaven")
library2.add_track("Imagine")

print(library1)
print(library2)

library1 + "Hotel California"
library1.remove_track("Stairway to Heaven")

print(library1)
print(library2)
