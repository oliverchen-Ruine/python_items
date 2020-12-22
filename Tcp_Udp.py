
#TCP服务器
#导入socket模块
import socket
import os
from threading import Thread
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',8080)
#绑定监听的地址和端口
s.bind(ip_port)
#可以连接的最大客户机的数目
s.listen(5)
 
def tcplink(con):
    print('已连接')
    while 1:
        cmd = con.recv(1024)   #接收客户端的信息
        command=cmd.decode('UTF-8')   #针对客户端发出的信息进行操作
        print("输入指令："+command)
        if command.startswith('cd'):
            os.chdir(command[2:].strip())
            result="修改目录成功"
        elif command == 'exit':
            break
        else:
            result=os.popen(command).read()
        if result:
            con.send(result.encode())
            print("结果已返回")
        else:
            con.send(b'Successfully connect')
    con.close()
 
if __name__=="__main__":
    while 1:
        #建立一个新的连接
        con,addr=s.accept()
        #创建新线程来处理TCP连接
        t=Thread(target=tcplink,args=(con,))
        t.start()
'''
#UDP 服务器
import socket
from threading import Thread
#创建一个socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定监听的地址和端口
ip_port=('127.0.0.1',8080)
s.bind(ip_port)

while 1:
    con, addr = s.recvfrom(1024)
    data = con.decode()
    #打印出发送过来的数据，再将ip地址和端口打印出来
    print(data, addr)
    if data=='exit':
        continue
    #回复，将消息发送回去
    reply=input("Server:")
    s.sendto(reply.encode(),addr)'''