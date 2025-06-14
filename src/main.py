from uniqueSongs import *
from dataSVD import *
from query import *

if __name__ == '__main__':
    #getUniqueSongs(8,'spotify_million_playlist_dataset/data','playlist_data')
    #mySVD('playlist_data/song_int','spotify_million_playlist_dataset/data',200)
    pass

songList = ["Talk That Talk by Rihanna","Heartless by Kanye West"]
print("Starting")
result = string_matrix(songList)
print("String Matrix to song int")
result = query(result)
print("Query done")
result = matrix_string(result,40)

print("Results:")
for song in result:
    print(song)