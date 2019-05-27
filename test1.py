#  coding utf-8
# @time      :2019/5/2216:40
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test1.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# aapt dump badging I:\PycharmProjects\Test_apk\Future.apk 查看app应用相关信息

Caps = {"platformName":"Android",
        "platformVersion":"5.1",
        "deviceName":"Addroid Emulator",
        "appPackage":"com.lemon.lemonban",
        "appActivity":"com.lemon.lemonban.activity.WelcomeActivity",
        "noRest":True
}

# 连接appium server  ，并连接哪一个driver
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=Caps)
driver.pull_file()
driver.push_file()
