import time

from selenium import webdriver
from datetime import date, datetime

driver = webdriver.Chrome()

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/forms.html")
date_input = driver.find_element_by_id("example-input-date")
time.sleep(2)
date_input_value = date(2021, 6, 5).strftime("00%Y-%m-%d")
# print(date_input_value)
date_input.send_keys(date_input_value)

datetime_input = driver.find_element_by_id("example-input-date-time")
time.sleep(2)
datetime_input_value = datetime(2012, 5, 5, 5, 5, 5, 555000).strftime("%Y.%m.%d %H:%M:%S:%f")
# print(datetime_input_value)
datetime_input.send_keys(datetime_input_value)

datetime_local_input = driver.find_element_by_id("example-input-date-time-local")
time.sleep(2)
datetime_local_input_value = datetime(2000, 5, 12, 12, 1).strftime("00%Y.%m.%dT%H:%M")
# print(datetime_local_input_value)
datetime_local_input.send_keys(datetime_local_input_value)

datetime_month = driver.find_element_by_id("example-input-month")
time.sleep(2)
datetime_month_value = datetime(1995, 12, 26).strftime("00%Y%B")
# print(datetime_month_value)
datetime_month.send_keys(datetime_month_value)

datetime_week = driver.find_element_by_id("example-input-week")
time.sleep(2)
datetime_week_value = datetime(2015, 12, 29).strftime("%W.hét,%Y")
# print(datetime_week_value)
datetime_week.send_keys(datetime_week_value)

datetime_time = driver.find_element_by_id("example-input-time")
time.sleep(2)
datetime_time_value = datetime(2021, 7, 16, 0, 25).strftime("%H:%M")
# print(datetime_time_value)
datetime_time.send_keys(datetime_time_value)

time.sleep(4)
driver.quit()
