import smtplib
from email.mime.text import MIMEText
from flask import Flask, request
from flask_cors import CORS, cross_origin
import firebase_admin
from firebase_admin import credentials, db
import json

cred = credentials.Certificate("drnearme.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://drnearme-21c37-default-rtdb.firebaseio.com"
})

reff = db.reference("/")

HOST = "smtp.gmail.com"
PORT = 587
FROM = 'yashgoswamigoat@gmail.com'
PASS = "ukszmmfvnaxjjomb"

app = Flask(__name__)
cors = CORS(app)
@app.route("/sendmail",methods=['POST'])
@cross_origin()
def sendVerificationMail():
    json = request.get_json()
    # print(json['to'])
    # print(json['otp'])
    # print(json['name'])
    TO = json['to']
    MSG = MIMEText(open("message.html", "r").read().replace('[Your OTP]', str(json['otp'])).replace('[User]', json['name']),"html")
    MSG['From'] = FROM
    MSG['To'] = TO
    MSG['Subject'] = "Dr.NearYou App - Verify Your Email"

    smtp = smtplib.SMTP(HOST, PORT)
    smtp.connect(HOST, PORT)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    status, res = smtp.login(FROM, PASS)

    smtp.sendmail(FROM, TO, MSG.as_string())
    smtp.quit()
    return "Success"

def PassGen(name,password):
    return int(''.join(str(ord(c)) for c in name))+int(''.join(str(ord(c)) for c in password))

@app.route("/signup",methods=['POST'])
@cross_origin()
def Signin():
    data = request.get_json()
    email = str(data['email']).replace(".","")
    name = data['username']
    password = data['password']
    reff.child('Accounts').child(email).set({
        'username' : name,
        'password' : str(PassGen(name,password))
    })
    return "Success"
@app.route("/auth",methods=['POST'])
@cross_origin()
def Auth():
    data = request.get_json()
    email = str(data['email']).replace(".","")
    password = data['password']
    AccountDetails = reff.child('Accounts').child(email).get()
    passNo = str(PassGen(AccountDetails['username'],password))
    print((passNo,AccountDetails['password']))
    if passNo==str(AccountDetails['password']):
        return json.dumps({
            'name' : AccountDetails['username'],
            'email' : data['email']
        })
    else:
        return str({
            'status' : False
        })
    return "Success"

if __name__=="__main__":
    app.run(debug=True)