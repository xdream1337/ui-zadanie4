import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, color):
        self.coords = (x, y)
        self.color = color
        self.euclidean_distance = -1


def classify(x, y, k):
    global number_of_training_data
    global final_data

    for j in range(number_of_training_data):
        final_data[j].euclidean_distance = math.sqrt(((x-final_data[j].coords[0]) ** 2) + ((y-final_data[j].coords[1]) ** 2))
    # calculates distances

    sorted_training_data = sorted(final_data, key=lambda z: z.euclidean_distance)
    # sort data by distance from lowest to highest

    r_count = 0
    g_count = 0
    b_count = 0
    p_count = 0

    for j in range(k):
        if sorted_training_data[j].color == "red":
            r_count += 1
        elif sorted_training_data[j].color == "green":
            g_count += 1
        elif sorted_training_data[j].color == "blue":
            b_count += 1
        elif sorted_training_data[j].color == "purple":
            p_count += 1

    final_colour = max(r_count, g_count, b_count, p_count)

    if final_colour == r_count:
        final_data.append(Point(x, y, "red"))
        return "red"

    elif final_colour == g_count:
        final_data.append(Point(x, y, "green"))
        return "green"

    elif final_colour == b_count:
        final_data.append(Point(x, y, "blue"))
        return "blue"

    elif final_colour == p_count:
        final_data.append(Point(x, y, "purple"))
        return "purple"


N_COLOR = 5000
print("Pocet bodov je:", N_COLOR * 4 + 20)


def extend_by_init_points():
    return Point(-4500, -4400, "red"), Point(-4100, -3000, "red"), Point(-1800, -2400, "red"), Point(-2500, -3400, "red"),Point(-2000, -1400, "red"),Point(+4500, -4400, "green"),Point(+4100, -3000, "green"),Point(+1800, -2400, "green"),Point(+2500, -3400, "green"),Point(+2000, -1400, "green"),Point(-4500, +4400, "blue"),Point(-4100, +3000, "blue"),Point(-1800, +2400, "blue"),Point(-2500, +3400, "blue"),Point(-2000, +1400, "blue"),Point(+4500, +4400, "purple"),Point(+4100, +3000, "purple"),Point(+1800, +2400, "purple"),Point(+2500, +3400, "purple"),Point(+2000, +1400, "purple"),

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
        point = Point(coords[0], coords[1], color)
        while point in points:
            coords = (random.randint(x1, x2), random.randint(y1, y2))
            point = Point(coords[0], coords[1], color)
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
    start = time.time()

    assigned = 0
    final_data = []
    final_data.extend(extend_by_init_points())
    fault = 0
    
    # sem zacinam robit
    red_points, blue_points, green_points, purple_points = 0, 0, 0, 0
    
    #print('zacinam robit...')
    
    while True:
        if red_points == blue_points == green_points == purple_points == N_COLOR:
            break
        
        while True:
            color = random.choice(color_list)
            
            if color != last_assigned:
                break
            

        if random.random() < 0.99:
            percentage = 99
        else:
            percentage = 1
            
        if color == "red":
            if red_points < N_COLOR:
                red_point = red_points_99[red_points] if percentage == 99 else red_points_1[red_points]
                red_points += 1
                assigned = classify(red_point.coords[0], red_point.coords[1], pole_knn[i])
                number_of_training_data += 1
            else:
                last_assigned = color
                continue
        if color == "green":
            if green_points < N_COLOR:
                green_point = green_points_99[green_points] if percentage == 99 else green_points_1[green_points]
                green_points += 1
                assigned = classify(green_point.coords[0], green_point.coords[1], pole_knn[i])
                number_of_training_data += 1
            else:
                last_assigned = color
                continue
        if color == "blue":
            if blue_points < N_COLOR:
                blue_point = blue_points_99[blue_points] if percentage == 99 else blue_points_1[blue_points]
                blue_points += 1
                assigned = classify(blue_point.coords[0], blue_point.coords[1], pole_knn[i])
                number_of_training_data += 1
            else:
                last_assigned = color
                continue
        if color == "purple":
            if purple_points < N_COLOR:
                purple_point = purple_points_99[purple_points] if percentage == 99 else purple_points_1[purple_points]
                purple_points += 1
                assigned = classify(purple_point.coords[0], purple_point.coords[1], pole_knn[i])
                number_of_training_data += 1
            else:
                last_assigned = color
                continue

        if assigned != color:
            fault += 1
        last_assigned = assigned

    print("pocet chyb je: ", fault)
    end = time.time()
    print("time elapsed:", end - start)

    for data in final_data:
        if pole_knn[i] == 1:
            axs[0, 0].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axs[0, 0].set_title(pole_knn[i])
        if pole_knn[i] == 3:
            axs[0, 1].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axs[0, 1].set_title(pole_knn[i])
        if pole_knn[i] == 7:
            axs[1, 0].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axs[1, 0].set_title(pole_knn[i])
        if pole_knn[i] == 15:
            axs[1, 1].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axs[1, 1].set_title(pole_knn[i])
fig.tight_layout()
plt.savefig("knn")


print("koniec")