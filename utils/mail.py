from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

import smtplib

class Email(object):
    def __init__(self, file_path=None, html_path=None, image_path=None):
        """初始化Email"""
        self.file_path = file_path
        self.image_path = image_path
        self.html_path = html_path

    def get_latest_file(self, get_path=None):
        """获取指定目录下按改动时间排序最新文件"""
        # 列出目录下所有文件和文件夹保存到lists
        lists = os.listdir(get_path)
        # 按时间排序
        lists.sort(key=lambda x: os.path.getmtime(get_path + "\\" + x))
        # 获取最新的文件保存到latest
        latest = os.path.join(get_path, lists[-1])
        return latest

    def create_email(self):
        """创建并发送邮件，测试报告通过邮件附件的形式发出"""
        sender = 'zhuyao@excean.com'
        password = 'zhuyao520'
        # 输入SMTP服务器地址
        smtpserver = 'smtp.ym.163.com'
        receiver = ''
        # 确认收件人地址
        receiver = 'zhuyao@excean.com'
        # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
        subject = '测试报告'
        subject = Header(subject, 'utf-8').encode()

        # 构造邮件对象MIMEMultipart对象
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver

        # 邮件正文内容,构造MIMEText对象，第一个参数是邮件正文，第二个参数就是MIME的subtype,传入'plain'表示纯文本
        text = MIMEText('<html><body>'
                        + '<h2>测试结论如下</h2>'
                        + '<p>如图<img src="cid:Imgid">'
                        + '</body></html>', 'html', 'utf-8')
        msg.attach(text)

        # 插入图片
        image_path ="C:\\Users\\zm01\\Desktop\\photo.png"
        if self.image_path is not None:
            with open('C:\\Users\\zm01\\Desktop\\photo.png', 'rb') as f:
                # MIMEImage，只要打开相应图片，再用read方法读入数据，指明src中的代号是多少。比如Imgid
                mime = MIMEImage(f.read())
                # 加上必要的头信息:
                mime.add_header('Content-ID', 'Imgid')
                msg.attach(mime)

        # 插入附件，使用压缩后的文件做为附件，包含测试apk，测试结论
        #file_path = "C:\\Users\\zm01\\Desktop\\log.txt"
        with open(self.get_latest_file(self.file_path), 'rb') as f:
            file = f.read()
            text_file = MIMEText(file, 'base64', 'utf-8')
            text_file.add_header('Content-Disposition', 'attachment', filename='test_report.zip')
            msg.attach(text_file)

        # 发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver, 25)
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            print('邮件发送成功')
            smtp.quit()
        except smtplib.SMTPException as e:
            print('邮件发送失败，Case:%s' % e)

if __name__ == '__main__':
    email = Email(file_path=r'D:\\',
                         image_path="C:\\Users\\zm01\\Desktop\\photo.png")
    email.create_email()