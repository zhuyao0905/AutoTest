import os
import time


def get_time():
    """获取当前时间"""
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return now

def get_desktop_path():
    """获取系统桌面路径"""
    global path
    path = os.path.join(os.path.expanduser("~"), 'Desktop')
    return path

def get_ip():
    a = os.popen('ipconfig').readlines()
    for i in a:
        if 'IPv4' in i:
            print(i.split()[-1])
            return i.split()[-1]

if __name__ == '__main__':
    get_time()
    get_desktop_path()
    get_ip()