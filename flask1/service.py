
from wxpusher import WxPusher # https://github.com/wxpusher/wxpusher-sdk-python
app_token = 'AT_VqsyjlZxsloRxLnaOxbQdP3vCei22Ib6'   # 本处改成自己的应用 APP_TOKEN
uid_myself = 'UID_bIgme9sTMeA4Bv44XAL19VH5Ag6b'  # 本处改成自己的 UID
#  === TCP 服务端程序 server.py ===
import requests
# 导入socket 库（*表示导入所有可用函数和名字）
from socket import *

IP = ''
# 端口号
PORT = 50000
# 定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 512
# socket是库中的一个类，有两个初始化参数(分别指明这个socket所用的传输层和网络层协议)
# 类后加括号实例化一个socket对象，赋给监听socket(因为这是一个服务端程序，要等待客户端的连接)
# 参数 AF_INET （internet）表示该socket网络层使用IP协议
# 参数 SOCK_STREAM （一种流）表示该socket传输层使用tcp协议
listenSocket = socket(AF_INET, SOCK_STREAM)

# 调用socket类的bind()函数,绑定ip地址和端口,即与服务器连接的ip地址和端口号
# 参数是（IP地址，端口号）二元组
listenSocket.bind((IP, PORT))
def wxpusher_send_by_webapi(msg):
    """利用 wxpusher 的 web api 发送 json 数据包，实现微信信息的发送"""
    webapi = 'http://wxpusher.zjiecode.com/api/send/message'
    data = {
        "appToken":app_token,
        "content":msg,
        "summary":msg[:99], # 该参数可选，默认为 msg 的前10个字符
        "contentType":1,
        "topicIds":[7158],
        "uids":[ uid_myself, ],
        }
    result = requests.post(url=webapi,json=data)
    return result.text

# 调用socket类的listen()函数，使socket处于监听状态，等待客户端的连接请求
# 参数 8 表示 最多接受多少个等待连接的客户端（类似在排队的人数）
listenSocket.listen(8)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')

dataSocket, addr = listenSocket.accept()
print('接受一个客户端连接:', addr)

# while循环的作用：不断接收客户端发来的消息
while True:
    # 调用数据socket的recv()方法，recieve(接收)，
    # 参数BUFLEN 指定从接收缓冲里最多读取多少字节
    # 这里的recvd接受的是字节串（bytes类型），与字符串（string类型）不同，网络传输用的都是字节串
    recved = dataSocket.recv(BUFLEN)

    # 如果返回空bytes（空字节），表示对方关闭了连接
    # 退出循环，结束消息收发
    if not recved:
        break

    info = recved.decode()
    print(f'收到对方信息： {info}')
    result1 = wxpusher_send_by_webapi(info)
    print(result1)
    dataSocket.send(f'服务端接收到了信息 {info}'.encode())


# =================================part 2 =====================================

# 服务端也调用close()关闭socket
dataSocket.close()
listenSocket.close()









