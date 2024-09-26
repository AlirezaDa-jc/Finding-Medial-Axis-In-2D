import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize
from skimage.draw import polygon
from skimage.util import invert

# خواندن نقاط از فایل
def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:  # اطمینان از داشتن حداقل دو مقدار
                x, y = map(float, parts[:2])
                points.append((x, y))
    return np.array(points)

# تولید تصویر باینری از نقاط
def create_binary_image(points, img_size):
    img = np.zeros(img_size, dtype=np.uint8)
    min_points = points.min(axis=0)
    max_points = points.max(axis=0)
    normalized_points = (points - min_points) / (max_points - min_points)
    scaled_points = (normalized_points * (np.array(img_size) - 1)).astype(int)
    # Create a mask using the polygon function
    rr, cc = polygon(scaled_points[:, 1], points[:, 0], img.shape)
    img[rr, cc] = 1
    return img

# محاسبه محور میانی
def compute_medial_axis(binary_image):
    skeleton = skeletonize(binary_image)
    return skeleton

# نمایش گرافیکی
def plot_medial_axis(points, medial_axis):
    plt.figure(figsize=(8, 8))
    plt.imshow(medial_axis, cmap='gray')
    plt.scatter(points[:, 0], points[:, 1], c='red', s=1)
    plt.title('Medial Axis')
    plt.gca().invert_yaxis()  # Invert the y-axis to match the expected orientation
    plt.axis('equal')
    plt.show()
# مسیر فایل ورودی
file_path = 'elephant.txt'  # فایل خود را اینجا قرار دهید

# خواندن نقاط
points = read_points(file_path)

# اندازه تصویر
img_size = (int(points[:, 1].max()) + 1, int(points[:, 0].max()) + 1)

# تولید تصویر باینری
binary_image = create_binary_image(points, img_size)

# محاسبه محور میانی
medial_axis = compute_medial_axis(binary_image)

# نمایش گرافیکی
plot_medial_axis(points, medial_axis)
