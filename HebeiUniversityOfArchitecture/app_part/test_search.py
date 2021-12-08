"""
__author__ = 'hogwarts_xixi'
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
测试用例
1、打开【美团】app
2、点击首页的【美食】，进入美食页面
3、在美食页面搜索【火锅】
4、验证搜索结果的前五个店铺名，包含火锅
"""


class TestFood:
    def setup(self):
        desire_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            # 重要的：通过命令获取package/activity :
            # adb logcat ActivityManager:I | grep "cmp"
            "appPackage": "com.sankuai.meituan",
            "appActivity": "com.meituan.android.pt.homepage.activity.MainActivity",
            # # 跳过设备初始化 ,跳过settings.apk的安装与设置
            # "skipDeviceInitialization": True,
            # # 跳过uiautomato2 服务安装
            # "skipServerInstallation": True,
            # 防止 清缓存数据
            "noReset": "True",
        }
        # 客户端与服务端建立连接的关键语句，启动app
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 隐式等待，每一次查找元素的时候，动态的查找
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search_food(self):
        search_key = "火锅"
        # 2、点击首页的【美食】，进入美食页面
        self.driver.find_element(MobileBy.XPATH,'//android.view.View[@content-desc="美食"]').click()
        # 3、在美食页面搜索【火锅】
        self.driver.find_element(MobileBy.ID, "com.sankuai.meituan:id/txt_search_keyword").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.EditText']").send_keys(search_key)
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='搜索']").click()
        def wait(x:WebDriver):
            try:
                self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").click()
            except:
                print("未找到搜索按钮")
            return "智能排序" in self.driver.page_source

        WebDriverWait(self.driver,10).until(wait)
        # 4、验证搜索结果的前五个店铺名，包含火锅
        size = self.driver.get_window_size()
        width = int(size.get("width"))
        height = size.get("height")
        name_list = []

        while True:
            # 获取页面元素
            results = self.driver.find_elements(MobileBy.ID, "com.sankuai.meituan:id/poi_info_first_poiName")
            for ele in results:
                name = ele.get_attribute("text")
                if name not in name_list:
                    name_list.append(name)
                    print(f"店名为：{name}")

            if len(name_list)>=3:
                break
            else:
                TouchAction(self.driver).press(x=int(width / 2), y=(height * 0.9)).move_to(x=int(width / 2),
                                                                                  y=(height * 0.2)).release().perform()

        final_result = name_list[:3]
        # for name in final_result:
        #     if search_key not in name:
        #         assert False
        # 验证每一个name 里都包含seach_key,如果有一个不包含则为False
        assert all([search_key in name for name in final_result])


    def test_search_food1(self):
        search_key = "火锅"
        # 2、点击首页的【美食】，进入美食页面
        self.driver.find_element(MobileBy.XPATH,'//android.view.View[@content-desc="美食"]').click()
        # 3、在美食页面搜索【火锅】
        self.driver.find_element(MobileBy.ID, "com.sankuai.meituan:id/txt_search_keyword").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.EditText']").send_keys(search_key)
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='搜索']").click()
        def wait(x:WebDriver):
            try:
                self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").click()
            except:
                print("未找到搜索按钮")
            return "智能排序" in self.driver.page_source

        WebDriverWait(self.driver,10).until(wait)
        # 4、验证搜索结果的前五个店铺名，包含火锅
        size = self.driver.get_window_size()
        width = int(size.get("width"))
        height = size.get("height")
        name_list = []

        # 获取页面元素
        results = self.driver.find_elements(MobileBy.ID, "com.sankuai.meituan:id/poi_info_first_poiName")
        for ele in results:
            name = ele.get_attribute("text")
            if name not in name_list:
                name_list.append(name)
                print(f"店名为：{name}")

        final_result = name_list[:3]
        # for name in final_result:
        #     if search_key not in name:
        #         assert False
        # 验证每一个name 里都包含seach_key,如果有一个不包含则为False
        assert all([search_key in name for name in final_result])


