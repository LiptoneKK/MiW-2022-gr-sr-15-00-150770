import numpy as np
A = np.array([[1, 2, 0],
              [2, 0, 2]])
U, s, V = np.linalg.svd(A)
S = np.zeros((A.shape[0], A.shape[1]))
S[:A.shape[0], :A.shape[0]] = np.diag(s)

wynik = np.dot(np.dot(U,S),np.transpose(V))
print("u: ")
print(U)
print("s: ")
print(S)
print("v: ")
print(V)
print("A = UEV^T")
print(wynik)
#różnica w wyniku prawdopodobnie wynika z dokładności jaką oferuje nam program
