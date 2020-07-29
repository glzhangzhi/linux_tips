# -*- coding: utf-8 -*-
import socket
import smtplib
from email.mime.text import MIMEText


def showip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("1.1.1.1",80))
	ip=s.getsockname()[0]
	s.close()
	return ip

def send_email(content, title):

	#设置服务器所需信息
	#163邮箱服务器地址
	mail_host = 'smtp.126.com'  
	#163用户名
	mail_user = 'glzhangzhi'  
	#密码(部分邮箱为授权码) 
	mail_pass = 'qm18817329757'   
	#邮件发送方邮箱地址
	sender = 'glzhangzhi@126.com'  
	#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
	receivers = ['glzhangzhi@126.com']  

	#设置email信息
	#邮件内容设置
	message = MIMEText(content,'plain','utf-8') #注意这里，如果不把content内容改掉，很可能被126认为是垃圾邮件，不允许发送
	#邮件主题       
	message['Subject'] = title #同内容
	#发送方信息
	message['From'] = sender 
	#接受方信息     
	message['To'] = receivers[0]  

	#登录并发送邮件
	try:
		smtpObj = smtplib.SMTP() 
		#连接到服务器
		smtpObj.connect(mail_host,25)
		#登录到服务器
		smtpObj.login(mail_user,mail_pass) 
		#发送
		smtpObj.sendmail(
			sender,receivers,message.as_string()) 
		#退出
		smtpObj.quit() 
		print('success')
	except smtplib.SMTPException as e:
		print('error',e) #打印错误

send_email('标题为本次开机树莓派IP地址', showip())

#接着在crontab里输入
#@reboot 