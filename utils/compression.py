# coding=utf-8
import os
import time
from zipfile import ZipFile,ZIP_DEFLATED

class Compression(object):
    """压缩文件和文件夹"""
    def __init__(self,new_file_path=None,dir_path=None):
        self.new_file_path = new_file_path
        self.dir_path = dir_path

    def compress_dir(self):
        # 压缩后文件存放路径
        new_file = self.new_file_path + "\\" + time.strftime('%Y%m%d%')+ 'test_report' + '.zip'
        z = ZipFile(new_file,'w',ZIP_DEFLATED)
        for root,dirs,files in os.walk(self.dir_path):
            # 去掉父级目录，只压缩指定文件目录的文件及内部文件
            fpath = root.replace(self.dir_path,'')
            fpath = fpath and fpath + os.sep or ''
            for file in files:
                z.write(os.path.join(root,file),fpath + file)
        z.close()

if __name__ == '__main__':
    z = Compression()
    z.compress_dir()


