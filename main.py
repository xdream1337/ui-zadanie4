import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, color):
        self.coords = (x, y)
        self.color = color
        self.euclidean_distance = 0

def classify(x, y, k):

    # zistujem vzdialenosti bodov od sucasneho bodu
    for j in range(n_data):
        color_data[j].euclidean_distance = math.sqrt(((x-color_data[j].coords[0]) ** 2) + ((y-color_data[j].coords[1]) ** 2))
    
    # zoradim si body podla vzdialenosti
    sorted_training_data = sorted(color_data, key=lambda x: x.euclidean_distance)
    
    r_count, g_count, b_count, p_count = 0, 0, 0, 0

    # vypocitam K susedov
    for j in range(k):
        if sorted_training_data[j].color == "red":
            r_count += 1
        elif sorted_training_data[j].color == "green":
            g_count += 1
        elif sorted_training_data[j].color == "blue":
            b_count += 1
        elif sorted_training_data[j].color == "purple":
            p_count += 1

    # zistim ktora farba prevlada
    color = max(r_count, g_count, b_count, p_count)

    # klasifikujem bod na zaklade poctu susedov
    if color == r_count:
        color_data.append(Point(x, y, "red"))
        return "red"

    elif color == g_count:
        color_data.append(Point(x, y, "green"))
        return "green"

    elif color == b_count:
        color_data.append(Point(x, y, "blue"))
        return "blue"

    elif color == p_count:
        color_data.append(Point(x, y, "purple"))
        return "purple"


# generovanie pociatocnych bodov
def extend_by_init_points():
    return Point(-4500, -4400, "red"), Point(-4100, -3000, "red"), Point(-1800, -2400, "red"), Point(-2500, -3400, "red"),Point(-2000, -1400, "red"),Point(+4500, -4400, "green"),Point(+4100, -3000, "green"),Point(+1800, -2400, "green"),Point(+2500, -3400, "green"),Point(+2000, -1400, "green"),Point(-4500, +4400, "blue"),Point(-4100, +3000, "blue"),Point(-1800, +2400, "blue"),Point(-2500, +3400, "blue"),Point(-2000, +1400, "blue"),Point(+4500, +4400, "purple"),Point(+4100, +3000, "purple"),Point(+1800, +2400, "purple"),Point(+2500, +3400, "purple"),Point(+2000, +1400, "purple"),


N_COLOR = int(input("Zadajte pocet bodov pre JEDNU FARBU na generovanie: "))
N_POINTS = N_COLOR * 4 + 20
print("Pocet vsetkych bodov je:", N_POINTS)

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
        
        # ochrana proti generovaniu duplicitnych bodov
        while point in points:
            coords = (random.randint(x1, x2), random.randint(y1, y2))
            point = Point(coords[0], coords[1], color)
            
        points.append(point)
    
    return points

# generacia bodov
red_points_99 = generate_n_color_points(N_COLOR, "red", 99)
green_points_99 = generate_n_color_points(N_COLOR, "green", 99)
blue_points_99 = generate_n_color_points(N_COLOR, "blue", 99)
purple_points_99 = generate_n_color_points(N_COLOR, "purple", 99)
red_points_1 = generate_n_color_points(N_COLOR, "red", 1)
green_points_1 = generate_n_color_points(N_COLOR, "green", 1)
blue_points_1 = generate_n_color_points(N_COLOR, "blue", 1)
purple_points_1 = generate_n_color_points(N_COLOR, "purple", 1)


# nastavenie matplotlibu
plt.xlim(-5000, 5000)
plt.ylim(-5000, 5000)
plt.yticks(np.arange(-5000, 6000, 1000))
plt.yticks(np.arange(-5000, 6000, 1000))
figure, axis = plt.subplots(2, 2)
plt.suptitle('KNN algoritmus, pocet bodov:' + str(N_POINTS))

knn_values = [1, 3, 7, 15]
colors = ["red", "green", "blue", "purple"]

# zaciatok samotnej generacie
for i in range(len(knn_values)):
    print("Zacinam generovat body pre K:", knn_values[i])
    last_color = ""
    
    start = time.time()

    assigned = 0
    color_data = []
    color_data.extend(extend_by_init_points())
    n_data = len(color_data)
    fault_colors = 0

    red_points, blue_points, green_points, purple_points = 0, 0, 0, 0
    
    while True:
        if red_points == blue_points == green_points == purple_points == N_COLOR:
            break
        
        while True:
            color = random.choice(colors)
            if color != last_color:
                break
            
        if random.random() < 0.99:
            percentage = 99
        else:
            percentage = 1
            
        if color == "red":
            if red_points < N_COLOR:
                red_point = red_points_99[red_points] if percentage == 99 else red_points_1[red_points]
                red_points += 1
                classified_color = classify(red_point.coords[0], red_point.coords[1], knn_values[i])
                n_data += 1
            else:
                last_color = color
                continue
        if color == "green":
            if green_points < N_COLOR:
                green_point = green_points_99[green_points] if percentage == 99 else green_points_1[green_points]
                green_points += 1
                classified_color = classify(green_point.coords[0], green_point.coords[1], knn_values[i])
                n_data += 1
            else:
                last_color = color
                continue
        if color == "blue":
            if blue_points < N_COLOR:
                blue_point = blue_points_99[blue_points] if percentage == 99 else blue_points_1[blue_points]
                blue_points += 1
                classified_color = classify(blue_point.coords[0], blue_point.coords[1], knn_values[i])
                n_data += 1
            else:
                last_color = color
                continue
        if color == "purple":
            if purple_points < N_COLOR:
                purple_point = purple_points_99[purple_points] if percentage == 99 else purple_points_1[purple_points]
                purple_points += 1
                classified_color = classify(purple_point.coords[0], purple_point.coords[1], knn_values[i])
                n_data += 1
            else:
                last_color = color
                continue

        if classified_color != color:
            fault_colors += 1
        last_color = classified_color

    end = time.time()

    for data in color_data:
        if knn_values[i] == 1:
            axis[0, 0].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axis[0, 0].set_title('K:' + str(knn_values[i]))
            axis[0, 0].set(xlabel='Took: ' + "{:0.2f}".format(end-start) + "sec, success rate: " + "{:0.2f}%".format(100-(fault_colors*100)/N_POINTS))
        if knn_values[i] == 3:
            axis[0, 1].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axis[0, 1].set_title('K:' + str(knn_values[i]))
            axis[0, 1].set(xlabel='Took: ' + "{:0.2f}".format(end-start) + "sec, success rate: " + "{:0.2f}%".format(100-(fault_colors*100)/N_POINTS))
        if knn_values[i] == 7:
            axis[1, 0].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axis[1, 0].set_title('K:' + str(knn_values[i]))
            axis[1, 0].set(xlabel='Took: ' + "{:0.2f}".format(end-start) + "sec, success rate: " + "{:0.2f}%".format(100-(fault_colors*100)/N_POINTS))
        if knn_values[i] == 15:
            axis[1, 1].plot(data.coords[0], data.coords[1], marker="o", color=data.color)
            axis[1, 1].set_title('K:' + str(knn_values[i]))
            axis[1, 1].set(xlabel='Took: ' + "{:0.2f}".format(end-start) + "sec, success rate: " + "{:0.2f}%".format(100-(fault_colors*100)/N_POINTS))
    
    print("Generacia bodov pre K:", knn_values[i], "bola uspesna!")

print("Ukladam grafy...")    
figure.tight_layout()
plt.savefig("vygenerovane_knn_grafy_n" + str(N_COLOR))
print("Grafy uspesne ulozene!")
