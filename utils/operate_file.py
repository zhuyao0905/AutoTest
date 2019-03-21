import os

class OperateFile(object):
    def __init__(self,file,dir,method = 'w+'):
        self.file = file
        self.dir = dir
        self.method = method
        self.fileHandle = None

    def check_file(self):
        # 检验给出的路径是否是一个文件
        if not os.path.isfile(self.file):
            print('文件不存在')
            return False
        else:
            print('文件已存在')
            return True

    def mk_file(self):
        # 检查文件是否存在
        if not os.path.isfile(self.file):
            # open直接打开一个文件，如果文件不存在则创建文件
            f = open(self.file,self.method)
            f.close()
            print('创建文件成功')
            return True
        else:
            print('文件已存在')
            return False

    def mk_dir(self):
        # 检查文件夹是否存在，若不存在创建一个新的文件夹
        if not os.path.isdir(self.dir):
            d = os.mkdir(self.dir)
            print('创建成功')
            return True
        else:
            print('目录已存在')
            return False

    def remove_file(self):
        # 删除文件
        if os.path.isfile(self.file):
            os.remove(self.file)
            print('删除文件成功')
        else:
            print('文件不存在')

    def write_txt(self,line):
        # 按行写入txt文档
        OperateFile(self.file).check_file()
        self.fileHandle = open(self.file,self.method)
        self.fileHandle.write(line + "\n")
        self.fileHandle.close()

    def read_txt_row(self):
        OperateFile(self.file).check_file()
        self.fileHandle = open(self.file,self.method)
        print(self.fileHandle.readline())
        self.fileHandle.close()

    def read_txt_rows(self):
        OperateFile(self.file).check_file()
        self.fileHandle = open(self.file,self.method)
        file_list = self.fileHandle.readlines()
        for i in file_list:
            print(i.strip("\n"))
        self.fileHandle.close()

if __name__=='__main__':
    of = OperateFile('D:\\应用双开测试报告\\com.excelliance.dualaid.vend.cy-11033-12-release (66).apk',
                     'D:\\应用双开测试报告\\传音测试报告')
    of.check_file()
    of.mk_dir()
