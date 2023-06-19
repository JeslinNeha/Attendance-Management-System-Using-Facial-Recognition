import os
import yagmail
import smtplib

receiver = ["jeslinneha@gmail.com", "aswinimohan2712@gmail.com",
            "harini.maran28@gmail.com"]  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep + \
    "Attendance_2022-05-28.csv"  # attach the file

# mail information
yag = yagmail.SMTP("blueskiesabove5@gmail.com", "ahj@54321")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
