# coding=utf-8
import os
import time

class Log(object):
    # 获取Android手机的运行日志，可同时抓取多个log
    def catch_log(self,log_path):
        # 抓取Android手机log
        adb_list_old = []
        adb_list_new = []
        # 获取adb的pid
        for i in os.popen('tasklist|findstr "adb.exe"').readlines():
            adb_list_old.append(i.split()[1])
            print(adb_list_old)
        os.popen('adb logcat -v threadtime > '+log_path)
        time.sleep(1)
        for j in os.popen('tasklist|findstr "adb.exe"').readlines():
            adb_list_new.append(j.split()[1])
            print(adb_list_new)
        for log_pid in adb_list_new:
            if log_pid not in adb_list_old:
                print(log_pid)
                return log_pid

    def stop_log(self,log_pid):
        os.popen('taskkill /f /pid %s' % log_pid)

if __name__=='__main__':
    log = Log()
    log1 = log.catch_log(r'D:\\Autotest_cy\\log\\%s.txt' % time.strftime('%H%M%S'))
    time.sleep(5)
    log2 =  log.catch_log(r'D:\\Autotest_cy\\log\\%s.txt' % time.strftime('%H%M%S'))
    time.sleep(5)
    log.stop_log(log2)
    time.sleep(10)
    log.stop_log(log1)