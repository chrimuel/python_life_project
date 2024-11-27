import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.utils import make_msgid
import random

# Function to parse the CSV into a dictionary
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

# Function to send an email
def send_email(student_email, subject, body, sender_email="office@muc.ch", sender_password=";HideIt;"):
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

# Import your `exam.csv` file
data = parse_csv_to_dict('02_email/exam.csv')
print(data)

# Choose a random student for a special message
chosen_email = random.choice(list(data.keys()))
print(f"Chosen student: {chosen_email}")

# Send exam results to all students
for email, info in data.items():
    subject = "Exam Results"
    body = f"""
    Hi {info['First Name']} {info['Last Name']},

    Here are your results:
    Problem 1: {info['Scores']['Problem 1']} ({info['Comments']['Problem 1']})
    Problem 2: {info['Scores']['Problem 2']} ({info['Comments']['Problem 2']})
    Problem 3: {info['Scores']['Problem 3']} ({info['Comments']['Problem 3']})
    """
    if chosen_email==email:
        body +="""
    Congratulations! You have been selected to present a summary of the book in the next class. 
    Please prepare a brief presentation and feel free to reach out if you have any questions.
    """
    body +="""
    Best regards,
    Your Instructor
    """
    send_email(email, subject, body)

