import smtplib
from email.mime.text import MIMEText
from flask import Flask, request
from flask_cors import CORS, cross_origin


HOST = "smtp.gmail.com"
PORT = 587
FROM = 'yashgoswamigoat@gmail.com'
PASS = "ukszmmfvnaxjjomb"

app = Flask(__name__)
cors = CORS(app)
@app.route("/sendmail",methods=['POST','GET'])
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


if __name__=="__main__":
    app.run(debug=True)