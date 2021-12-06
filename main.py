import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, color):
        self.coords = (x, y)
        self.colour = color
        self.euclidean_distance = -1


def classify(x, y, k):
    global number_of_training_data
    global final_data

    for j in range(number_of_training_data):
        training_data[j].distance = math.sqrt(((x-training_data[j].x) ** 2) + ((y-training_data[j].y) ** 2))
    # calculates distances

    sorted_training_data = sorted(training_data, key=lambda z: z.distance)
    # sort data by distance from lowest to highest

    r_count = 0
    g_count = 0
    b_count = 0
    p_count = 0

    for j in range(k):
        if sorted_training_data[j].colour == "red":
            r_count += 1
        elif sorted_training_data[j].colour == "green":
            g_count += 1
        elif sorted_training_data[j].colour == "blue":
            b_count += 1
        elif sorted_training_data[j].colour == "purple":
            p_count += 1

    final_colour = max(r_count, g_count, b_count, p_count)

    if final_colour == r_count:
        final_data.append(Point(x, y, "red"))
        training_data.append(Point(x, y, "red"))
        return "red"

    elif final_colour == g_count:
        final_data.append(Point(x, y, "green"))
        training_data.append(Point(x, y, "green"))
        return "green"

    elif final_colour == b_count:
        final_data.append(Point(x, y, "blue"))
        training_data.append(Point(x, y, "blue"))
        return "blue"

    elif final_colour == p_count:
        final_data.append(Point(x, y, "purple"))
        training_data.append(Point(x, y, "purple"))
        return "purple"


N_COLOR = 5000
print("Pocet bodov je:", N_COLOR * 4 + 20)

R1 = Point(-4500, -4400, "red")
R2 = Point(-4100, -3000, "red")
R3 = Point(-1800, -2400, "red")
R4 = Point(-2500, -3400, "red")
R5 = Point(-2000, -1400, "red")

G1 = Point(+4500, -4400, "green")
G2 = Point(+4100, -3000, "green")
G3 = Point(+1800, -2400, "green")
G4 = Point(+2500, -3400, "green")
G5 = Point(+2000, -1400, "green")

B1 = Point(-4500, +4400, "blue")
B2 = Point(-4100, +3000, "blue")
B3 = Point(-1800, +2400, "blue")
B4 = Point(-2500, +3400, "blue")
B5 = Point(-2000, +1400, "blue")

P1 = Point(+4500, +4400, "purple")
P2 = Point(+4100, +3000, "purple")
P3 = Point(+1800, +2400, "purple")
P4 = Point(+2500, +3400, "purple")
P5 = Point(+2000, +1400, "purple")

final_data = []
training_data = []
training_data.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
final_data.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))


def generate_n_color_points(n, color, percentage):
    points = []
    
    if percentage == 99:
        if color == "red":
            x1,x2 = -5000,499
            y1,y2 = -5000,499
        elif color == "green":
            x1,x2 = -499,5000
            y1,y2 = -5000,499
        elif color == "blue":
            x1,x2 = -5000,499
            y1,y2 = -499,5000
        elif color == "purple":
            x1,x2 = -499,5000
            y1,y2 = -499,5000
    elif percentage == 1:
        if color == "red":
            x1,x2 = 500,5000
            y1,y2 = 500,5000
        elif color == "green":
            x1,x2 = -5000,-500
            y1,y2 = 500,5000
        elif color == "blue":
            x1,x2 = 500,5000
            y1,y2 = -5000,-500
        elif color == "purple":
            x1,x2 = -5000,-500
            y1,y2 = -5000,-500
    
    for i in range(n):
        coords = (random.randint(x1, x2), random.randint(y1, y2))
        point = Point(coords[1], coords[2], color)
        while point in points:
            coords = (random.randint(x1, x2), random.randint(y1, y2))
            point = Point(coords[1], coords[2], color)
        points.append(point)
    
    return points

red_points_99 = generate_n_color_points(N_COLOR, "red", 99)
green_points_99 = generate_n_color_points(N_COLOR, "green", 99)
blue_points_99 = generate_n_color_points(N_COLOR, "blue", 99)
purple_points_99 = generate_n_color_points(N_COLOR, "purple", 99)

red_points_1 = generate_n_color_points(N_COLOR, "red", 1)
green_points_1 = generate_n_color_points(N_COLOR, "green", 1)
blue_points_1 = generate_n_color_points(N_COLOR, "blue", 1)
purple_points_1 = generate_n_color_points(N_COLOR, "purple", 1)



# set plot canvas
plt.xlim(-5000, 5000)
plt.ylim(-5000, 5000)
plt.yticks(np.arange(-5000, 6000, 1000))
plt.yticks(np.arange(-5000, 6000, 1000))
plt.xlabel("X")
plt.ylabel("Y")
fig, axs = plt.subplots(2, 2)
plt.suptitle('KNN algorithm')

pole_knn = [1, 3, 7, 15]
for i in range(4):
    color_list = ["red", "green", "blue", "purple"]
    last_assigned = ""
    number_of_training_data = 20
    training_data = []
    training_data.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
    start = time.time()

    assigned = 0
    final_data = []
    final_data.extend((R1, R2, R3, R4, R5, G1, G2, G3, G4, G5, B1, B2, B3, B4, B5, P1, P2, P3, P4, P5))
    fault = 0
    # sem zacinam robit
    r = 0
    g = 0
    b = 0
    p = 0
    red_count = 0
    blue_count = 0
    green_count = 0
    purple_count = 0

    while True:
        if red_count == blue_count == green_count == purple_count == NUMBER:
            break

        x_coordinate = 0
        y_coordinate = 0

        while True:
            random_number = random.randint(0, 3)
            color = color_list[random_number]
            if red_count or blue_count or green_count or purple_count == 10000:
                break
            if color != last_assigned:
                break

        if random.random() < 0.99:
            if color == "red":
                if red_count != NUMBER:
                    red_pop = red[r]
                    x_coordinate = red_pop.x
                    y_coordinate = red_pop.y
                    red_count += 1
                    r += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
            if color == "green":
                if green_count != NUMBER:
                    green_pop = green[g]
                    x_coordinate = green_pop.x
                    y_coordinate = green_pop.y
                    green_count += 1
                    g += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
            if color == "blue":
                if blue_count != NUMBER:
                    blue_pop = blue[b]
                    x_coordinate = blue_pop.x
                    y_coordinate = blue_pop.y
                    blue_count += 1
                    b += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
            if color == "purple":
                if purple_count != NUMBER:
                    purple_pop = purple[p]
                    x_coordinate = purple_pop.x
                    y_coordinate = purple_pop.y
                    purple_count += 1
                    p += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1

        else:
            if color == "red":
                if red_count != NUMBER:
                    red_pop = red_wrong[r]
                    x_coordinate = red_pop.x
                    y_coordinate = red_pop.y
                    red_count += 1
                    r += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
            if color == "green":
                if green_count != NUMBER:
                    green_pop = green_wrong[g]
                    x_coordinate = green_pop.x
                    y_coordinate = green_pop.y
                    green_count += 1
                    g += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
            if color == "blue":
                if blue_count != NUMBER:
                    blue_pop = blue_wrong[b]
                    x_coordinate = blue_pop.x
                    y_coordinate = blue_pop.y
                    blue_count += 1
                    b += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
            if color == "purple":
                if purple_count != NUMBER:
                    purple_pop = purple_wrong[p]
                    x_coordinate = purple_pop.x
                    y_coordinate = purple_pop.y
                    purple_count += 1
                    p += 1
                    assigned = classify(x_coordinate, y_coordinate, pole_knn[i])
                    number_of_training_data += 1
        if assigned != color:
            fault += 1
        last_assigned = assigned

    print("pocet chyb je: ", fault)
    end = time.time()
    print("time elapsed:", end - start)

    x_2D_list = []
    y_list = []
    for data in final_data:

        if pole_knn[i] == 1:
            axs[0, 0].plot(data.x, data.y, marker="o", color=data.colour)
            axs[0, 0].set_title(pole_knn[i])
        if pole_knn[i] == 3:
            axs[0, 1].plot(data.x, data.y, marker="o", color=data.colour)
            axs[0, 1].set_title(pole_knn[i])
        if pole_knn[i] == 7:
            axs[1, 0].plot(data.x, data.y, marker="o", color=data.colour)
            axs[1, 0].set_title(pole_knn[i])
        if pole_knn[i] == 15:
            axs[1, 1].plot(data.x, data.y, marker="o", color=data.colour)
            axs[1, 1].set_title(pole_knn[i])
fig.tight_layout()
plt.savefig("knn")


print("koniec")