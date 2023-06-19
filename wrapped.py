import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

top_tracks = sp.current_user_top_tracks(limit = 50, time_range = "long_term")
top_artists = sp.current_user_top_artists(limit = 50, time_range = "long_term")
artist_pop = [[i, 0] for i in range(5)]
track_pop = [[i, 0] for i in range(5)]

tracks = []
track_pop_sorted = []
for idx, item in enumerate(top_tracks["items"]):
    tracks.append(item["name"])
    track_pop[min(4, item["popularity"] // 20)][1] += 1
    track_pop_sorted.append((item["name"], item["popularity"]))
    #print(str(idx + 1) + ". " + item["name"] + ", ", item["popularity"])
genres = {}
artists = []
artist_pop_sorted = []
for idx, item in enumerate(top_artists["items"]):
    artist_pop[min(4, item["popularity"] // 20)][1] += 1
    artists.append(item["name"])
    artist_pop_sorted.append((item["name"], item["popularity"]))
    for i in item["genres"]:
        if i not in genres:
            genres[i] = 1
        else:
            genres[i] += 1
    #print(str(idx + 1) + ". " + item["name"] + ", ", item["popularity"], item["genres"])
artist_pop_sorted.sort(key=lambda x: x[1])
track_pop_sorted.sort(key=lambda x: x[1])
#print(artist_pop_sorted)
genrearr = []
for i in genres:
    genrearr.append((i, genres[i]))
genrearr.sort(key=lambda x: -x[1])

sorted_track_pop = list(sorted(track_pop, key=lambda x: x[1]))
sorted_artist_pop = list(sorted(artist_pop, key=lambda x: x[1]))
#print("Average artist popularity: " + str(avg_artist_popularity))
#print("Average track popularity: " + str(avg_track_popularity))

print("Top tracks: ")
for i in range(5):
    print(str(i + 1) + ". " + tracks[i])

print("Top artists: ")
for i in range(5):
    print(str(i + 1) + ". " + artists[i])

print("Top genres: ")
for i in range(5):
    print(str(i + 1) + ". " + genrearr[i][0])

print("Your most popular artists:")
for i in range(5):
    print(str(i + 1) + ". " + artist_pop_sorted[len(artist_pop_sorted) - 1 - i][0])

print("Your most underground artists:")
for i in range(5):
    print(str(i + 1) + ". " + artist_pop_sorted[i][0])

print("Your most popular tracks")
for i in range(5):
    print(str(i + 1) + ". " + track_pop_sorted[len(track_pop_sorted) - 1 - i][0])

print("Your most underground tracks:")
for i in range(5):
    print(str(i + 1) + ". " + track_pop_sorted[i][0])



'''Top songs,
top artists,
top genres,
most underground artists, most popular artists, artist popularity distribution,
most underground tracks, most popular tracks, track popularity distribution
'''
