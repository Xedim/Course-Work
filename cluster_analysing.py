import numpy as np
import matplotlib.pyplot as plt

def generate_random_color():
    R = np.random.randint(0, 255)
    G = np.random.randint(0, 255)
    B = np.random.randint(0, 255)
    return R, G, B

def cluster_analysing(cluster, number_of_features, k, network_size, illustration):
    cluster_mean = np.zeros((network_size, number_of_features))
    fig5, ax5 = plt.subplots()
    if k == 0:
        mask = np.all(cluster != 0, axis=1)
        cluster_1 = cluster[mask]
        print("Saving ", "cluster_1", "...")
        np.savetxt("Clusters_Data\Cluster 1.txt", cluster_1, fmt='%.10f')
        #print("Cluster 1:\n", cluster_1)
        cluster_mean[k] = cluster_1.mean(axis = 0)
        print("Cluster 1 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_1.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $1$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 1:
        mask = np.all(cluster != 0, axis=1)
        cluster_2 = cluster[mask]
        print("Saving ", "cluster_2", "...")
        np.savetxt("Clusters_Data\Cluster 2.txt", cluster_2, fmt='%.10f')
        #print("Cluster 2:\n", cluster_2)
        cluster_mean[k] = cluster_2.mean(axis = 0)
        print("Cluster 2 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_2.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $2$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 2:
        mask = np.all(cluster != 0, axis=1)
        cluster_3 = cluster[mask]
        print("Saving ", "cluster_3", "...")
        np.savetxt("Clusters_Data\Cluster 3.txt", cluster_3, fmt='%.10f')
        #print("Cluster 3:\n", cluster_3)
        cluster_mean[k] = cluster_3.mean(axis = 0)
        print("Cluster 3 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_3.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $3$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 3:
        mask = np.all(cluster != 0, axis=1)
        cluster_4 = cluster[mask]
        print("Saving ", "cluster_4", "...")
        np.savetxt("Clusters_Data\Cluster 4.txt", cluster_4, fmt='%.10f')
        #print("Cluster 4:\n", cluster_4)
        cluster_mean[k] = cluster_4.mean(axis = 0)
        print("Cluster 4 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_4.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $4$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 4:
        mask = np.all(cluster != 0, axis=1)
        cluster_5 = cluster[mask]
        print("Saving ", "cluster_5", "...")
        np.savetxt("Clusters_Data\Cluster 5.txt", cluster_5, fmt='%.10f')
        #print("Cluster 5:\n", cluster_5)
        cluster_mean[k] = cluster_5.mean(axis = 0)
        print("Cluster 5 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_5.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $5$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 5:
        mask = np.all(cluster != 0, axis=1)
        cluster_6 = cluster[mask]
        print("Saving ", "cluster_6", "...")
        np.savetxt("Clusters_Data\Cluster 6.txt", cluster_6, fmt='%.10f')
        #print("Cluster 6:\n", cluster_6)
        cluster_mean[k] = cluster_6.mean(axis = 0)
        print("Cluster 6 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_6.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $6$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 6:
        mask = np.all(cluster != 0, axis=1)
        cluster_7 = cluster[mask]
        print("Saving ", "cluster_7", "...")
        np.savetxt("Clusters_Data\Cluster 7.txt", cluster_7, fmt='%.10f')
        #print("Cluster 7:\n", cluster_7)
        cluster_mean[k] = cluster_7.mean(axis = 0)
        print("Cluster 7 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_7.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $7$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 7:
        mask = np.all(cluster != 0, axis=1)
        cluster_8 = cluster[mask]
        print("Saving ", "cluster_8", "...")
        np.savetxt("Clusters_Data\Cluster 8.txt", cluster_8, fmt='%.10f')
        #print("Cluster 8:\n", cluster_8)
        cluster_mean[k] = cluster_8.mean(axis = 0)
        print("Cluster 8 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_8.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $8$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 8:
        mask = np.all(cluster != 0, axis=1)
        cluster_9 = cluster[mask]
        print("Saving ", "cluster_9", "...")
        np.savetxt("Clusters_Data\Cluster 9.txt", cluster_9, fmt='%.10f')
        #print("Cluster 9:\n", cluster_9)
        cluster_mean[k] = cluster_9.mean(axis = 0)
        print("Cluster 9 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_9.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $9$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
    if k == 9:
        mask = np.all(cluster != 0, axis=1)
        cluster_10 = cluster[mask]
        print("Saving ", "cluster_10", "...")
        np.savetxt("Clusters_Data\Cluster 10.txt", cluster_10, fmt='%.10f')
        #print("Cluster 10:\n", cluster_10)
        cluster_mean[k] = cluster_10.mean(axis = 0)
        print("Cluster 10 mean:\n",cluster_mean[k])
        np.savetxt('Cluster_Mean\Cluster_Mean_10.txt', cluster_mean[k], fmt='%.10f')
        if illustration != 0:
            ax5.plot(range(number_of_features), cluster_mean[k], c = [generate_random_color()], marker = '.')
            plt.xlabel(r'$Number$ $of$ $features$')
            plt.ylabel(r'$Cluster$ $10$ $Mean$')
            plt.title(r'$Mean$')
            plt.grid(True)
