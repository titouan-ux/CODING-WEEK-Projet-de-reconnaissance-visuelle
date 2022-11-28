from utils_cv.email_sender import send_alert
from utils_cv.load import absolut_path
def test_email():
    assert send_alert("coding_weeks_cs_wolf-b-gone@protonmail.com", "message",absolut_path("tests\\loup.png"))
