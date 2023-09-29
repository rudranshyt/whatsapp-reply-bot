import pywhatkit
from config import phone

phoneNumber = input('enter a number')
pywhatkit.sendwhatmsg_instantly(
    phoneNo = phone,
    message="Howdy! This message will be sent instantly!",
)