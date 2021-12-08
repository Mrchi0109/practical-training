"""
__author__ = 'hogwarts_xixi'
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "meituan"
caps["appPackage"] = "com.sankuai.meituan"
caps["appActivity"] = "com.meituan.android.pt.homepage.activity.MainActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@content-desc='美食']").click()
size = driver.get_window_size()
width = int(size.get("width"))
height = size.get("height")
num = 0
name_list = []
while num < 1:
    num = num + 1
    sleep(2)
    TouchAction(driver).press(x=int(width / 2), y=(height * 0.9)).move_to(x=int(width / 2),
                                                                          y=(height * 0.1)).release().perform()
    datas = driver.find_elements_by_xpath("//*[@resource-id='com.sankuai.meituan:id/poi_name']")
    for ele in datas:
        name = ele.get_attribute("text")
        if name not in name_list:
            name_list.append(name)
            print(f"店名为：{name}")
            ele.click()
            driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                              'scrollable(true).instance(0)).'
                                                              'scrollIntoView(new UiSelector().'
                                                              'text("查看更多").instance(0));').click()
            top_food = driver.find_elements_by_xpath("//*[@resource-id='com.sankuai.meituan:id/title']")[:3]
            for food_name in top_food:
                print(f"菜名为：{food_name.get_attribute('text')}")
            # while True:
            #     data = driver.find_elements_by_xpath("//*[@resource-id='com.sankuai.meituan:id/poi_name']")
            #     if len(data) > 0:
            #         break
            #     else:
            #         driver.back()
