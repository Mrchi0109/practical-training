"""
__author__ = 'hogwarts_xixi'
"""
# appium-client
# pip install appium-python-client
from appium import webdriver

# 定义了一个字典，初始化的配置信息
caps = {}
caps["platformName"] = "Android"
# adb logcat ActivityManager:I | grep "cmp"
caps["appPackage"] = "com.sankuai.meituan"
caps["appActivity"] = "com.meituan.android.pt.homepage.activity.MainActivity"
# 防止清缓存
caps["noReset"] = "true"
# 设备的名字
caps["deviceName"] = "emulator-5554"
# 最重要的一句，与appium server 建立连接，需要将caps 传入到参数里面
# 会返回一个driver对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("美食")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.GridLayout/android.widget.FrameLayout[1]/android.widget.TextView")
el2.click()

driver.quit()