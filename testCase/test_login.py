#coding=utf-8
from appium import webdriver

class Test(object):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '721QADRG345FC'
        desired_caps['appPackage'] = 'com.excelliance.dualaid'
        desired_caps['appActivity'] = 'com.excelliance.kxqp.ui.HelloActivity'
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.find_element_by_id('com.excelliance.dualaid:id/iv_icon').click()
        #self.driver.find_element_by_class_name('android.widget.ImageView').click()
        #self.driver.find_element_by_id('com.excelliance.dualaid:id/et_input_account').send_keys('17521047889')
       # self.driver.find_element_by_class_name('android.widget.RelativeLayout').click()

    def tearDown(self):
        # 一定要记得关闭driver, 否则下次连接的时候可能会出异常
        self.driver.quit()
    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    t = Test()
    t.setUp()
