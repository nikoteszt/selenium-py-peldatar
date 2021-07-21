from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/scrolltoload.html")

time.sleep(3)
js = "window.scrollTo(0, 3000);"
for s in range(2):
    driver.execute_script(js)
    time.sleep(6)

images = driver.find_elements_by_xpath("//div[@class='image']")
print(len(images))
print()
i = 1
for j in images[:20]:
    url = (j.find_element_by_tag_name("img").get_attribute("src"))
    nev = str(j.find_element_by_tag_name("p").text)

    file_name = f'cats/{i}_{nev.replace("Cat id: ", "")}'
    r = requests.get(url)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)

    i += 1

driver.quit()
