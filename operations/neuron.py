import csv
import random
import numpy as np


def open_csv(csv_path, tolerance, eta, iterations):

    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        matrix = np.array([row for row in reader]).astype(float)
        yd = np.array(matrix[:, -1]).reshape(-1, 1).astype(int)
        norm_e_by_iterations = []
        w_by_iterations = []
        w = initialize_w(matrix)
        w_by_iterations.append(w)

        for i in range(int(iterations)):
            u = get_u(w, matrix)
            yc = activation_function(u)
            e = obtain_error(yd, yc)
            delta_w = calculate_delta_w(int(eta), e, matrix)
            norm_e_by_iterations.append(obtain_norm_e(e))
            w = update_w(w, delta_w)
            w_by_iterations.append(w)

        print("Hecho")
        return w_by_iterations, norm_e_by_iterations


def initialize_w(matrix):
    w = []
    for _ in range(matrix.shape[1] - 1):
        w.append([random.random()])

    return np.array(w)


def get_u(w, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    return np.dot(x, w)


def activation_function(u):
    return np.where(u >= 0, 1, 0).astype(int)


def obtain_error(yd, yc):
    return yd - yc


def obtain_norm_e(e):
    return np.linalg.norm(e)


def calculate_delta_w(eta, e, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    return -eta * np.dot(e.T, x)


def update_w(w, delta_w):
    return w + delta_w
