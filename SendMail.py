from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
import config

app = Flask(__name__)

def SendMail(sender_name, receiver_email, subject, message):
    server = smtplib.SMTP(config.SERVER, config.PORT)
    server.starttls()
    server.login(config.SENDER, config.PASSWORD)
    msg = MIMEText(message)
    msg["From"] = f"{sender_name} <{config.SENDER}>"
    msg["To"] = receiver_email
    msg["Subject"] = subject
    server.sendmail(config.SENDER, [receiver_email], msg.as_string())
    server.quit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["GET"])
def api():
    sender_name = request.args.get("name")
    receiver_email = request.args.get("receiver")
    subject = request.args.get("sub")
    message = request.args.get("message")
    SendMail(sender_name, receiver_email, subject, message)
    return "Sent"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
