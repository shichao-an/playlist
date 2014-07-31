# -*- coding: utf-8 -*-
import csv


def write_data(filename, rows):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


class Song(object):
    def __init__(self, song_id, name, artist, replays=0):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.replays = replays


class Playlist(object):
    csvfile = 'playlist.csv'
    header = ['id', 'name', 'artist', 'played']

    def __init__(self):
        self.songs = self.load_songs()
        self.dict_songs = {s.song_id: s for s in self.songs}

    def load_songs(self):
        songs = []
        lines = filter(lambda x: x, read_data(self.csvfile))
        raw_songs = lines[1:]
        for raw_song in raw_songs:
            song_id = int(raw_song[0])
            name = raw_song[1]
            artist = raw_song[2]
            replays = int(raw_song[3])
            song = Song(song_id, name, artist, replays)
            songs.append(song)
        return songs

    def add_song(self, name, artist, replays=0):
        if not self.songs:
            song_id = 1
        else:
            song_id = len(self.songs) + 1
        song = Song(song_id, name, artist, replays)
        self.songs.append(song)

    def update_song(self, song_id, name, artist, replays):
        song = self.dict_songs[song_id]
        song.name = name
        song.artist = artist
        song.replays = replays

    def save_songs(self, replays=True):
        if replays is True:
            self.songs.sort(key=lambda x: x.replays, reverse=True)
        else:
            self.songs.sort(key=lambda x: x.song_id)
        #print [song.replays for song in self.songs]
        print '%d songs in total.' % len(self.songs)
        lines = [
            [x.song_id, x.name, x.artist, x.replays] for x in self.songs
        ]
        lines.insert(0, self.header)
        write_data(self.csvfile, lines)


if __name__ == '__main__':
    print 'Add a new song'
    name = raw_input('Name: ').strip()
    artist = raw_input('Artist: ').strip()
    replays = raw_input('Played: ').strip()
    replays = int(replays)
    playlist = Playlist()
    playlist.add_song(name, artist, replays)
    playlist.save_songs()
