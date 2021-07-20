from selenium import webdriver
import csv
import time
import filecmp

driver = webdriver.Chrome()
# driver.get("http://localhost:9999/another_form.html")
driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/another_form.html")


def find_and_clear_by_id(idt):
    element = driver.find_element_by_id(idt)
    element.clear()
    return element


add_button = driver.find_element_by_id('submit')

with open('table_in_006.csv', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        # print(row)
        find_and_clear_by_id("fullname").send_keys(row[0])
        find_and_clear_by_id("email").send_keys(row[1])
        find_and_clear_by_id("dob").send_keys(row[2])
        find_and_clear_by_id("phone").send_keys(row[3])
        add_button.click()

time.sleep(2)
export_button = driver.find_element_by_tag_name("button")
export_button.click()
time.sleep(2)

file1 = "table_in_006.csv"
file2 = "C:\\Users\\Simon\\Downloads\\table.csv"

filecmp.clear_cache()
print("A csv filek (bit szerintű) identikálásának az eredménye:")
print(filecmp.cmp(f'{file1}', f'{file2}', shallow=False))
print("-" * 50)
print("A csv filek (tartalom szerinti) identikálásának az eredménye:")


def get_csv_file_lines(file):
    with open(file, 'r', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file)
        for rowtext in rows:
            yield rowtext


def compare_csv_files_line_by_line(csv_file_one, csv_file_two):
    csvfile_02 = get_csv_file_lines(csv_file_two)
    for line_one in get_csv_file_lines(csv_file_one):
        line_two = csvfile_02.__next__()
        if line_two != line_one:
            print('File names being compared:')
            print(f'csv_file_one: {csv_file_one}')
            print(f'csv_file_two: {csv_file_two}')
            print(f'The following rows have difference in the files being compared.')
            print('csv_file_one:', line_one)
            print('csv_file_two:', line_two)
            print('\n')


print(f'A {file1} és {file2} közti különbségek:')
compare_csv_files_line_by_line(file1, file2)

driver.quit()
