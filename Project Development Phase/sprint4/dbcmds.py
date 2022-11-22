from connect import execDB, execReturn
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


# INSERT into user_data(username , email , pass ) values ('Manoj' , 'manoj.selvam312@gmail.com' , 'Abcd123$')
def addUser(username , email , password):
    sql_fd = f"SELECT * FROM user_data WHERE username='{username}'"
    r = execReturn(sql_fd)

    if r != [] :
        return "Username Exists"
        
    sql_st = f"INSERT INTO user_data(username , email , pass ) values ( '{username}' , '{email}' , '{password}' )"
    r = execDB(sql_st)
    return r

def getPassword(username ):
    sql_fd = f"SELECT * FROM user_data WHERE username='{username}'"
    r = execReturn(sql_fd)

    if r == [] :
        return "User Does not exist"
        
    sql_fd = f"SELECT pass FROM user_data WHERE username='{username}'"
    r = execReturn(sql_fd)
    return r[0]['PASS']

def insertDonor(name , age , email , bloodgrp , mobno, gender , inputAddress , inputCity, inputState , inputZip ):
    sql_fd = f"INSERT INTO donor_data(uname , agev , email , bloodgrp , mobno , gender , addr , city , statev , zip ) values ( '{name}' , {age} , '{email}', '{bloodgrp}', '{mobno}', '{gender}', '{inputAddress}', '{inputCity}', '{inputState}' , '{inputZip}' )"
    r = execDB(sql_fd)
    print(r)
    return r

import os
sg = sendgrid.SendGridAPIClient(api_key=os.getenv("PL"))
from_email = Email("manoj.selvam312@gmail.com")  # Change to your verified sender

def process_request(name , age , email , bloodgrp , mobno, gender , inputAddress , inputCity, inputState , inputZip ):
    sql_fd = f"SELECT * FROM donor_data WHERE bloodgrp='{bloodgrp}' AND city='{inputCity}'"

    # sql_fd = f"SELECT * FROM donor_data"
    r = execReturn(sql_fd)
    if r == [] :
        return
    # print(r)
    for i in r:
        to_mail = To(i['EMAIL'])
        subject = "Request For plasma"
        cnt = f"""Plasma Requester Details :  
            Name : {name}
            email : {email} 
            bloodgrp : {bloodgrp} 
            mobno : {mobno} 
            Address : {inputAddress}
            City : {inputCity} 
            State : {inputState}
        """
        try:
            content = Content("text/plain", cnt)
            mail = Mail(from_email, to_mail , subject, content)
            mail_json = mail.get()
            response = sg.client.mail.send.post(request_body=mail_json)
            print(response.headers, cnt )
        except :
            print("Unable to send mail")
        



