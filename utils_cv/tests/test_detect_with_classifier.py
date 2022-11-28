from utils_cv.detector.detect_with_classifier import object_detector
from utils_cv.load import absolut_path

def test_object_detector():
    list_of_object=object_detector(absolut_path('tests\\renard.png'))
    assert str(type(list_of_object))=="<class 'list'>"
    for img in list_of_object:
        assert str(type(img))=="<class 'numpy.ndarray'>"
