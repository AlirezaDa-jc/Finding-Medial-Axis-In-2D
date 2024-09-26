import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import csv

# خواندن نقاط از فایل
def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            try:
                points.append([float(row[0]), float(row[1])])
            except ValueError:
                print(f"Skipping invalid row: {row}")
    return np.array(points)

# محاسبه محور میانی
def compute_medial_axis(points):
    vor = Voronoi(points)
    return vor

# نمایش گرافیکی نقاط و محور میانی
def plot_medial_axis(points, vor):
    plt.figure()
    plt.plot(points[:, 0], points[:, 1], 'o')
    voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=2, line_alpha=0.6, point_size=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Medial Axis of Points')
    plt.show()

# مسیر فایل ورودی
file_path = 'horse-2D.txt'  # فایل خود را اینجا قرار دهید

# خواندن نقاط
points = read_points(file_path)

# اطمینان از اینکه نقاط خوانده شده‌اند
if points.size == 0:
    print("No valid points found in the file.")
else:
    # محاسبه محور میانی
    vor = compute_medial_axis(points)

    # نمایش گرافیکی
    plot_medial_axis(points, vor)

