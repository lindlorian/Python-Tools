import os
import platform
from sys import platform


class PlatformHelper:

    @staticmethod
    def get_test_directory():

        current_directory = os.getcwd()

        if platform == "Darwin":

            root_dir = current_directory + "/"

        else:

            root_dir = current_directory + "\\"
