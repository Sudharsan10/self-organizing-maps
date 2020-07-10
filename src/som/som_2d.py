# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Self Organising Maps
# Authors   :-> Sudharsan
# E-mail    :->  s10@terpmail.umd.edu

# ---------------------------------------------------------------------------------------------------------------------- #
# Import packages
# ---------------------------------------------------------------------------------------------------------------------- #
import numpy as np
from src.som.som import SOM


class SOM_2D(SOM):
    """
    SOM_2D is a Child class inheriting SOM parent class for performing 2D Self Organizing Maps algorithm implementation

    Functions:
        -> initializer()                : A function to initialise all the required parameters to perform 2D SOM fitting
        -> compute_neighbourhood_prob() : A function to compute the gaussian probability for neighbourhood in 2D
        -> fit()                        : A function to perform 1D SOM fitting to the given data
        -> save_data()                  : A function to set the object's save data flags
    """

    def __init__(self):
        super().__init__()
        self.MAP = None
        self.BMU = None
        self.dist = None
        self.data = None
        self.shapes = None
        self.output = None
        self.result = None
        self.weights = None
        self.data_dim = None
        self.data_set = None
        self.result_map = None
        self.neighborhood_prob = None

        self.N = 12
        self.lattice = np.arange(self.N)

        # -----> Hyper parameter Constants <----- #
        self.lr_const = 0.005
        self.epochs_const = 2000
        self.neighbors_radius_const = 10
        self.time_const = self.epochs_const / np.log(self.neighbors_radius_const)

    def initializer(self, data: np.array, output: np.array) -> None:
        """
        Initialize the SOM 2D object with the appropriate data

        Args:
            data: np.array
                Input data to train the SOM
            output: np.array
                Output data to classify to visualize the SOM

        Returns: None

        """
        self.data_dim = data.shape
        self.data = data
        self.data_set = data.copy()
        self.output = output
        self.weights = np.random.uniform(size=(self.N, self.N, data.shape[1]))
        self.shapes = self.weights.shape

    def hyperparameter_constants(self, lr_const: float = 0.005, epoch_const: int = 2000, neigh_radius_const: int = 10):
        """
        A function to set the hyperparameter constants

        Args:
            lr_const: float
                learning rate constant
            epoch_const: int
                total epoch const
            neigh_radius_const: int
                neighbor radius constant

        Returns: None

        """
        self.lr_const = lr_const
        self.epochs_const = epoch_const
        self.neighbors_radius_const = neigh_radius_const
        self.time_const = self.epochs_const / np.log(self.neighbors_radius_const)

    def find_euclidean_distance(self, X: np.array, Y: np.array, axis_val: int = 2 ) -> np.array:
        """
        Compute Euclidean Distance
        Args:
            axis_val: int
            X: np.array
            Y: np.array

        Returns: np.array

        """
        return np.linalg.norm(X - Y, axis=axis_val)

    def find_BMU(self, dist: np.array) -> np.array:
        """
        Compute the Best Matching Unit
        Args:
            dist: np.array
                An numpy array of euclidean distance

        Returns: np.array

        """
        return np.unravel_index(np.argmin(dist), dist.shape)

    def compute_neighborhood_prob(self, index: np.array, epoch: int) -> np.array:
        """
        Compute Neighborhood probability
        Args:
            index: np.array

            epoch: np.array

        Returns: np.array

        """
        sigma = self.compute_neighborhood_size(epoch)
        lateral_dist_x, lateral_dist_y = np.meshgrid(abs(self.lattice - index[0]), abs(self.lattice - index[1]))
        neighborhood_matrix = np.round(np.sqrt(lateral_dist_x ** 2 + lateral_dist_y ** 2), 2)
        return np.round(np.exp(-neighborhood_matrix ** 2 / (2 * sigma ** 2)), 2)[:, :, np.newaxis]

    def compute_accuracy(self, data: np.array, out: np.array, som_map: np.array = None) -> None:
        """
        Compute the Accuracy of the given data
        Args:
            data: np.array
            out: np.array
            som_map: np.array

        Returns: None

        """
        if som_map is not None:
            self.result_map = som_map

        self.result = np.zeros((len(data), 3))

        for i, x in enumerate(data):
            dist_grid = np.linalg.norm(x - self.MAP, axis=2)
            BMU = np.unravel_index(np.argmin(dist_grid, axis=None), dist_grid.shape)
            index = np.argmax(self.result_map[BMU])
            self.result[i, index] = 1
        y = np.array([[1], [2], [3]])
        print("Accuracy: ", np.round(np.sum(self.result @ y == out) * 100 / len(out), 2), str("%"))

    def visualize(self):
        """
        Visualize
        Returns:None

        """
        self.result_map = np.zeros([self.N, self.N, 3], dtype=np.float32)
        self.MAP = self.weights.copy()
        for i, data_point in enumerate(self.data_set):
            data = np.tile(data_point, (self.N, self.N, 1))
            dist_grid = np.linalg.norm(data - self.MAP, axis=2)
            BMU = np.unravel_index(np.argmin(dist_grid, axis=None), dist_grid.shape)
            if self.output[i] == 1:
                self.result_map[BMU] += np.asarray([0.5, 0, 0])
            elif self.output[i] == 2:
                self.result_map[BMU] += np.asarray([0, 0.5, 0])
            elif self.output[i] == 3:
                self.result_map[BMU] += np.asarray([0, 0, 0.5])

    def fit(self) -> None:

        x = True
        for epoch in range(1, self.epochs_const + 1):
            np.random.shuffle(self.data)
            for data_point in self.data:
                data = np.tile(data_point, (self.N, self.N, 1))
                self.dist = self.find_euclidean_distance(data, self.weights)
                self.BMU = self.find_BMU(self.dist)
                self.neighborhood_prob = self.compute_neighborhood_prob(self.BMU, epoch)
                self.lr = self.compute_learning_rate(epoch)
                self.update_weights(data_point)
