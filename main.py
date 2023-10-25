from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from sklearn_som.som import SOM

from cutting_white_borders import cutting_white_borders
from height_matrix import height_matrix
from features_matrix import features_matrix
from cluster_analysing import cluster_analysing
from PCA import PCA
from saving_images import saving_images


def figure_drawing(selected_dimensions_case, projection_on_dimensions):
    if selected_dimensions_case == 0:
        print('Drawing fig 1...')
        plt.figure(1)
        plt.plot(projection_on_dimensions[:,0], projection_on_dimensions[:,1], 'r.')
        plt.xlabel(r'$Z_1$')
        plt.ylabel(r'$Z_2$')
        plt.title(r'$Projections$ $Z_1$ $Z_2$')
        plt.grid(True)
    elif selected_dimensions_case == 1:
        print('Drawing fig 2...')
        plt.figure(2)
        plt.plot(projection_on_dimensions[:,0], projection_on_dimensions[:,2], 'b.')
        plt.xlabel(r'$Z_1$')
        plt.ylabel(r'$Z_3$')
        plt.title(r'$Projections$ $Z_1$ $Z_3$')
        plt.grid(True)
    elif selected_dimensions_case == 2:
        print('Drawing fig 3...')
        plt.figure(3)
        plt.plot(projection_on_dimensions[:,1], projection_on_dimensions[:,2], 'g.')
        plt.xlabe(r'$Z_2$')
        plt.ylabel(r'$Z_3$')
        plt.title(r'$Projections$ $Z_2$ $Z_3$')
        plt.grid(True)
    else:
        print('No selected dimesions case...')


def scat(selected_dimensions_case, number_of_objects, number_of_features, projection_on_dimensions, index_list, predictions, map_features_matrix, k):
    cluster = np.zeros((number_of_objects, number_of_features))
    fig4, ax4 = plt.subplots()
    for i in range(number_of_objects):
         if   (predictions[i] == k):
             ax4.scatter(projection_on_dimensions[i,index_list[selected_dimensions_case,0]], projection_on_dimensions[i,index_list[selected_dimensions_case,1]], c = [generate_random_color()], marker = '.')
             cluster[i] = map_features_matrix[i]

    if selected_dimensions_case == 0:
        plt.xlabel(r'$Z_1$')
        plt.ylabel(r'$Z_2$')
        plt.title(r'$Clusters$')
        plt.grid(True)
    elif selected_dimensions_case == 1:
        plt.xlabel(r'$Z_1$')
        plt.ylabel(r'$Z_3$')
        plt.title(r'$Clusters$')
        plt.grid(True)
    elif selected_dimensions_case == 2:
        plt.xlabel(r'$Z_2$')
        plt.ylabel(r'$Z_3$')
        plt.title(r'$Clusters$')
        plt.grid(True)


#Step 1

image_map_RGB = Image.open('Map_Cutting\Actual_Map.tif')
image_map = image_map_RGB.convert('L')
image_map = np.array(image_map)
bw_map_image = cutting_white_borders(image_map)
bw_map_image.save("Map_Cutting\Actual_Map.tif")

#Step 2

illustration = True
min_height = -41 
max_height = 354
pixel_length = 70
number_of_features = 5
map_height_matrix = height_matrix(bw_map_image, min_height, max_height)
map_features_matrix = features_matrix(map_height_matrix, pixel_length, number_of_features)

#Step 3

map_height_matrix = np.loadtxt('height_matrix.txt')
map_features_matrix = np.loadtxt('features.txt')
average_features_of_data = map_features_matrix.mean(axis = 0)
np.savetxt('Average_features_of_data.txt', average_features_of_data)
number_of_objects, number_of_features = map_features_matrix.shape
projection_on_dimensions = np.loadtxt('PCA_features_3.txt')

#Step 4

norm_features_matrix, projection_on_dimensions = PCA(map_features_matrix)
index_list = np.array([[0,1],[0,2],[1,2]])
selected_dimensions_case = 0

struct = 2
neuron = 5
network_size = struct*neuron

print("Creating SOM...")
som = SOM(m=neuron, n=struct, dim=number_of_features)
som.fit(map_features_matrix)
predictions = som.predict(map_features_matrix)
print("Saving Predictions...")
np.savetxt('Predictions.txt', predictions, fmt='%d')

predictions = np.loadtxt('Predictions.txt')
predictions_matrix = np.reshape(predictions, (len(map_height_matrix[:,0]), len(map_height_matrix[0,:])))
np.savetxt('Predictions_matrix.txt', predictions_matrix)

#Step 5

saving_images(network_size, image_map_RGB, predictions_matrix)


plt.show()

    
