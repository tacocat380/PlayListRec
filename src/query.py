import os 
import json 
import numpy as np
from scipy.sparse import load_npz, csr_matrix

def query(inputMatrix):
    # check matrix data 
    try: 
        vt = load_npz('matrixData/matrixVT.npz')
        v = vt.T
    except:
        print("matrixData file input error")
    inputMatrix = csr_matrix(inputMatrix)
    if all(item in [0,1] for item in inputMatrix.data):
        # perform qVVt
        result = inputMatrix.dot(v)
        return result.dot(vt).toarray().tolist()[0]
    else:
        print("Matrix isn't binary")
        return -1

def matrix_string(inputMatrix,num_topSongs):
    with open('playlist_data/int_song','r') as f:
        int_song = json.load(f)
    sorted_indices = sorted(range(len(inputMatrix)), key=lambda i: inputMatrix[i], reverse=True)[:num_topSongs]
    result = []
    for index in sorted_indices:
        result.append(int_song[str(index)])
    return result

def string_matrix(inputList):
    with open('playlist_data/song_int','r') as f:
        song_int = json.load(f)
    result = [0] * (max(song_int.values())+1)
    for index in inputList:
        if index in song_int:
            result[song_int[index]] = 1
        else:
            print(f"Song not found: {index}")
    return result