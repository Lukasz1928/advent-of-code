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
single_channel_img = np.zeros((height, width), dtype=np.int)
for x in range(height):
    for y in range(width):
        layer_id = 0
        color = 2
        while layer_id < layers_count and img[layer_id][x][y] == 2:
            layer_id += 1
        if layer_id < layers_count:
            color = img[layer_id][x][y]
        single_channel_img[x][y] = color
for x in range(height):
    for y in range(width):
        print(" " if single_channel_img[x][y] == 0 else "#", end='')
    print()
