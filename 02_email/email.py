import os
import csv

print(os.getcwd())  # Returns the current working directory as a string

def parse_csv_to_dict(filename):
    student_data = {}
    print(os.getcwd())
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row['Email']
            student_data[email] = {
                'First Name': row['First name'],
                'Last Name': row['Last name'],
                'Scores': {
                    'Problem 1': row['Problem 1 score'],
                    'Problem 2': row['Problem 2 score'],
                    'Problem 3': row['Problem 3 score']
                },
                'Comments': {
                    'Problem 1': row['Problem 1 comments'],
                    'Problem 2': row['Problem 2 comments'],
                    'Problem 3': row['Problem 3 comments']
                }
            }
    return student_data

import smtplib
from email.mime.text import MIMEText
from email.utils import make_msgid

def send_email(student_email, student_info):
    sender_email = "office@muc.ch"
    sender_password = ";HideIt;"

    subject = "Exam Results"
    body = f"""
    Hi {student_info['First Name']} {student_info['Last Name']},

    Here are your results:
    Problem 1: {student_info['Scores']['Problem 1']} ({student_info['Comments']['Problem 1']})
    Problem 2: {student_info['Scores']['Problem 2']} ({student_info['Comments']['Problem 2']})
    Problem 3: {student_info['Scores']['Problem 3']} ({student_info['Comments']['Problem 3']})

    Best regards,
    Your Instructor
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = student_email

    # Generate a unique Message-ID
    msg['Message-ID'] = make_msgid()

    with smtplib.SMTP('asmtp.mail.hostpoint.ch', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, student_email, msg.as_string())
        print(f"Email sent to {student_email}")



# Test the function with your `exam.csv` file
data = parse_csv_to_dict('02_email/exam.csv')
print(data)


# Example: Send an email
for email, info in data.items():
    send_email(email, info)


