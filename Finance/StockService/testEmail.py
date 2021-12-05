#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 0:28
# @Author : HuYouLiang
# @File : testEmail.py
# @Purpose :
import smtplib
from email.mime.text import  MIMEText

MailServer = "smtp.163.com"
UserSend = "hankhuhu@163.com"
Passwd = "LVFKOFSPBGVYVBZJ"

mail = MIMEText("发送的邮件内容：Test")
mail["Subject"] = "这是邮件主题"
mail["From"] = UserSend
mail["To"] = "982857141@qq.com"

smtp = smtplib.SMTP(MailServer, port=25)
smtp.login(UserSend, Passwd)
smtp.sendmail(UserSend, mail["To"], mail.as_string())
smtp.quit()
