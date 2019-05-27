#  coding utf-8
# @time      :2019/5/2211:29
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :run2.py.py
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction

Caps = {"platformName":"Android",
        "platformVersion":"5.1",
        "deviceName":"Addroid Emulator",
        "appPackage":"com.xxzb.fenwoo",
        "appActivity":"com.xxzb.fenwoo.activity.addition.WelcomeActivity",
        # "noRest":True
}

# 连接appium server  ，并连接哪一个driver
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=Caps)
time.sleep(10)
win_size = driver.get_window_size()
# 从右向左 滑屏
y = win_size['height']*0.5
x_s = win_size['width']*0.9
x_e = win_size['width']*0.1
# 开始滑动
for index in range(3):
    driver.swipe(x_s,y,x_e,y,200)
    time.sleep(2)
WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_start")))
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()


WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_login")))
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_login").click()
WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/et_phone")))
driver.find_element_by_id("com.xxzb.fenwoo:id/et_phone").send_keys('18684720553')
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_next_step").click()
driver.find_element_by_id("com.xxzb.fenwoo:id/et_pwd").send_keys('python')
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_next_step").click()
WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_confirm")))
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_confirm").click()
WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_gesturepwd_guide")))
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_gesturepwd_guide").click()
WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/right_btn")))
driver.find_element_by_id("com.xxzb.fenwoo:id/right_btn").click()
WebDriverWait(driver,10).until(ec.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/gesturepwd_create_lockview")))

ele = driver.find_element_by_id("com.xxzb.fenwoo:id/gesturepwd_create_lockview")
size = ele.size
loc = ele.location
setp = size['width']/6
# 九宫格的每个点坐标
loc1 = (loc['x']+setp,loc['y']+setp)
loc2 = (loc1[0]+ 2*setp,loc1[1])
loc3 = (loc1[0]+ 4*setp,loc1[1])
loc4 = (loc1[0],loc1[1]+setp*2)
loc5 = (loc1[0]+ setp*2,loc1[1]+setp*2)
loc6 = (loc1[0]+ setp*4,loc1[1]+setp*2)
loc7 = (loc1[0],loc1[1]+setp*4)
loc8 = (loc1[0]+ setp*2,loc1[1]+setp*4)
loc9 = (loc1[0]+ setp*4,loc1[1]+setp*4)
tc = TouchAction(driver)
for i in range(2):
    tc.press(x = loc1[0],y = loc1[1]).wait(2000).\
        move_to(x=loc3[0],y=loc3[1]).wait(2000).\
        move_to(x=loc5[0],y=loc5[1]).wait(2000).\
        move_to(x=loc7[0],y=loc7[1]).wait(2000). \
        move_to(x=loc9[0], y=loc9[1]).wait(2000). \
        release().perform()
    driver.find_element_by_id("com.xxzb.fenwoo:id/right_btn").click()

time.sleep(2)
driver.quit()