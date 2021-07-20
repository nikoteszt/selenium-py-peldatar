from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/dragndrop2.html")


def js_dnd(dragged, dropped):
    f2 = open("dnd.js", "r")
    javascript2 = f2.read()
    f2.close()
    time.sleep(2)
    driver.execute_script(javascript2, dragged, dropped)


time.sleep(2)

drag1 = driver.find_element_by_id("Pizza")
drop1 = driver.find_element_by_id("Doing")
js_dnd(drag1, drop1)


drag2 = driver.find_element_by_id("Tacos")
drop2 = driver.find_element_by_id("Doing")
js_dnd(drag2, drop2)


drag3 = driver.find_element_by_id("BBQ")
drop3 = driver.find_element_by_id("Doing")
js_dnd(drag3, drop3)


drag4 = driver.find_element_by_id("Burgers")
drop4 = driver.find_element_by_id("Doing")
js_dnd(drag4, drop4)

driver.implicitly_wait(5)
