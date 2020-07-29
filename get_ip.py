import socket

#输出树莓派IP地址

def showip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("1.1.1.1",80))
	ip=s.getsockname()[0]
	s.close()
	return ip