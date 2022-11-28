from utils_cv.detector.utilitary import resize
from utils_cv.load import absolut_path
from utils_cv.detector.utilitary import max_ls
import cv2

def test_resize():
    img=cv2.imread(absolut_path('tests\\renard.png'))
    assert str(type(resize(img)))=="<class 'numpy.ndarray'>"

def test_max_ls():
    assert max_ls([2, 6, 4, 9, 1, 5, 5, 6, 0]) == (9, 3)
