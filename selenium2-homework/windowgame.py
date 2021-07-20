from selenium import webdriver
import time
import random

driver = webdriver.Chrome()

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html")
main_window = driver.window_handles[0]
target_color = driver.find_element_by_id("target_color").text
number_of_guesses = driver.find_element_by_id("numberOfGuesses")

buttons = driver.find_elements_by_xpath("//button[@id]")


stop = 99
while True:
    i = random.randint(0, stop)
    buttons[i].click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

    if not driver.find_element_by_tag_name("h1").text == target_color:
        stop -= 1
    else:
        break

    driver.close()

    driver.switch_to.window(main_window)
    time.sleep(1)
    buttons.pop(i)


time.sleep(2)
driver.switch_to.window(main_window)
print(number_of_guesses.text, " lépésből találtad meg a megfelelő ablakot.")

driver.quit()
