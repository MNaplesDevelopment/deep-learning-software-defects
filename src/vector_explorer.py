import numpy as np
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

with open("py2vec\py2vec_model3.pkl", "rb") as f:
    embeddings = pickle.load(f)
with open("py2vec\cen.pkl", "rb") as f:
     cen = pickle.load(f)
with open("py2vec\parray.pkl", "rb") as f:
    nparray = pickle.load(f)
with open("py2vec\index.pkl", "rb") as f:
    ndx = pickle.load(f)


def kmeans(data, k, num_iter, print_progress=True):
    """
    K-means clustering algorithm

    Input:
    data - 2D numpy array containing all the points
    k - Number of clusters
    num_iter - number of iterations

    Output:
    centroids - the locations of the centers of the clusters
    c - Equal to the size of the number of points and contains the
    integer representation of which cluster the point was assigned to
    """
    # c will contain the indexes representing the cluster each
    # point was assigned to.
    c = np.zeros(data.shape[0])

    # Randomly initialize the centroids (the center point of the clusters).
    centroids = np.random.rand(k, data.shape[1])

    # Main loop.
    for i in range(num_iter):
        # First operation: Iterate through every point and assign it to the
        # closest centroid.
        for j in range(data.shape[0]):
            # Min distance gets set to the distance of the first centroid, I find this more
            # robust than setting it to the minimum integer value or something similar.
            min_dist = np.sum((data[j, :] - centroids[0, :])**2)
            c[j] = 0
            for l in range(1, k):
                # Use a simple distance formula to calculate the distance
                # between the current point and current centroid.
                dist = np.sum((data[j, :] - centroids[l, :])**2)
                # If the centroid is closer to the current point, update the
                # min distance and the index in c.
                if dist < min_dist:
                    min_dist = dist
                    c[j] = l
        # Second operation: Move the centroids to the average location of all
        # points assigned to it.
        for j in range(k):
            # Store all the points that were assigned to the current cluster in clusters.
            clusters = np.where(c == j)
            # Average the location of the centroid by adding together all the points and
            # dividing by the number of points. This will slowly move the centroids until
            # they appropriately represent a cluster.
            #
            # NOTE: It is not uncommon for a centroid to have no points assigned to it and
            # so at this step you may see a divide by zero error, that is okay it just means
            # a centroid will not be clustered and you will end up with less clusters than requested.
            centroids[j, :] = np.sum(data[clusters, :], axis=1) / len(clusters[0])
        # Print progress.
        if i % 10 == 0 and print_progress:
            print(str(i))
    return centroids, c


def get_low_dim_embs(vectors):
    """
    t-SNE is a machine learning algorithm for visualizing data
    it transforms higher dimensional vectors into lower dimensions
    in a very non-linear way, preserving much of the information.

    Input:
    vectors - high dimensional vectors

    Output:
    2-D vectors
    """
    tsne = TSNE(
        perplexity=30, n_components=2, init='pca', n_iter=250)
    return tsne.fit_transform(vectors)


high_dim_embs = []
labels = []
# store vectors in high_dim_embs (high dimensional embeddings)
# and store each word in labels. It is imperative we preserve the order
# so that each word maps to its embedding by sharing the same index.
for key, value in embeddings.items():
    high_dim_embs.append(value)
    labels.append(key)

# Preform k-means clustering
nclusters = 20
# cen, ndx = kmeans(np.asarray(high_dim_embs), nclusters, 10)
# print(cen)


def plot_with_labels(words):
    """
    Plots every word embedding and labels only a list of specified words.

    Input:
    words - A list of words to be labeled.

    Output:
    None, but generates a matplotlib graph
    """
    ndx = []
    fig, ax = plt.subplots()
    # Search through the list of words and find their corresponding
    # index value.
    for word in words:
        for i in range(len(labels)):
            if labels[i] == word:
                ndx.append(i)
    # Plot all points
    ax.scatter(nparray[:, 0], nparray[:, 1], s=30, color='burlywood')
    # Label the specified words.
    for i in range(len(ndx)):
        ax.scatter(nparray[ndx[i], 0], nparray[ndx[i], 1], s=30, color='chartreuse')
        plt.text(nparray[ndx[i], 0], nparray[ndx[i], 1], words[i])
    # Display graph
    plt.show()

# plot_with_labels(['if', 'else', 'is', 'not', 'sin', 'cos', 'tan', 'power', 'np', 'shape', 'log', 'range', 'for'])


def plot_kmeans_clusters(n_clusters, label):
    """
    Visualize the k-means clustering. The maximum number of clusters is 20.

    Input:
    n_clusters - the number of clusters
    labels - Boolean value, True will label every 50th point.

    Output:
    None, but generates a graph.
    """
    # Bank of 20 colors.
    colors = ['DarkOrchid', 'DarkRed', 'DarkSlateBlue', 'ForestGreen', 'GoldenRod', 'MediumVioletRed',
              'MidnightBlue', 'SlateGrey', 'BurlyWood', 'Plum', 'MediumAquaMarine', 'RosyBrown',
              'Lime', 'MediumBlue', 'MediumSeaGreen', 'Olive', 'PaleVioletRed', 'y',
              'c', 'r']
    clusters = []
    fig, ax = plt.subplots()
    # Go through each cluster and plot all its associated points, coloring each cluster uniquely.
    for i in range(n_clusters):
        clusters.append(nparray[np.where(ndx == i)[0], :])
        ax.scatter(clusters[i][:, 0], clusters[i][:, 1], s=30, color=colors[i], label='Cluster ' + str(i))

    # Label every 50th words.
    if label:
        z = 0
        for i in range(nparray.shape[0]):
            plt.text(nparray[z][0], nparray[z][1], labels[z])
            z = z + 50
            if z >= nparray.shape[0]:
                break
    # Display graph.
    plt.show()


plot_kmeans_clusters(nclusters, True)
