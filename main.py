import os

# 设置发件人的邮件地址和邮箱密码
username = "zhuyao@excean.com"
passwoed = input('请输入邮箱密码：')

# 监控adb进程，初始化所有adb.exe进程（kill掉)
logcat = Logcat()
logcat.kill_adb(arg=0)

# 监控目标安装