from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'English')]"))
)
language = driver.find_element(By.XPATH,"//*[contains(text(),'English')]")
language.click()
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)
cookie = driver.find_element(By.ID, "bigCookie")
while True:
    cookie_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))
    cookie.click()
    #print(cookie_count)
    for i in range(4):
        product_price = driver.find_element(By.ID,"productPrice"+str(i)).text.replace(",","")
        if not product_price.isdigit():
            continue
        product_price = int(product_price)
        if cookie_count>=product_price:
            product = driver.find_element(By.ID,"product"+str(i))
            product.click()
            break