import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import traceback

MY_ADDRESS = 'coding_weeks_cs_wolf-b-gone@mail.com'
PASSWORD = 'Coding_weeks_CS_GR4'


def send_alert(email, recognition_result, image_path):
    """Sends an email to the email adress: 'email', the subject includes 'alert_kind', the image image_path is added in the email.

    Parameters
    ----------
    email: string
        address to send the email to

    body: string
        explain the type of alert to the user : the certainty level of detection of a predator is either high or medium.

    image_path: string
        path to the image in which the predator is detected:

    Returns
    -------
    bool
        True if the email is sent successfully"""

    server = smtplib.SMTP(host='smtp.mail.com', port=587)
    server.starttls()
    server.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "This is a chicken-almost-eaten alert"
    body = "Alert, a " + recognition_result + " was detected near your property"
    msg.attach(MIMEText(body, 'plain'))
    img_data = open(image_path, 'rb').read()
    img = MIMEImage(img_data)
    msg.attach(img)
    try:
        server.send_message(msg)
    except Exception:
        traceback.print_exc()
        return False
    return True
