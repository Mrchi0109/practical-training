"""
__author__ = 'hogwarts_xixi'
"""
from time import sleep

from appium import webdriver


# 使用 pytest 单元测试框架改造一下用例, pip install pytest
# pytest的规则：
# 文件名以test_开头，
# 类名以Test开头，
# 方法名以test_开头
# 在执行测试用例之前会先执行setup方法，在执行测试用例之后，会执行teardown方法
from appium.webdriver.common.mobileby import MobileBy


class TestFood:

    def setup(self):
        # 启动app
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待 全局的等待
        # 动态的查找元素，会在10秒 之内动态的等待元素出现，
        # 如果10秒之内等到了这个元素，就继续执行后续代码，
        # 如果10秒等不到这个元素，就抛异常，TimeoutException
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 关闭app
        self.driver.quit()

    def test_food(self):
        search_key = "火锅"
        # 定位\ 交互
        # 1、打开【美团】app
        # 2、点击首页的【美食】，进入美食页面
        self.driver.find_element(MobileBy.XPATH,"//*[@content-desc='美食']").click()
        # 3、在美食页面搜索【火锅】
        self.driver.find_element(MobileBy.ID, "com.sankuai.meituan:id/txt_search_keyword").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText']").send_keys(search_key)
        sleep(5)
        # find_element 返回的是一个WebElement 类型的元素
        ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']")
        ele.click()
        # 4、验证搜索结果的前两个店铺名，包含火锅
        # find_elements 返回一个list列表, [WebElement, WebElement,.....]
        elements=self.driver.find_elements(MobileBy.ID, "com.sankuai.meituan:id/poi_info_first_poiName")
        print(elements)
        namelist = []
        for element in elements:
            # 将所有查找出来的元素的text放在列表中
            namelist.append(element.text)
        print(namelist)
        # 如果搜索出来的结果为空，则断言失败
        if len(namelist) == 0:
            print("搜索结果为空")
            assert False
        # 获取新的列表，只拿到它的前两个值
        result = namelist[:2]
        for i in result:
            assert "火锅" in i



