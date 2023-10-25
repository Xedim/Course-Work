from PIL import Image

def saving_images(network_size, image_map_RGB, predictions_matrix):
    color_amount = 3
    RGB = np.loadtxt('RGB.txt')
    image_bw = image_map_RGB.convert('L')
    width, height = image_bw.size
    full_image_pixels = np.zeros((height, width, color_amount), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            full_image_pixels[y, x] = [int(image_bw.getpixel((x, y)))] * color_amount  

    for k in range(network_size):
        cluster_image_pixels = np.zeros((height, width, color_amount), dtype=np.uint8)
        for x in range(width):
            for y in range(height):
                cluster_image_pixels[y, x] = [int(image_bw.getpixel((x, y)))] * color_amount  
        R, G, B = RGB[k]
        print("a")
        for x in range(width):
            for y in range(height):
                if int(predictions_matrix[y, x]) == k:
                    cluster_image_pixels[y, x] = [int(R), int(G), int(B)]  
                    full_image_pixels[y, x] = [int(R), int(G), int(B)]
        print("aa")
        cluster_image_colored = Image.fromarray(cluster_image_pixels, 'RGB')
        cluster_image_colored.save(f"Cluster_Map\Cluster_{k+1}_map.png")
           
    full_image = Image.fromarray(full_image_pixels, 'RGB')
    full_image.save(f"Cluster_Map\Clusters_full_map.png")
