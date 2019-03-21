import yaml
import os
from appium import webdriver
global data

class AppiumInit(object):
    """appium server"""
    def appium_init(self):
        """读取配置文件的数据"""
        global driver
        file = open('D:\AutoTest\config\config.yaml', 'r',encoding='utf-8')
        data = yaml.load(file)
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['packageName'] = data['packageName']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['autoLaunch'] = 'false'
        # 不要在会话前重置应用状态。默认值false
        desired_caps['noReset'] = 'true'
        desired_caps['automationName'] = data['automationName']
        desired_caps['app'] = data['app']
        # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['unicodekeyboard'] = data['unicodekeyboard']
        # 隐藏键盘
        desired_caps['resetkeyboard'] = data['resetkeyboard']
        # 初始化
        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
        return driver

    def quit(self):
        # 一定要记得关闭driver, 否则下次连接的时候可能会出异常
        driver.quit()

class AppOpeation(object):

    def uninstall_app(self):
        os.popen('adb shell uninstall '+ data['packageName'])

    def clear_app(self):
        os.popen('adb shell pm clear '+ data['packageName'])

    def force_stop(self):
        os.popen("adb shell am force-stop " + data['packageName'])

    def start_app(self,choice=0):
        # 启动APP（choice=0正常启动，choice=1启动并返回启动耗时
        if choice ==0:
            os.popen('adb shell am start ' + data['packageName'] +'/'+ data['appActivity'])
        elif choice == 1:
            t = os.popen('adb shell am start -W ' + data['packageName'] +'/'+ data['appActivity'])
            for line in t.readlines():
                if 'TotalTime' in line:
                    start_time = line.split()[1]
                    return start_time
        else:
            print('argument error,you can only choose 0 or path')