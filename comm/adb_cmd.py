# coding=utf-8
import os

class  Adb(object):
    '''调用adb命令获取设备或App相关信息'''
    __adb_command = [
        'adb devices',
        'adb shell',
    ]
    def __init__(self,pck_name):
        '''初始化Adb类，传入apk的包名参数'''
        self.pck_name =pck_name

    def command_list(self):
        print(self.__adb_command)

    def get_device_id(self):
        texts = os.popen('adb devices').readlines()
        print(texts)
        text = []
        for i in texts:
            if len(i) >1:
                text.append(i)
        if len(text) == 1 :
            print('未检测到已连接设备')
        elif len(text) == 2:
            device =text[1].split()[0]
            print(device)
            return device
        else:
            print('已连接到多台设备')
            device_list = []
            for i in list(range(1,len(text))):
                device_list.append(text[i].split()[0])
            # print(device_list)
            return device_list

    def check_usb_connect(self):
        "查看USB连接状态"
        text = os.popen('adb devices').readlines()
        if 'device' in text[1]:
            print('usb已连接')
            return True
        else:
            print('usb未连接')
            return False

    # def get_device_ip(self):
    #     # 获取Android手机IP地址,8.0查询不到
    #     data = os.popen('adb shell netcgf').readlines()
    #     for i in data:
    #         if 'wlan0' in i:
    #             ip = i.split()[2].split('/')[0]
    #             print(ip)
    #             return ip

    def get_app_uid(self):
        "根据APP包名获取其uid"
        content = os.popen('adb shell pm dump ' + self.pck_name + ' |findstr "u0a" ').read()
        uid = content.split()[-1].replace(':','')
        # print('%s的uid为：%s' % (self.pck_name,uid))
        return uid

    def get_activity(self):
        # 根据APP包名获取启动入口类
        activity = ((x.split()[5]) for x in os.popen('adb shell '
                'monkey -v -v -v 0').readlines() if self.pck_name in x )
        launch_activity = self.pck_name + '/' + activity.__next__()
        # print(launch_activity)
        return launch_activity

    def app_start(self):
        # 启动APP
        os.popen('adb shell am start ' + self.get_activity())

    def back(self):
        # back按键
        os.popen('adb shell input keyevent 4')

    def home(self):
        # home按键
        os.popen('adb shell input keyevent 1')

    def force_stop(self):
        # 强行停止APP
        os.popen('adb shell am force-stop ' + self.pck_name)

    def clear_data(self):
        # 清除数据
        os.popen('adb shell pm clear ' + self.pck_name)

    def uninstall(self):
        # 卸载APP
        os.popen('adb shell uninstall ' + self.pck_name)

    def get_version(self):
        # 获取版本号
        version = os.popen(
            'adb shell pm dump ' + self.pck_name + ' |findstr "versionName"').read().replace()
        # print('版本号：%s' % version)
        return version

if __name__=='__main__':
    adb = Adb('com.excelliance.dualaid.vend.cy')
    adb.get_app_uid()
    adb.get_device_id()