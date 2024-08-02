import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


def initialize_means(img, clusters):
	points = img.reshape((-1, img.shape[2]))
	m, n = points.shape

	means = np.zeros((clusters, n))
	for i in range(clusters):
		rand_indices = np.random.choice(m, size=10, replace=False)
		means[i] = np.mean(points[rand_indices], axis=0)

	return points, means


def distance(x1, y1, x2, y2):
	dist = np.square(x1 - x2) + np.square(y1 - y2)
	dist = np.sqrt(dist)
	return dist


def k_means(points, means, clusters, iterations):
	m, n = points.shape
	index = np.zeros(m)
	while iterations > 0:
		for j in range(m):
			min_dist = float('inf')
			temp = None

			for k in range(clusters):
				x1, y1 = points[j, 0], points[j, 1]
				x2, y2 = means[k, 0], means[k, 1]

				if distance(x1, y1, x2, y2) <= min_dist:
					min_dist = distance(x1, y1, x2, y2)
					temp = k
					index[j] = k

		for k in range(clusters):
			cluster_points = points[index == k]
			if len(cluster_points) > 0:
				means[k] = np.mean(cluster_points, axis=0)

		iterations -= 1

	return means, index



def compress_image(means, index, img):
	centroid = np.array(means)
	recovered = centroid[index.astype(int), :]
	recovered = recovered.reshape(img.shape)
	plt.imshow(recovered)
	plt.show()
	cv2.imwrite('compressed_scene.jpg', recovered)



