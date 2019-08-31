from selenium import webdriver
import os
import shutil
import re
from config import *
from getpass import getpass


def GetClassTable():
    # TODO: Replace the getter from selenium to requests_html, selenium is too huge!
    username = ''
    password = ''
    default = True
    if ('default' in CONFIG.keys()):
        default = bool(CONFIG['default'])
    if (not 'userName' in CONFIG.keys() or not 'passWord' in CONFIG.keys()):
        print("Can't find 'userName' and 'passWord' in config!")
        username = input("Username:")
        password = getpass()
    else:
        username = CONFIG['userName']
        password = CONFIG['passWord']
    options = webdriver.ChromeOptions()
    if ('.downloadTable' in os.listdir()):
        shutil.rmtree(".downloadTable")
    subPath = os.path.join(os.getcwd(), '.downloadTable')
    prefs = {'download.default_directory': subPath}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=options)
    print("pyBeiHangCalGenerator-OnlineGetter")
    print("Logging in...")
    driver.get(
        'https://sso.buaa.edu.cn/login?service=http%3A%2F%2F10.200.21.61%3A7001%2Fieas2.1%2Fwelcome'
    )
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()
    if (str(driver.current_url).find("://10.200.21.61") == -1):
        print("Login Failed!")
        return False
    print("Trying to get class table...")
    driver.get("http://10.200.21.61:7001/ieas2.1/kbcx/queryGrkb")
    if (not default):
        select = driver.find_element_by_name("xnxq")
        selections = select.find_elements_by_css_selector("option")
        for k, option in enumerate(selections):
            print(str(k) + ": " + option.text)
        s = input("Select a classTable file" + " (0 - " +
                  str(len(selections) - 1) + "): ")
        selections[int(s)].click()
    driver.execute_script("exportExcel();")
    files = []
    while len(files) == 0 or not re.match(r".*\.xls$", files[0]):
        files = os.listdir(subPath)
    xlsFileName = files[0]
    print("Downloaded class table file: " + xlsFileName + ", moving...")
    shutil.copy(os.path.join(subPath, xlsFileName), 'table.xls')
    print("Success!")
    shutil.rmtree(".downloadTable")
    driver.close()
    return True


if __name__ == '__main__':
    GetClassTable()
