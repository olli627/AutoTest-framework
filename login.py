from time import sleep, time

from selenium import webdriver
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 初始化
driver = webdriver.Edge()
driver.get("http://webdriveruniversity.com/")
driver.maximize_window()

try:
    # 1. 点击 login 链接
    driver.find_element(By.XPATH, "(//*[@class='section-title'])[2]").click()

    # 2. 切换到新窗口
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    # 3. 等待页面标题更新
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("WebDriver | Login Portal"))
    print("页面标题已更新为 'WebDriver | Login Portal'")

    # 4. 传值并登录
    driver.find_element(By.XPATH, "//*[@placeholder='Username']").send_keys("kongxinbo")
    driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("0627violaz")
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()

    # 5. 处理可能的警告框
    try:
        # 等待警告框出现
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"警告框内容: {alert.text}")
        alert.accept()  # 或者使用 alert.dismiss() 根据需要
    except (NoAlertPresentException, TimeoutException):
        print("没有发现警告框。")

    # 6. 保存截图并关闭浏览器
    driver.save_screenshot("current_page.png")
    sleep(5)
finally:
    driver.quit()