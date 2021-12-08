"""
__author__ = 'hogwarts_xixi'
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
# 第一个录制脚本
caps = {}
caps["platformName"] = "Android"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("美食")
el1.click()
el2 = driver.find_element_by_id("com.sankuai.meituan:id/food_home_title_bar")
el2.click()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]")
el3.click()
el4 = driver.find_element_by_id("com.sankuai.meituan:id/search_edit")
el4.send_keys("hogwarts")

driver.quit()