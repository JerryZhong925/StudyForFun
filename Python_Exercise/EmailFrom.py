#!/usr/bin/env python
#coding:utf-8
from email.mime.text import MIMEText
import smtplib
msg = MIMEText('hello, send by Python...hello, send by Python...hello, send by Python...hello, send by Python...hello, send by Python...', 'plain', 'utf-8')
from_addr='jerry_zhong925@sina.com'
password='890925'
smtp_server='smtp.sina.com'
to_addr='812972650@qq.com'
server = smtplib.SMTP(smtp_server, 25) 
server.set_debuglevel(1)
#server.esmtp_features["auth"]="LOGIN PLAIN"
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
