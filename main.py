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
    # print(request.get_json())
    TO = 'yashgoswamiyg100@gmail.com'
    MSG = MIMEText(open("message.html", "r").read().replace('[Your OTP]', '6912').replace('[User]', 'Yash Goswami'),
                   "html")
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