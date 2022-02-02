import os
from pathlib import Path
import sys

def buildPath (fileName):
    fullPath = Path(os.getcwd(), __file__)
    rootFolderPath = fullPath.parent.parent.parent
    return os.path.join(rootFolderPath, 'samples', fileName)
