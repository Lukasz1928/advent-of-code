import numpy as np

raw_img = [int(x) for x in open('input', 'r').read()]
width = 25
height = 6
layers_count = len(raw_img) // (width * height)
img = np.zeros((layers_count, height, width), dtype=np.int)
rx = 0
for l in range(layers_count):
    for x in range(height):
        for y in range(width):
            img[l][x][y] = raw_img[rx]
            rx += 1
layer_zeros = [(img[l] == 0).sum() for l in range(layers_count)]
layer_with_max_zeros = np.argmin(layer_zeros)
result = (img[layer_with_max_zeros] == 1).sum() * (img[layer_with_max_zeros] == 2).sum()
print(result)
