import numpy as np


def trapezoidal_rule(fun, a, b, n):
    integral = 0

    dx = (b - a) / n

    for i in range(n):
        fa = a + dx * i
        fb = a + dx * (i + 1)

        integral += (fun(fa) + fun(fb)) / 2 * dx
    return integral


integral = trapezoidal_rule(lambda x: x, 0.0, 1.0, 100)
print(integral)


# -===========================================


def func1(x):
    return x


def mc_integrate(func, a, b, n):
    vals = np.random.uniform(a, b, n)
    y = [func(val) for val in vals]

    y_mean = np.sum(y) / n
    integ = (b - a) * y_mean

    return integ


print(f"Monte Carlo solution: {mc_integrate(func1, 0, 1, 1000000): .4f}")

# -----------------------------------

x_y = [[2, 1], [5, 2], [7, 3], [8, 3]]


def matrix_transpose(matrix):
    return np.dot(np.transpose(matrix), matrix)


def matrix_inverse(matrix):
    return np.linalg.inv(matrix)


def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)


def linear_regression(matrix):
    matrix_x = np.array([1, x[0]] for x in matrix)
    matrix_y = np.array([x[1] for x in matrix])
    kow = matrix_transpose(matrix_x)
    odw = matrix_inverse(kow, np.transpose(matrix_x))
    return np.dot(odw, np.transpose(matrix_x), matrix_y)


