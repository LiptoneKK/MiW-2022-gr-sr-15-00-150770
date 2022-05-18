import numpy as np
n = 3
mtx = [[2,1,3],[1,6,7],[3,7,9]]
mtx = np.array(mtx)
mtx.shape = (n,n)
Q, R = np.linalg.qr(mtx)
print("Macierz Q: \n",Q)
print("Macierz R: \n",R)
Ak = np.linalg.eigvals(mtx)
print("Macierz Ak: \n",Ak)