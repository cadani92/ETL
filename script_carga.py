import os
import pandas as pd
from configuracion.utilities import ETLUtilies

class ETL:

    def __init__(self, root: str, levels_up: int):
        util = ETLUtilies()
        self.root = util.get_directory(levels_up)
        print(self.root)


root_dir = os.getcwd()
directory_file = ETL(root_dir, 3)

