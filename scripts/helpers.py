import os

def buildPath (fileName):
    currentPath = os.getcwd()
    return os.path.join(currentPath, 'samples', fileName)
