import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
import socks
import socket
# socks.set_default_proxy(socks.HTTP, '地址', 25, True, '15573706812@163.com', 'zhl19980625')
socket.socket = socks.socksocket
def send_email(resultFile):
    smtpserver='smpt.163.com'
    user="15573706812@163.com"
    password="zhl19980625"
    sender="15573706812@163.com"
    receiver="1260242849@qq.com"
    subject="百度测试结果"
    sendfile=open("C:\\Users\\Administrator\\PycharmProjects\\untitled2\\lianxi\\testresult.html","r",encoding='utf-8').read()
    sendfile=open(resultFile,"r",encoding='utf-8').read()
    att=MIMEText(sendfile,"base64","utf-8")
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]="attachment;filename = "+resultFile
    msgRoot=MIMEMultipart('related')
    msgRoot['Subject']=subject
    msgRoot.attach(att)
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msgRoot.as_string())
    smtp.quit()