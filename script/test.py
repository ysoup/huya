from selenium import webdriver
import time
import json

# 读取配置文件
with open("../config/ws.json", "r") as fi:
    load_dict = json.load(fi)

# 模拟
browser = webdriver.PhantomJS(executable_path='/usr/phantomjs/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',
                              service_log_path="test.log")
url = load_dict["crawler_url"]
browser.get(url)

browser.find_element_by_id("nav-login").click()
time.sleep(3)
login_class = browser.find_element_by_css_selector("[class='UDBSdkLgn-switch UDBSdkLgn-webQuick']")
login_class.find_element_by_tag_name("img").click()

# 模拟登录
browser.find_element_by_css_selector("[class='UDBSdkLgn-lgInput E_acct']").send_keys(load_dict["user_name"])
browser.find_element_by_css_selector("[class='UDBSdkLgn-lgInput E_passwd']").send_keys(load_dict["pass_word"])
browser.find_element_by_css_selector("[class='UDBSdkLgn-lgButton E_login']").click()
time.sleep(3)

# 生成登陆后快照
browser.save_screenshot("huya.png")
browser.quit()