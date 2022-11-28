from utils_cv.detector.detection_helping import sliding_window
from utils_cv.detector.detection_helping import image_pyramid

def test_sliding_windows():
    assert str(type(sliding_window('tests\\renard.png',16,(200, 150))))=="<class 'generator'>"

def test_image_pyramid():
    assert str(type(image_pyramid('tests\\renard.png')))=="<class 'generator'>"