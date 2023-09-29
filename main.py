import pywhatkit
from config import phone

pywhatkit.sendwhatmsg_instantly(
    phoneNo = phone,
    message="Howdy! This message will be sent instantly!",
)