import numpy as np

def features_matrix(map_height_matrix, pixel_length, number_of_features):
    height, width = map_height_matrix.shape
    natural_increasing = 100

    features_matrix = np.zeros((height*width, number_of_features))
    map_height_list = map_height_matrix.flatten()
    features_matrix[:,0] = map_height_list
    
    north_border = map_height_matrix[0,:]
    biased_north_matrix = np.delete(map_height_matrix, height - 1, axis=0)
    biased_north_matrix = np.insert(biased_north_matrix, 0, north_border, axis=0)
    north_angle_matrix = (biased_north_matrix - map_height_matrix) / pixel_length * natural_increasing
    north_angle_list = north_angle_matrix.flatten()
    features_matrix[:,1] = north_angle_list
    
    south_border = map_height_matrix[height - 1,:]
    biased_south_matrix = np.delete(map_height_matrix, 0, axis=0)
    biased_south_matrix = np.insert(biased_south_matrix, height - 1, south_border, axis=0)
    south_angle_matrix = (biased_south_matrix - map_height_matrix) / pixel_length * natural_increasing
    south_angle_list = south_angle_matrix.flatten()
    features_matrix[:,2] = south_angle_list
    
    west_border = map_height_matrix[:,width - 1]
    biased_west_matrix = np.delete(map_height_matrix, 0, axis=1)
    biased_west_matrix = np.insert(biased_west_matrix, width - 1, west_border, axis=1)
    west_angle_matrix = (biased_west_matrix - map_height_matrix) / pixel_length * natural_increasing
    west_angle_list = west_angle_matrix.flatten()
    features_matrix[:,3] = west_angle_list
    
    east_border = map_height_matrix[:,0]
    biased_east_matrix = np.delete(map_height_matrix, width - 1, axis=1)
    biased_east_matrix = np.insert(biased_east_matrix, 0, east_border, axis=1)
    east_angle_matrix = (biased_east_matrix - map_height_matrix) / pixel_length * natural_increasing
    east_angle_list = east_angle_matrix.flatten()
    features_matrix[:,4] = east_angle_list      
    
    np.savetxt('features.txt', features_matrix, fmt='%.10f')
    return features_matrix
