import numpy as np

MAX_ITERATIONS = 100
message = ""


def user_input():
    n = int(input("Enter matrix size: "))
    print("Enter A matrix:")
    a = np.array([input().strip().split() for _ in range(n)], float)
    print("Enter B vector:")
    b = np.array(input().strip().split(), dtype=float)
    exp = float(input("Enter exp:"))
    return n, a, b, exp


def print_equation_system(n, A, b):
    for i in range(n):
        print(" + ".join([str(A[i, j]) + "*x" + str(j + 1) for j in range(n)]), "=", b[i])


def Seidel(A, B, n, eps):
    global message
    x = np.zeros(n, dtype=np.float64)
    for iteration in range(MAX_ITERATIONS):
        xx = x.copy()
        for i in range(n):
            x[i] = -(A[i, :]@x - B[i] - A[i, i] * x[i]) / A[i, i]

        gap = abs(x - xx)
        message += "Iteration " + str(iteration + 1) + ": " + str(x) + "\n"
        message += "Difference: " + str(gap) + "\n\n"

        if max(gap) < eps:
            break

    return x


def demonstration():
    n, A, B, eps = user_input()
    print("\nEquation system:")
    print_equation_system(n, A, B)
    x = Seidel(A, B, n, eps)
    print("\nIterations:")
    print(message)
    print("Solution:")
    print(x)


if __name__ == "__main__":
    demonstration()

# 3.2 -11.5 38
# 0.8 1.3 -6.4
# 2.4 7.2 -1.2

# 2.8 -6.5 4.5