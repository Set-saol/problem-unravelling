from socket import socket,AF_INET,SOCK_STREAM #导入模块
import datetime

# 端口扫描 通过对目标主机的 IP地址和端口 建立连接判断端口是否打开
def scan_port(ip,port):
    try: # 如果使用sock.connect 尝试建立连接 连接失败会使程序报异常 所以要使用到 异常处理 try
        time = datetime.datetime.now()  # 日志时间获取
        # (1)创建socket对象
        sock = socket(AF_INET, SOCK_STREAM)

        # (2)对目标主机进行尝试建立连接
        return_value = sock.connect_ex((ip, port))
        # connect_ex 对目标主机连接成功则 返回0 失败则返回 error错误
        # (3)判断并输出结果
        if return_value == 0:
            #通过文件操作,把结果导入文件中
            with open('./端口扫描结果.txt', 'a') as file:
                file.write(f'port {port} is open -- time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        else:
            with open('./端口扫描结果.txt', 'a') as file:
                file.write(f'port {port} not is open -- time:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    except Exception :
        print('如果使用了connect尝试连接,连接失败报异常被try处理了,所以else不会返回连接失败的数据')



if __name__ == '__main__':
    ip_location = input('请输入你要扫描的目标主机IP地址(如：127.0.0.1)：')
    port_number = eval(input('请输入要扫描的目标主机端口(端口号0~65535):'))
    scan_port(ip_location,port_number)