# -*-coding:GBK -*-
#1、组装邮件
#组装邮件头
#组装邮件正文
#连接smtp服务器并发送邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email_config

def send_email(report_file):
    msg=MIMEMultipart()
    msg.attach(MIMEText(email_config["body"],"plain","utf-8"))

    msg["From"]=email_config["user"]
    msg["Subject"]=email_config["Subject"]
    msg["To"]=email_config["receiver"]

    attr=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    attr["Content-Type"]="application/octet-stream"
    attr["Content-Disposition"]="attachment;filename='report.html'"
    msg.attach(attr)

    smtp=smtplib.SMTP_SSL(email_config["server"])
    smtp.login(email_config["user"],email_config["password"])
    smtp.sendmail(msg["From"],msg["To"],msg.as_string())