# ---------------------------------------------------------------------------------------------------------------------- #
# Project   :-> Self Organising Maps
# Authors   :-> Sudharsan
# E-mail    :-> s10@terpmail.umd.edu

# ---------------------------------------------------------------------------------------------------------------------- #
# Import packages
# ---------------------------------------------------------------------------------------------------------------------- #
import glob
import cv2
import pandas as pd


# -----> Frames to Video <----- #
def frames_to_video(directory: str, name: str):
    """
    A function to create a video of the
    Args:
        directory: string
            Directory of the folder that contains individual frames
        name: string
            Desired name for the output video file
    Returns: None

    """
    img_array = []
    for filename in glob.glob(directory + '/*.png'):
        img = cv2.imread(filename)
        img_array.append(img)
    out = cv2.VideoWriter(name + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, img_array[0].shape)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def load_dataset(source: str) -> pd.DataFrame:
    """
    It loads data from file using pandas read_table function

    Args:
        source: str
            relative path from root to the data file

    Returns:
        Returns the loaded pandas datafram data.

    """
    return pd.read_table(source)

    pass
