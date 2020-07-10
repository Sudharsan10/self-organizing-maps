# -------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Self Organising Maps
# Authors   :-> Sudharsan
# E-mail    :->  s10@terpmail.umd.edu

# -------------------------------------------------------------------------------------------------------------------- #
# Import packages
# -------------------------------------------------------------------------------------------------------------------- #
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from src.handler.utility import*
from src.som.som_2d import *


def implementation() -> None:
    wine_input_data = load_dataset('./data/raw/wine_data/Wine Input.asc')
    wine_desired_output_data = load_dataset('./data/raw/wine_data/Wine Desired.asc')

    feature_scaler = MinMaxScaler(feature_range=(0, 1))
    wine_input_data = feature_scaler.fit_transform(wine_input_data)
    wine_input_data = pd.DataFrame(data=wine_input_data)
    wine_input_data.columns = ['Alcohol', 'Malic acid', 'Ash','Alcalinity of Ash', 'Magnesium', 'Total phenols', 'Flavanoids',
                               'Non-flavanoids phenols', 'Proanthocyanins', 'color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']


    wine_desired_output_data = feature_scaler.fit_transform(wine_desired_output_data)
    wine_desired_output_data = pd.DataFrame(data=wine_desired_output_data)

    X = wine_input_data.to_numpy()
    Y = wine_desired_output_data.to_numpy()
    mod = np.array([[1, 2, 3]])
    out = Y @mod.T

    split_ratio = 0.8
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    n = int(split_ratio*len(X))

    train_x, train_y = X[idx[0:n]], Y[idx[0:n]]
    test_x, test_y = X[idx[n:]], Y[idx[n:]]
    train_out, test_out = out[idx[0:n]], out[idx[n:]]

    # -----> Step 01: Create the SOM_2D object <----- #
    problem = SOM_2D()

    # -----> Step 02: Initialise the object with data and parameters <----- #
    problem.initializer(train_x.copy(), train_out.copy())

    # -----> Step 03: Fitting the SOM_2D for the Wine data <----- #
    problem.fit()
    problem.visualize()

    print("Red = Class 1")
    print("Blue = Class 2")
    print("Green = Class 3")
    plt.figure(figsize=(10,10))
    plt.imshow(problem.result_map, interpolation='nearest')
    plt.show()

    problem.compute_accuracy(test_x, test_out)


if __name__ == '__main__':
    implementation()

