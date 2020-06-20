import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "D:\PythonScript\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com")

timeout = time.time() + 15
try:
    while(driver.find_element_by_class_name("_1QMFu")):
        print("Waiting 15s for login...")
        if time.time() > timeout:
            print("Sorry login timed out...")
            break
except:
    pass

print("Waiting to 3s to load...\n----------ENTER CONTACT NAME----------")
contact_name = str(input())
print("----------ENTER THE NUMBER OF TIME YOU WANT TO SEND THE MESSAGE----------")
message_count = int(input().rstrip())
print("----------ENTER THE MESSAGE YOU WANT TO SEND----------")
message = str(input())
time.sleep(3)

print("Locating searchbar...")
search_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(search_xpath))
input_box_search.click()

print("Searching contact...")
input_box_search.send_keys(contact_name)
time.sleep(3)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact_name+"']")
selected_contact.click()

print("Contact Located...")
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)

print("Sending Message...")
for _ in range(message_count):
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(5)
    driver.quit()
