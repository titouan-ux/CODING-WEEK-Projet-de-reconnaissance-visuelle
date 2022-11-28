from utils_cv.performance import performance
from utils_cv.performance_object_detector import performance_object_detector

def test_performance():
    x,y=performance()
    assert (x>=0 and x<=1 and y>=0 and y<=1) 

def test_performance_object_detector():
    x,y=performance_object_detector()
    assert (x>=0 and x<=1 and y>=0 and y<=1)
