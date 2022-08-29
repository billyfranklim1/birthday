import datetime
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

eleNM = None
 
def wish_birth(name):
    return "Parabéns " + name + " ! Que Deus te abençoe e te proteja sempre. Feliz aniversário!"
 
def getJsonData(file, attr_ret, attr1, attr2, attr_val1, attr_val2):
    data = json.load(file)
    retv =[]
    for i in data:
        if(i[attr1]== attr_val1 and i[attr2]== attr_val2):
           retv.append(i[attr_ret])
    return retv
 
data_file = open("birthdays.json", "r")
# data_file = open("birthdays-test.json", "r")
namev =[]
print("Script Running")

while True:
    try:
        datt = datetime.datetime.now()
        namev = getJsonData(data_file, "name", "birth_month", "birth_date",
                                           str(datt.month), str(datt.day))
 
    except json.decoder.JSONDecodeError:
        continue
    if(namev !=[]):
        break

    

options = Options()
options.add_argument("--user-data-dir=/home/billy/.config/google-chrome")
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 



driver.get("https://web.whatsapp.com/")


# delay added to give time for all elements to load
time.sleep(10)

eleNM = driver.find_element(By.XPATH, '//span[@title ="Pega na minha sword"]')
eleNM.click()
 
for inp in namev:
 
    while(True):
        input_box = driver.find_element(By.XPATH, '//div[@title ="Type a message"]')
        input_box.click()
        input_box.send_keys(wish_birth(inp))
        sendbutton = driver.find_element(By.XPATH, '//button[@data-testid ="compose-btn-send"]')
        sendbutton.click()
        break