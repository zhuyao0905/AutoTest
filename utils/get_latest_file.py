# coding=utf-8
import os

def get_latest_file(file_path, postfix=''):
    """获取指定目录下(不含子目录)按改动时间排序最新文件"""
    #列出目标目录下所有文件和文件夹并将其保存到列表
    lists = os.listdir(file_path)
    print(lists)



if __name__ == '__main__':
    get_latest_file(r'D:\\')