import yaml
from yaml.loader import SafeLoader
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import sqlite3 as sl

class Export:
    def __init__(self):
        self.set_my_credentials()
        self.launch_API()
        self.user = "22rgo6mrxumdxizu6z26jiubq"
        self.get_all_playlists()

    def set_my_credentials(self):
        with open('../secrets.yaml') as file:
            secret_data = yaml.load(file, Loader=SafeLoader)
        self.client_ID = secret_data["spotify"]["client_ID"]
        self.client_secret = secret_data["spotify"]["client_Secret"]

    def launch_API(self):
        self.auth_manager = SpotifyClientCredentials(client_id=self.client_ID, client_secret=self.client_secret)
        self.api = spotipy.Spotify(client_credentials_manager=self.auth_manager)

    def get_all_playlists(self):
        self.all_playlists = self.api.user_playlists(user=self.user)
        print(self.all_playlists)
        # print("1: {}".format(self.all_playlists['items']))
        # print("2: {}".format(self.all_playlists['offset']))
        self.list_playlists = list()
        while self.all_playlists:
            for i, playlist in enumerate(self.all_playlists['items']):
                self.list_playlists.append(playlist['name'])
                #print(playlist)
            if self.all_playlists['next']:
                self.all_playlists = self.api.next(self.all_playlists)
            else:
                self.all_playlists = None
        print(self.list_playlists)
        # playlists = self.api.user_playlists(user=user)
        # while playlists:
        #     for i, playlist in enumerate(playlists['items']):
        #         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
        #     if playlists['next']:
        #         playlists = self.api.next(playlists)
        #     else:
        #         playlists = None


if __name__ == '__main__':
    Export()


my_playlist = api.playlist('3EJrGDybRcxA26kqVFJbGc')
playlist_name = my_playlist['name']
num_tracks = my_playlist['tracks']['total']
tracks = my_playlist['tracks']['items']
for i in tracks:
    if 'track' in i:
        i = i['track']
        print(i['name'])
    if not i:
        continue