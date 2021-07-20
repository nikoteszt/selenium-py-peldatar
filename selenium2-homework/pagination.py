from selenium import webdriver
import pprint
import time

driver = webdriver.Chrome()
extracted_data = []
fname = ""
try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/pagination.html")
    while True:
        time.sleep(2)
        table = driver.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")

        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            fname = cells[1].text
            if fname[0] == "A":
                data_row["id"] = cells[0].text
                data_row["first_name"] = cells[1].text
                data_row["second_name"] = cells[2].text
                data_row["surname"] = cells[3].text
                data_row["second_surname"] = cells[4].text
                data_row["birth_date"] = cells[5].text
                extracted_data.append(data_row)
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

    pprint.pprint(extracted_data)
    print(len(extracted_data))

    csvwrite = open("pagination.csv", "w", encoding="utf-8")
    csv_row1 = extracted_data[0]
    csv_rown = {}
    for k in csv_row1.keys():
        print(k + ",", end="", file=csvwrite)
    print("", file=csvwrite)
    for i in range(len(extracted_data)):
        csv_rown[i] = extracted_data[i]
        for v in csv_rown[i].values():
            print(v + ",", end="", file=csvwrite)
        print("", file=csvwrite)


finally:
    driver.close()
