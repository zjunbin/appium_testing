#  coding utf-8
# @time      :2019/5/2110:07
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :run.py.py
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
# 等待“我的柠檬”
WebDriverWait(driver,10).until(ec.visibility_of_element_located(
    (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")')))
# adb shell dumpsys activity | find "mFocusedActivity" 查看当前活动的应用包名
# driver.find_element(MobileBy.ID,"com.lemon.lemonban:id/category_description")
# driver.find_element(MobileBy.CLASS_NAME,"android.widget.TextView")
# driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,"")
# driver.find_element(MobileBy.ACCESSIBILITY_ID,"")
# 第一种定位
# driver.find_element(MobileBy.ID,"com.lemon.lemonban:id/navigation_my")
# 第二种方式
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")').click()
# 等待“用户登录”
WebDriverWait(driver,10).until(ec.visibility_of_element_located(
    (MobileBy.ID,'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')))
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")').click()

WebDriverWait(driver,20).until(ec.visibility_of_element_located(
    (MobileBy.ID,'com.lemon.lemonban:id/et_mobile')))
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/et_mobile")').send_keys('13240150942')
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/et_password")').send_keys('150942')
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/btn_login")').click()
