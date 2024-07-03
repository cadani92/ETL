import os
import pandas as pd

class ETLUtilies:

    def __init__(self):
        self.directory = os.getcwd()
        self.directory = self.directory.replace("\\", "/")

    def get_directory(self, levels_up: int):
        directory = self.directory
        for i in range(levels_up):
            directory = os.path.dirname(directory)
        directory = directory.replace("\\", "/")
        return directory



    