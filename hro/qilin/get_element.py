from hro.qilin.delayed import wrapper


@wrapper
def get_elements_by_class_name_send(driver, name, index, content):
    el = driver.find_elements_by_class_name(name)[index]
    el.clear()
    el.send_keys(content)


@wrapper
def get_element_by_class_name_click(driver, name):
    el = driver.find_element_by_class_name(name)
    el.click()
