# coding: utf-8
import time
from selenium import webdriver
from hro.qilin.get_element import get_elements_by_class_name_send, get_element_by_class_name_click


def main_func():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=option)
    driver.implicitly_wait(10)
    url = "http://172.16.14.115:3101/login"
    driver.get(url)
    driver.maximize_window()
    get_elements_by_class_name_send(driver, "el-input__inner", 0, "18238484337")
    get_elements_by_class_name_send(driver, "el-input__inner", 1, "Q9X6P8")
    get_element_by_class_name_click(driver, "el-button")
    # yzm = input("请输入验证码")
    # input_yzm = driver.find_elements_by_class_name("el-input__inner")[2]
    # input_yzm.send_keys(yzm)
    # time.sleep(10)
    # loggin.click()
    time.sleep(30000)

# eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2MDMyOTQ5ODUyNTY3NDI5MTIiLCJ1c2VySWQiOjYwMzI5NDk4NTI1Njc0MjkxMiwicGxhdGZvcm0iOiJQQ19DTElFTlQiLCJpcCI6IjE3Mi4xNi4xNC4xMjUiLCJkZXZpY2VJZCI6IjU1MDgzODQ4NzIwNjA3Mjk2MCIsInZlcnNpb24iOiIwLjAuMSIsInJvb3RPcmdJZCI6MSwib3JnSWQiOjcxNywic3RhZmZJZCI6NjAzMjk0Nzc3MzMyNTEwNzIwLCJpYXQiOjE1NjQ0ODE0NjEsImV4cCI6MTU2NDU2Nzg2MX0.XoYQmdp07v3Wkf4XewlwmpLIC04piv7WLoUoYOE-r0M


if __name__ == '__main__':
    main_func()
