from utils import *


image=cv2.imread('scene.jpg')
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image=image/255.0

points, means=initialize_means(image, clusters=2)
means, index=k_means(points, means, clusters=2, iterations=10)
compress_image(means, index, image)
