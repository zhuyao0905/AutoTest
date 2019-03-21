#!urs/bin/python
import os
import time
import urllib
from comm.common import AppiumInit
from comm.common import AppOpeation

class AppiumServerCheck(object):
    """appium server"""
    appium = AppiumInit()
    app_operation = AppOpeation()

    def check_appium_server(self):
        # 检查appium服务是否开启，如未开启则自动开启服务进行初始化
        if 'node.exe' in os.popen('tasklist | findstr "node.exe"').read():
            while True:
                try:
                    self.appium.appium_init()
                    break
                except ConnectionRefusedError:
                    time.sleep(3)
                except urllib.error.URLError:
                    time.sleep(3)
            self.app_operation.force_stop()
            print('测试环境正常，开始执行测试\n')
        else:
            os.popen('start appium')
            print('正在启动appium服务程序，请稍等...\n')
            while True:
                if 'node.exe' in os.popen('tasklist | findstr "node.exe"').read():
                    while True:
                        try:
                            self.appium.appium_init()
                            break
                        except ConnectionRefusedError:
                            time.sleep(3)
                        except urllib.error.URLError:
                            time.sleep(3)
                    self.app_operation.force_stop()
                    print('测试环境正常，开始执行测试\n')
                    break
                else:
                    time.sleep(3)
    def stop_appium_server(self):
        # 结束appium进程（Windows适用）
        pid_node = os.popen('tasklist | findstr "node.exe"').readlines()
        for i in pid_node:
            os.popen('taskkill /f /pid ' + i.split()[1])
        pid_cmd = os.popen('tasklist |findstr "cmd.exe').readlines()
        for i in pid_cmd:
            os.popen('taskkill /f /pid ' + i.split()[1])

if __name__=='__main__':
    appium_check = AppiumServerCheck()
    appium_check.check_appium_server()
    appium_check.stop_appium_server()


if __name__=='__main__':
    App = AppiumInit()
    App.appium_init()
