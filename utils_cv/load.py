import os

def absolut_path(path):
    """Returns the absolute path corresponding to the relatif path path from the directory utils_cv.

    Parameters
    ----------
    path: string
        relative path from the directory utils_cv

    Returns
    -------
    string
        absolute path corresponding to path"""
    root = os.path.dirname(__file__)
    return os.path.join(root, path)
