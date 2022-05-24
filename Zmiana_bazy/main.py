import numpy as np

bT = [[1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1,-1,-1,-1,-1],
      [1, 1,-1,-1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1,-1,-1],
      [1,-1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1,-1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1,-1, 0, 0],
      [0, 0, 0, 0, 0, 0, 1,-1]]


b = np.transpose(bT)
Xb = [8, 6, 2, 3, 4, 6, 6, 5]


def ortogon(arr):
      arrT = np.transpose(arr)

      return  np.matmul(arr, arrT)


def normalizuj(arr):
      norms = np.linalg.norm(arr)
      return arr / norms



def zmiana_bazy(B, X):
      Xa = np.matmul(B, X)
      return Xa


a = zmiana_bazy(b, Xb)
print(a)