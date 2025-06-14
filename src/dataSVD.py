import os 
import json 
import numpy as np
from tqdm import tqdm
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
from scipy.sparse import save_npz


def mySVD(path_song_int,path_songData,k):
    data = []
    row_indices = [] 
    col_indices = []
    print("Reading data and creating matrix")
    with open(path_song_int,'r') as f:
        song_int = json.load(f)

    playlistSlices = os.listdir(path_songData)
    currentPlaylist = 0

    for slice in tqdm(playlistSlices):
        with open(os.path.join(path_songData,slice)) as f:
            list_playList = json.load(f)["playlists"]
            for playlist in list_playList:
                for track in playlist["tracks"]:
                    tempName = track["track_name"] + " by " + track["artist_name"]
                    if tempName in song_int:
                        data.append(1)
                        row_indices.append(currentPlaylist)
                        col_indices.append(song_int[tempName])
                currentPlaylist += 1

    print(f"Number of playlist read: {currentPlaylist:,}")
    print("Computing SVD")
    matrix = csr_matrix((data, (row_indices, col_indices)), shape=(1_000_000, max(song_int.values())+1))
    matrix = matrix.astype(np.float64)
    u, s, vt = svds(matrix, k=k)
    print("SVD computed")

    u = csr_matrix(u)
    s = csr_matrix(s)
    vt = csr_matrix(vt)
    save_npz('matrixData/matrixU.npz', u)
    save_npz('matrixData/matrixS.npz', s)
    save_npz('matrixData/matrixVT.npz', vt)
    print("SVD saved")

