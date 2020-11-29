from sympy import diff, log, sqrt, symbols
import numpy as np

MAX_ITERATIONS = 100
message = ""

def isIterable(J, xx):
    J_0 = J(xx)
    if abs(J_0[0][0]) + abs(J_0[0][1]) >= 1 or abs(J_0[1][0]) + abs(J_0[1][1]) >= 1:
        raise ValueError('Limit condition is not suitable for the method')


def iteration(F, J, xx, eps):
    global message
    try:
        isIterable(J, xx)
        for iter in range(MAX_ITERATIONS):
            x_new = F(xx)
            delta = np.absolute(x_new-xx)
            xx = x_new

            message += "Iteration " + str(iter + 1) + ": " + str(xx) + "\n"
            message += "Difference: " + str(delta) + "\n\n"
            if np.all(delta < eps):
                break
        return xx
    except ValueError as e:
        message += str(e)


def demonstration():
    x, y = symbols('x y')
    f1 = sqrt((x*(y+5)-1)/2.0)
    f2 = sqrt(x + 3.0 * log(x))

    def F(xx):
        return np.array(
            [f1.subs([(x, xx[0]), (y, xx[1])]),
             f2.subs([(x, xx[0]), (y, xx[1])])])

    def J(xx):
        return np.array(
            [[diff(f1, x).subs([(x, xx[0]), (y, xx[1])]), diff(f1, y).subs([(x, xx[0]), (y, xx[1])])],
             [diff(f2, x).subs([(x, xx[0]), (y, xx[1])]), diff(f2, y).subs([(x, xx[0]), (y, xx[1])])]])

    x = iteration(F, J, xx=np.array([3.5, 2.2]), eps=0.001)
    print("\nIterations:")
    print(message)
    print("Solution:")
    print(x)


if __name__ == "__main__":
    demonstration()





    # xx = np.array([3.5, 2.2])
    # print(diff(f2, x).subs(x, 3.5))
    # def F(x):
    #     return np.array(
    #         [np.sqrt((x[0]*(x[1]+5)-1)/2.0),
    #          np.sqrt(x[0] + 3.0 * np.log(x[0]))])