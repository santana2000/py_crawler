# np.meshgrid函数
import numpy as np

points = np.arange(-5,5,0.1)
xs, ys = np.meshgrid(points, points)
