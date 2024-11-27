import smtplib
import random

def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s' % from_addr
    header += '\r\nTo: %s' % ','.join(to_addr_list)
    header += '\r\nSubject: %s\r\n' % subject
    message = header + message
    
    print(header)
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

#### FILL THIS INFO ##########
login = ''
password = ''
#########################

fromaddr = 'bell.anapop@gmail.com'
subject = 'Exam Scores'

scores = {}    
file = open("exam.csv")
for f in file:
    email, rest = f.strip().split(',',1)
    scores[email] = rest.split(',')

random_student = random.choice(list(scores.keys()))

for to,s in scores.items():
    message = "Dear " + s[1] + ',\nYour score for the book assignment is broken down below, by question number.'
    message += "\n\n1) " + s[2] + "%: " + s[3]
    message += "\n2) " + s[4] + "%: " + s[5]
    message += "\n3) " + s[6] + "%: " + s[7]
    if random_student == to:
        message += "\n\nYou've been randomly chosen to present a summary of the book in the next class. Looking forward to it!"
    print(subject)
    sendemail(fromaddr, [to], subject, message, login, password)

# Copyright Manning Publications