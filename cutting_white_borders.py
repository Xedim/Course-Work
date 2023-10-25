from PIL import Image
import numpy as np

def cutting_white_borders(image_array):
    a = np.zeros((2))
    b = np.zeros((2))

    height, width = image_array.shape
    tr_1 = 0
    tr_2 = 0

    for i in range(height):
        for j in range(width):
            if image_array[i,j] != 255:
                a = np.array([i,j])
                tr_1 = 1
                break
        if tr_1 == 1:
            break

    for i in range(height - 1, -1, -1):
        for j in range(width - 1, -1, -1):
            if image_array[i,j] != 255:
                b = np.array([i + 1,j + 1])
                tr_2 = 1
                break
        if tr_2 == 1:
            break

    print(a)
    print(b)
    
    real_map_image = Image.new("L", (b[1] - a[1], b[0] - a[0]))
    for y in range(a[1], b[1]):
        for x in range(a[0], b[0]):
            real_map_image.putpixel((y - a[1], x - a[0]), int(image_array[x, y].item()))


    return real_map_image
