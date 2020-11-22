import numpy as np

MAX_ITERATIONS = 100
message = ""


def Newton_system(F, J, x, eps):

    global message
    for iteration in range(MAX_ITERATIONS):
        D_x = J(x)
        D_y = J(x)
        D_x[:, 0] = F(x)
        D_y[:, 1] = F(x)

        det = np.linalg.det(J(x))
        det_x = np.linalg.det(D_x)
        det_y = np.linalg.det(D_y)

        x_new = np.array([x[0] - det_x / det, x[1] - det_y / det])
        delta = np.absolute(x_new-x)
        x = x_new

        message += "Iteration " + str(iteration + 1) + ": " + str(x) + "\n"
        message += "Difference: " + str(delta) + "\n\n"
        if np.all(delta < eps):
            break

    return x


def demonstration():
    def F(x):
        return np.array(
            [np.exp(2 * x[0]) + x[1] ** 0.5 - 3.0,
             np.exp(x[0]) - 3 * (x[1] ** 0.5) + 1.0])

    def J(x):
        return np.array(
            [[2 * np.exp(2 * x[0]), 1.0 / (2 * (x[1] ** 0.5))],
             [np.exp(x[0]), -3.0 / (2 * (x[1] ** 0.5))]])

    x = Newton_system(F, J, x=np.array([-0.9, 0.5]), eps=0.001)
    print("\nIterations:")
    print(message)
    print("Solution:")
    print(x)


if __name__ == "__main__":
    demonstration()

