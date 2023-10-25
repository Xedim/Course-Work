import numpy as np
from scipy.stats import chi2

def PCA(features_matrix):
    mean_features = features_matrix.mean(axis = 0)
    std_features = features_matrix.std(axis = 0)
    print(mean_features)
    print(std_features)
    norm_features_matrix = (features_matrix - mean_features) / std_features
    nfm_height, nfm_width = norm_features_matrix.shape
    dimentions = 3

    Cov = np.dot(np.transpose(norm_features_matrix), norm_features_matrix) / (nfm_height - 1)
    np.savetxt('Cov.txt', Cov, fmt='%.3f')
    Cov_eigenvalues, Cov_eigenvectors = np.linalg.eig(Cov)
    np.savetxt('Cov_eigenvalues.txt', Cov_eigenvalues, fmt='%.10f')
    np.savetxt('Cov_eigenvectors.txt', Cov_eigenvectors, fmt='%.10f')

    Cov_descending_eigenvalues = -np.sort(-Cov_eigenvalues)
    Alpha = Cov_descending_eigenvalues / np.sum(Cov_descending_eigenvalues)
    Gamma = np.zeros(len(Cov_descending_eigenvalues))
    for i in range(len(Gamma)):
        for j in range(i + 1):
            Gamma[i] = Gamma[i] + Alpha[j]
    print("Alpha =", Alpha)
    print("Gamma =", Gamma)

    Sum_for_D = 0
    for i in range(nfm_width):
        for j in range(i):
            Sum_for_D = Sum_for_D + Cov[i][j] ** 2
    D_statistics = nfm_height * Sum_for_D
    Chi2_statistics = chi2.ppf(0.95, df = nfm_width * (nfm_width - 1) / 2) 
    print(D_statistics, " > ", Chi2_statistics, " = ", D_statistics > Chi2_statistics)


    projection = np.dot(norm_features_matrix, Cov_eigenvectors)
    projection_cov = np.dot(np.transpose(projection), projection) / (nfm_height - 1)
    print(projection_cov)
    np.savetxt('Projection_cov.txt', projection_cov, fmt='%.10f')

    Cov_eigenvectors_by_dimentions = []
    for i in range(dimentions):
        Cov_eigenvectors_by_dimentions.append(Cov_eigenvectors[:,i])
    Cov_tr_eigenvectors_by_dimentions = np.transpose(Cov_eigenvectors_by_dimentions)
    projection_on_dimensions = np.dot(norm_features_matrix, Cov_tr_eigenvectors_by_dimentions)
    np.savetxt('PCA_features_3.txt', projection_on_dimensions, fmt='%.10f')

    projection_sum_disp = np.sum(projection.std(axis = 0) ** 2)
    features_sum_disp = np.sum(std_features ** 2)

    print(features_sum_disp)
    print(projection_sum_disp)
    print(np.sum(norm_features_matrix.std(axis = 0) ** 2))
    print(Cov_eigenvalues)
    print(projection.std(axis = 0) ** 2)


    return norm_features_matrix, projection_on_dimensions
