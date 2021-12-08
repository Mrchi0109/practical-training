# 使用pytest 测试框架编写测试用例的规范
# 1. 测试用例文件需要以test开头命名
# 2. 安装 pytest 第三方库
# 3. 在 settings->tools 选择 default test runner 为 pytest
# 4. 新建一个测试函数 `def test_search():`
#
import time

from selenium import webdriver

def test_search():
    """
    完成测试步骤的编写
    1. 进入招聘页面
    2. 输入“测试” 关键字
    3. 点击搜索按钮
    3. 查看的每一条招聘信息是否有“测试”两个字
    拿预期结果和实际结果进行对比
    """
    # 实例化一个 driver 对象
    driver = webdriver.Chrome()
    # 打开指定的网页
    driver.get("https://jobs.bytedance.com/campus/position")
    # 通过driver 实例对象调用查找元素的方法，by 后面是什么，就是使用的哪种定位方式
    # 输入 定位信息 作为参数
    # 返回元素对象
    ele = driver.find_element_by_css_selector("#bd > section > section > main > div > div > div.header__36dmY > div > div.search-block.searchBlock__1mh35 > span > input")
    # 元素对象调用 输入内容的方法
    ele.send_keys("测试")
    # 返回元素对象2, 对元素对象2（搜索按钮），进行点击
    driver.find_element_by_css_selector(
        "#bd > section > section > main > div > div > div.header__36dmY > div > div.search-block.searchBlock__1mh35 > span > span.atsx-input-suffix > button")\
        .click()
    time.sleep(2)
    test_ele = driver.find_element_by_xpath('//*[@id="bd"]/section/section/main/div/div/div[2]/div[3]/div[1]/div[2]/a[1]/div/div[1]/span')
    print(test_ele.text)
    # 断言测试关键字是否在获取到的标题中
    assert "测试" in test_ele.text