import os
import random
def random_file(folder_path):
    files = os.listdir(folder_path)
    return folder_path + "/" + random.choice(files)
    
def file_exists(filename):
    """
    Check if a file exists.

    :param filename: The path to the file to check.
    :return: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)
