import argparse
import matplotlib.pyplot as plt
import numpy as np
import string
import copy
from matplotlib import colors as mcolors
import random

# Constants
G = 6.67408e-11
au = 1.496e11


class Cell_Planetoid(object):

    def __init__(self, uid, name, position, velocity, mass, color, size):
        self.uid = uid
        self.name = name
        self.mass = mass
        self.color = color
        self.pos = np.asarray(position, dtype=float).copy()
        self.vel =  np.asarray(velocity, dtype=float).copy()
        self.acc =  np.asarray([0,0,0], dtype=float)
        self.size = size


def plot_paths(Bodies, paths, size):
    #plt.figure(figsize=(8, 8))
    plt.xlim(0,size)
    plt.ylim(0,size)
    for n, planet in enumerate(Bodies):
        px, py = np.array(paths[n]).T;
        print(px, py, planet.color, planet.size)
        plt.plot(px, py, color=planet.color, lw=planet.size+555)
    plt.show()
    return


def calculate_name(pos):
    name = ''
    for i in range(0,10):
        name += random.choice(string.ascii_letters)
    name = name.lower().capitalize() + "_"
    if len(str(pos[0])) != 2:
        name += "0" + str(pos[0])
    else:
        name += str(pos[0])

    if len(str(pos[1])) != 2:
        name += "0" + str(pos[1])
    else:
        name += str(pos[1])

    return name


def calculate_color(mass):
    if mass <= 10:
        color = "blue"
    elif mass <= 20:
        color = "blue"
    elif mass <= 30:
        color = "blue"
    elif mass <= 40:
        color = "blue"
    elif mass <= 50:
        color = "blue"
    elif mass <= 60:
        color = "blue"
    elif mass <= 70:
        color = "blue"
    elif mass <= 80:
        color = "blue"
    elif mass <= 90:
        color = "blue"
    elif mass <= 99:
        color = "blue"
    else:
        color = "black"
    return color


def initial_params(Number, map_size):
    Planetoids = []
    for i in range(Number):
        pos = [random.randint(5, map_size-5), random.randint(0, map_size), 0]
        vel = [random.randint(-10, 10), random.randint(-10, 10), 0]
        name = calculate_name(pos)
        mass = random.randint(0,100)
        size = mass/5.0
        color = calculate_color(mass)
        Planetoids.append(Cell_Planetoid(i, name, pos, vel, mass, color, size))
    return Planetoids


def calculate_forces(Planetoids):
    for Planetoid in Planetoids:
        Planetoid.acc *= 0
        for other in Planetoids:
            if (Planetoid ==  other):
                continue
            else:
                rx = Planetoid.pos - other.pos
                r3 = sum(rx**2)**1.5
                Planetoid.acc += -G*other.mass*rx/r3

    return Planetoids


def calculate_euler(Planetoids, Points, dt):
    for index, Planetoid in enumerate(Planetoids):
        Planetoid.vel += Planetoid.acc*dt
        Planetoid.pos += Planetoid.vel*dt
        Points.append(Planetoid.pos[:2].copy())
    return Planetoids, Points


def main():
    day = 60 * 60 * 24
    t = 0
    dt = 0.1

    parser = argparse.ArgumentParser(description='Process an image')
    parser.add_argument('-n', '--number', type=str, help='filepath and name')
    parser.add_argument("-s", '--size', type=str, help='what to do with image')
    parser.add_argument("-t", '--time', type=str, help='what to do with image')
    parser.add_argument("-m", '--method', type=str, help='what to do with image')
    parser.add_argument('-p', '--special', type=str, help='filepath and name')
    args = parser.parse_args()

    number = int(args.number)
    size = int(args.size)
    time = int(args.time)
    method = args.method
    sepcial = args.special

    Planetoids = initial_params(number, size)
    Points = [[p.pos[:2].copy()] for p in Planetoids]

    if method == 'euler':
        while t < time:
            print(t)
            Planetoids = calculate_forces(Planetoids)
            Planetoids, Points = calculate_euler(Planetoids, Points, dt)
            t += dt
        plot_paths(Planetoids, Points, size)

    elif method == 'rk4':
        print("1" + method)


if __name__ == "__main__":
    main()
"""
    if mass <= 10:
        color = "lichtcyan"
    elif mass <= 20:
        color = "aqua"
    elif mass <= 30:
        color = "lightskyblue"
    elif mass <= 40:
        color = "deepskyblue"
    elif mass <= 50:
        color = "royalblue"
    elif mass <= 60:
        color = "blue"
    elif mass <= 70:
        color = "navyblue"
    elif mass <= 80:
        color = "indigo"
    elif mass <= 90:
        color = "silver"
    elif mass <= 99:
        color = "grey"
    else:
        color = "black"

"""