from selenium import webdriver
import csv
import time
import filecmp

driver = webdriver.Chrome()
driver.get("http://localhost:9999/another_form.html")


def find_and_clear_by_id(idt):
    element = driver.find_element_by_id(idt)
    element.clear()
    return element


add_button = driver.find_element_by_id('submit')

with open('table_in_006.csv', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_id("fullname").send_keys(row[0])
        find_and_clear_by_id("email").send_keys(row[1])
        find_and_clear_by_id("dob").send_keys(row[2])
        find_and_clear_by_id("phone").send_keys(row[3])
        add_button.click()

time.sleep(2)
export_button = driver.find_element_by_tag_name("button")
export_button.click()
time.sleep(2)
filecmp.clear_cache()
print(filecmp.cmp('table_in_006.csv', 'C:\\Users\\Simon\\Downloads\\table.csv', shallow=False))

driver.quit()
