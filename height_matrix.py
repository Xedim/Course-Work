import numpy as np

def height_matrix(real_map_matrix, min_height, max_height):
    height, width = real_map_matrix.shape
    map_height_matrix = np.zeros((height, width))

    translation_koef = (max_height - min_height) / 255
    map_height_matrix = translation_koef * real_map_matrix + min_height

    np.savetxt('height_matrix.txt', map_height_matrix, fmt='%.10f')
    return map_height_matrix
