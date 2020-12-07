import matplotlib.pyplot as plt
import numpy as np


def user_input():
    n = int(input('Enter number of data points: '))
    points = np.zeros((n, 2))
    print('Enter data for x and y: ')
    for i in range(n):
        points[i][0] = float(input('x['+str(i)+'] = '))
        points[i][1] = float(input('y['+str(i)+'] = '))
    xx = float(input('Enter interpolation point: '))
    return points, xx


def lagrange_interpolation(points, xx):
    sum = 0
    for i in range(len(points)):
        cur_y = points[i][1]
        cur_x = points[i][0]
        for j in range(len(points)):
            cur_y = cur_y*(xx - points[j][0])/(cur_x-points[j][0]) if i != j else cur_y
        sum += cur_y
    return sum


def demonstration():
    points, xx = user_input()
    yy = lagrange_interpolation(points, xx)
    print('x['+str(len(points))+'] = ' + str(yy))
    points = np.vstack((points, [xx, yy]))
    X = np.linspace(np.min(points[:, 0]), np.max(points[:, 0]))
    plt.plot(points[:, 0], points[:, 1], 'bo', X, [lagrange_interpolation(points, i) for i in X], 'k')
    plt.show()


if __name__ == "__main__":
    demonstration()



# points = np.array([[4, 6], [5, 7], [6, 8], [7, 9], [8, 10]])