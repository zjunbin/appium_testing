#  coding utf-8
# @time      :2019/5/2216:55
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test2.py
import os
import sys
import time
import unittest

from appium import webdriver
# from selenium import webdriver
from HTMLTestRunnerNew import HTMLTestRunner
from appium.webdriver.common.touch_action import TouchAction


global driver


class MyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化测试平台
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '78d358ad'
        desired_caps['appPackage'] = 'com.wochacha'
        desired_caps['appActivity'] = 'com.wochacha.StartupActivity'
        # desired_caps['appWaitActivity'] = ''
        desired_caps["unicodeKeyboard"] = "True"  # 输入中文
        desired_caps["resetKeyboard"] = "True"    # 输入中文

        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {WebView.setWebContentsDebuggingEnabled(true);}
        # cls.driver.implicitly_wait(8)
        time.sleep(8)

    def test_home_page(self):
        """首页原生页面和H5页面切换"""
        time.sleep(2)
        print(self.driver.contexts)
        contexts = self.driver.contexts
        self.driver.switch_to.context(contexts[1])  # 切换到H5页面
        time.sleep(2)
        print(self.driver.current_context)
        self.driver.switch_to.context("NATIVE_APP")  # 切换到原生页面

    def test_native_h5(self):
        """首页原生页面和H5页面切换"""
        # 注意切换H5的webview页面时，先打印下context，看是否有H5页面
        # 因为有的H5页面没有开启debug模式的话，即使有h5页面也无法切换
        # 解决方法，需要开发同学打一个测试包，加上一段调试的代码
        print(self.driver.context)
        print(self.driver.contexts)  # 打印所有上下文
        print(self.driver.current_context)
        print(self.driver.current_activity)  # 打印当前的activity
        self.driver.switch_to.context("NATIVE_APP")  # 切换到原生页面
        self.driver.switch_to.context("WEBVIEW_com.android.browser")  # 切换到H5页面

    def test_find_element(self):
        """定位元素方法"""
        self.driver.find_element_by_id("id")  # id定位
        self.driver.find_element_by_name("name")  # name定位
        self.driver.find_element_by_link_text("text")  # 链接名定位
        self.driver.find_element_by_partial_link_text("text")  # 通过元素部分可见链接文本定位
        self.driver.find_element_by_tag_name("name")  # 通过查找html的标签名称定位元素
        self.driver.find_element_by_xpath("xpath")  # 路径定位
        self.driver.find_element_by_class_name("android.widget.LinearLayout")  # 类名定位
        self.driver.find_element_by_css_selector("css")  # css选择器定位

    def test_find_elements_list(self):
        """定位元素复数集合方法"""
        self.driver.find_elements_by_id("id")  # id元素集合
        self.driver.find_elements_by_name("name")  # name元素集合
        self.driver.find_elements_by_link_text("text")  # 链接名元素集合
        self.driver.find_elements_by_partial_link_text("text")  # 部分元素可见链接集合
        self.driver.find_elements_by_tag_name("name")  # html标签名集合
        self.driver.find_elements_by_xpath("xpath")  # 路径定位集合
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")  # 类名定位集合
        elements = self.driver.find_elements_by_css_selector("css")  # css选择器定位集合
        elements[0].click()  # 选择复数集合里面第几个来进行定位

    def test_element_action(self):
        """元素操作方法"""
        element = self.driver.find_element_by_id("id")
        element.click()  # 点击
        element.clear()  # 清除元素内容
        element.text()  # 返回元素的文本内容
        element.submit(self)  # 提交表单
        element.is_enabled()  # 元素是否可用
        element.is_slected()  # 元素是否可选
        element.is_displayed()       # 元素是否可见
        element.send_keys("中英+selenium")  # 输入方法

    def test_swipe_all(self):
        """滑动方法汇总"""
        self.driver.swipe(500, 1700, 500, 100, 500)  # 向上滑动（坐标滑动可能不是很稳定）

        el1 = self.driver.find_element_by_name("商品黑榜")
        el2 = self.driver.find_element_by_name("曝光栏")
        self.driver.scroll(el1, el2)       # 从一个元素滑到另一个元素  稳定，推荐这个
        TouchAction(self.driver).press(el1).move_to(el2).release().perform()  # 从一个元素滑到另一个元素

        # 连续滑动，可以用作滑动屏幕解锁
        TouchAction().press(el1).move_to(el2).move_to(el3).move_to(el4).release().perform()  # 连续坐标滑动
        TouchAction(self.driver).press(x, y).move_to(x, y).move_to(x, y).move_to(x, y).release().perform()  # 连续元素滑动

        # 获取元素的大小（高和宽）,按照屏幕分辨率来滑动
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.75, x * 0.5, y * 0.25, 500)  # 上滑
        self.driver.swipe(x * 0.5, y * 0.25, x * 0.5, y * 0.75, 500)  # 下滑
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.25, y * 0.5, 500)  # 左滑
        self.driver.swipe(x * 0.25, y * 0.5, x * 0.75, y * 0.5, 500)  # 右滑

    def test_pinch_zoom(self):
        """捏屏幕和放大屏幕"""
        e1 = self.driver.find_element_by_id(id)
        # 捏 (Pinch)捏屏幕 (双指往内移动来缩小屏幕)
        self.driver.pinch(element=e1)
        # 放大 (Zoom)放大屏幕 (双指往外移动来放大屏幕)
        self.driver.zoom(element=e1)

    def test_screen_shot(self):
        """截屏方法"""
        self.driver.save_screenshot("D:/appium/screenshot/homepage.jpg") # 仅保存图片
        self.driver.get_screenshot_as_file("D:/appium/screenshot/homepage.jpg")  # 完整路径，IOError返回False
        self.driver.get_screenshot_as_base64()  # 截取当前屏幕图片，用于html页面直接嵌入base64编码图片
        self.driver.get_screenshot_as_png()   # 获取当前屏幕截图的二进制文件数据string

    def test_get_message(self):
        """获取当前信息"""
        self.driver.current_url   # 获取当前url
        self.driver.page_source   # 获取页面源
        self.driver.current_package    # 获取当前的包名
        self.driver.current_activity    # 获取当前的activity
        self.driver.current_context    # 列出当前上下文

    def test_pull_file(self):
        """设备推送文件"""
        # 从设备中拉出文件 (Pull File)
        self.driver.pull_file('Library/AddressBook/AddressBook.sqlitedb')
        # 推送文件到设备中去
        data = "push test"
        path = "/data/local/tmp/file.txt"
        self.driver.push_file(path, data.encode('base64'))
        # self.driver.push_file(path, data.encode('base64', 'errors'))
        # self.driver.push_file(path, base64.b64encode(bytes("push test", 'utf-8')))

    def test_js(self):
        """JS操作，执行"""
        # 在当前窗口/框架（特指 Html 的 iframe ）同步执行 javascript 代码
        driver.execute_script('document.title')
        # 异步执行代码，其他代码在执行
        driver.execute_async_script('document.title')

    def test_system(self):
        """系统杂项功能"""
        self.driver.app_strings(language=None, string_file=None)   # 获取应用字符串
        self.driver.background_app(5)  # 把当前应用置于后台5秒
        self.driver.hide_keyboard()  # 隐藏键盘
        self.driver.keyevent(176)  # 按键事件 (Key Event)给设备发送一个按键事件
        self.driver.toggle_location_services()   # 打开安卓设备上的位置定位设置
        # 打开一个应用或者activity，仅安卓端(百度糯米的包和activity名)
        self.driver.start_activity('com.nuomi', 'com.baidu.bainuo.dex.InstallDexActivity')

    def test_lock_and_open_notifaication(self):
        """锁屏和打开通知栏"""
        self.driver.open_notifications()  # 打开通知栏
        self.driver.find_element_by_id("com.android.systemui:id/clear_all_button").click()  # 点击清除通知
        self.driver.lock(5)  # 锁屏5秒

    def test_remove_install_reset(self):
        """卸载和安装app"""
        self.driver.is_app_installed("com.wochacha")  # 是否安装了app
        self.driver.remove_app("com.wochacha")  # 删除应用
        self.driver.install_app("D:/wochacha.apk")  # 安装应用
        self.driver.reset()  # 重置应用

    def test_launch_close_shake(self):
        """启动和关闭app,摇晃app"""
        # 这三个方法都报错，虽然不常用
        self.driver.launch_app()  # 启动应用
        self.driver.close_app()  # 关闭应用
        self.driver.shake()  # 摇晃设备

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 这句一定要加，不加再次启动appium会无法创建一个新的sessionid
        # cls.driver.close()  # 关闭当前窗口


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    date = time.strftime("%Y%m%d")      # 定义date为日期，time为时间  20180710  年月日
    tm = time.strftime("%Y%m%d-%H%M%S")  # 20180710-124530  年月日-时分秒
    # hms = time.strftime("%H%M%S")     # 124530  时分秒

    # 构造测试集 # 加入测试用例
    suite = unittest.TestSuite()
    suite.addTest(MyTests("test_home_page"))  # 首页
    # suite.addTest(MyTests("test_native_h5"))  # 原生页面与H5的切换
    # suite.addTest(MyTests("test_lock_and_open_notifaication"))  # 锁屏和打开通知栏
    # 执行测试用例 TextTestRunner
    unittest.TextTestRunner().run(suite)   # 执行测试用例
"""
    # 执行测试用例 HtmlTestRunner
    path = "./report/home_page/"+date+"/"
    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    # report_path = path+time+"report.html"      # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    report_path = path + time +"-home_page_1_report.html"   # 不添加时间的测试报告名
    report_title = u"百度糯米首页home_page_1测试报告"
    desc = u'Appium自动化测试报告详情：'

    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    # 关闭report，脚本结束
    report.close()
"""