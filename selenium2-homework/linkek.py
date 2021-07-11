from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999")
    time.sleep(1)
    sumlink = driver.find_elements_by_xpath("//a")

    lf = open("linkek_file.txt", "w", encoding="utf-8")

    for a in sumlink:
        print(a.get_attribute("href"), file=lf)
    print("Talált linkek száma: ", len(sumlink))

    lf.close()

finally:
    driver.quit()
