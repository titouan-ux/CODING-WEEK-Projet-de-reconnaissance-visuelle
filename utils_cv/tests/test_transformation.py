from utils_cv.load import absolut_path
from utils_cv.transformation import BGR_to_gray, resize_image
import cv2


def test_resize_image():
    # given
    img = cv2.imread(absolut_path(("tests\\renard.png")))
    (h, w, d) = img.shape
    new_dim = (200, 200)
    # when
    resized_image = resize_image(img, new_dim)
    # then
    assert resized_image.shape == (new_dim[0], new_dim[1], d)


def test_BGR_to_gray():
    img = cv2.imread(absolut_path(("tests\\renard.png")))
    BGR_to_gray(img)[0][0] - 1

