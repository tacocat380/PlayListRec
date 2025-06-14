import os
import multiprocessing
from tqdm import tqdm
import json

def getUniqueSong(inputFilePath):
    songs = set()
    with open(inputFilePath,'r') as f:
        data = json.load(f)
        data = data["playlists"]
        for playlist in data:
            for song in playlist["tracks"]:
                songs.add(song["track_name"] + " by " + song["artist_name"]) # accounts for track uri redirect legacy problem 
    return songs

def getUniqueSongs(threads,inputFolderPath,outputFolderPath):
    print("Creating song dictionary")
    try:
        fileList = os.listdir(inputFolderPath)
        fileList = [os.path.join(inputFolderPath,file) for file in fileList]

    except FileNotFoundError or PermissionError:
        print("getUniqueSongs, folder error")

    print("Reading each file and merging")
    total_result = set()
    with multiprocessing.Pool(processes=threads) as pool:
        for result in tqdm(pool.imap(getUniqueSong,fileList),total = len(fileList)):
            total_result.update(result)

    total_result = list(total_result)
    song_int = {total_result[index]:index for index in range(len(total_result))}
    int_song = {index:total_result[index] for index in range(len(total_result))}

    print(f"Number of tracks found: {len(total_result):,}")

    with open(os.path.join(outputFolderPath,"uniqueSongList"),'w') as f:
        json.dump(total_result,f)

    with open(os.path.join(outputFolderPath,"song_int"),'w') as f:
        json.dump(song_int,f)

    with open(os.path.join(outputFolderPath,"int_song"),'w') as f:
        json.dump(int_song,f)

