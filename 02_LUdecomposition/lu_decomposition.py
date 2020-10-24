import numpy as np


def user_input():
    n = int(input("Enter matrix size: "))
    print("Enter matrix:")
    a = np.array([input().strip().split() for _ in range(n)], int)
    return a


def lu(A):
    n = A.shape[0]
    U = A.copy().astype('float64')
    L = np.zeros((n, n), int).astype('float64')
    np.fill_diagonal(L, 1)

    for i in range(n):
        factor = U[i + 1:, i] / U[i, i]
        factor = factor.astype('float64')
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return L, U


def check_result(A, L, U):
    A_new = L @ U
    return np.array_equal(A, A_new)


def mat_print(A):
    col_maxes = [max([len(("{:g}").format(x)) for x in col]) for col in A.T]
    for x in A:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+"g}").format(y), end="  ")
        print("")


def print_result():
    a = user_input()
    L, U = lu(a)
    print("LU decomposition:")
    print("L: \t")
    mat_print(L)
    print("\nU: \t")
    mat_print(U)
    print()
    if check_result(a, L, U):
        print("Matrix A = Matrix L * Matrix U")
    else:
        print("Sth went wrong!")


if __name__ == "__main__":
    print_result()
