# coding = UTF-8
import os
import time

class FilePath(object):

    def __init__(self,apk_path,style = '.apk'):
        self.apk_path = apk_path
        self.style = style

    def get_file_path(self):
        '''获取安装包路径'''
        for file in os.listdir(self.apk_path):
            file_path = os.path.join(self.apk_path,file)
            if self.style in file_path and os.path.isfile(file_path):
                print(file_path)
                return file_path


if __name__ == '__main__':
    fp = FilePath(apk_path=r'D:\应用双开测试报告', style='.apk')
    fp.get_file_path()
