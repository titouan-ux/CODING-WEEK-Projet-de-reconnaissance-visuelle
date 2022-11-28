from utils_cv.recognition import recognition
from utils_cv.recognition import ind_max
from utils_cv.recognition import drop
from utils_cv.load import absolut_path
import cv2

def test_recognition():
    recognition(cv2.imread(absolut_path('tests\\renard.png')))

def test_ind_max():
    assert ind_max([2,6,4,9,1,5,5,6,0])==(3,9)

def test_drop():
    assert drop([1,3,5,5,6,9,7,4,5],5)==[1,3,6,9,7,4]


