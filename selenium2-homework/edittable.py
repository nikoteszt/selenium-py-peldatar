import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/editable-table.html")

add_button = driver.find_element_by_xpath('//div/button[@class="btn btn-success pull-right"]')
search_field = driver.find_element_by_xpath('//input[@placeholder="Search..."]')


def add_row_table(n, p, q, c):
    add_button.click()
    time.sleep(1)
    add_name = driver.find_element_by_xpath('//input[@name="name" and @value=""]')
    add_name.send_keys(n)
    add_price = driver.find_element_by_xpath('//input[@name="price" and @value=""]')
    add_price.send_keys(p)
    add_qty = driver.find_element_by_xpath('//input[@name="qty" and @value="0"]')
    add_qty.send_keys(q)
    add_category = driver.find_element_by_xpath('//input[@name="category" and @value=""]')
    add_category.send_keys(c)

    # Kikényszerítjük a DOM frissítését
    search_field.send_keys("xxxxx")
    search_field.send_keys(Keys.BACKSPACE * 5)


add_row_table("Galaxy S3", "110.05", "5", "Electronics")
add_row_table("Yoda", "30", "5", "soft toys")
