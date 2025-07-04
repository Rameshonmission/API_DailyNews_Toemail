import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import smtplib

api_key="f7cf2ea3fc9042788a1515ddf4b20bad"
topic="techcrunch"
url=("https://newsapi.org/v2/top-headlines?"
     f"sources={topic}"
     "&apiKey=f7cf2ea3fc9042788a1515ddf4b20bad"
     "&Language=en")
request = requests.get(url,verify=False)
content= request.json()

password ="wnhq xjon atvx ronl"
user_name="thriveonmission@gmail.com"

receiver ="thriveonmission@gmail.com"
hostname ="smtp.gmail.com"
port =465

context =ssl.create_default_context()

message=""
for item in content["articles"]:
    message=message+item["title"]+"\n" +item["description"]+ "\n"+ item["url"]+(2*"\n")
print(message)
# structure the e-mail
msg =MIMEMultipart()
msg['From']=user_name
msg['To'] =receiver
msg['Subject'] ="Important Daily News"

#encode the e-mail

msg.attach(MIMEText(message,'plain','utf-8'))


with smtplib.SMTP_SSL(hostname, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, msg.as_string())










