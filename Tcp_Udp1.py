
#TCP客户端

#导入socket库
import socket
#创建一个socket对象
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接，元组内应包括地址和端口号
s.connect(('127.0.0.1',8080))
#建立连接后，向服务器发送数据
while 1:
    cmd=input("command:")
    if cmd=='exit':
        s.send(b'exit')
        print('successfully exit!')
        break
    else:
        #将命令编码后发送给服务器
        s.send(cmd.encode('UTF-8'))
        #接收数据
        data=s.recv(65535)
        #解码打印数据
        print(data.decode(),len(data))
s.close()
'''
#UDP 客户端

import socket
#创建一个socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port=('127.0.0.1',8080)

while 1:
    #先发送，在接收
    data=input("Client:")
    s.sendto(data.encode(),ip_port)
    if data=='exit':
        break
    con, addr = s.recvfrom(1024)
    reply = con.decode()
    print(reply,addr)
s.close()'''