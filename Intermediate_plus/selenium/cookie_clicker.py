from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

cookie_url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(cookie_url)
cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")
        money = int(money)
        try:
            time_machine = driver.find_element(
                By.XPATH, value='//*[@id="buyTime machine"]/b')
            time_machine_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyTime machine"]/b').text.split("-")[1].strip().replace(",", ""))

            portal = driver.find_element(
                By.XPATH, value='//*[@id="buyPortal"]/b')
            portal_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyPortal"]/b').text.split("-")[1].strip().replace(",", ""))

            alchemy = driver.find_element(
                By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
            alchemy_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split("-")[1].strip().replace(",", ""))

            shipment = driver.find_element(
                By.XPATH, value='//*[@id="buyShipment"]/b')
            shipment_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyShipment"]/b').text.split("-")[1].strip().replace(",", ""))

            mine = driver.find_element(
                By.XPATH, value='//*[@id="buyMine"]/b')
            mine_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyMine"]/b').text.split("-")[1].strip().replace(",", ""))

            factory = driver.find_element(
                By.XPATH, value='//*[@id="buyFactory"]/b')
            factory_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyFactory"]/b').text.split("-")[1].strip().replace(",", ""))

            grandma = driver.find_element(
                By.XPATH, value='//*[@id="buyGrandma"]/b')
            grandma_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyGrandma"]/b').text.split("-")[1].strip().replace(",", ""))

            cursor = driver.find_element(
                By.XPATH, value='//*[@id="buyCursor"]/b')
            cursor_amount = int(driver.find_element(
                By.XPATH, value='//*[@id="buyCursor"]/b').text.split("-")[1].strip().replace(",", ""))
        except AttributeError:
            pass

        if money >= time_machine_amount:
            time_machine.click()
        elif money >= portal_amount:
            portal.click()
        elif money >= alchemy_amount:
            alchemy.click()
        elif money >= shipment_amount:
            shipment.click()
        elif money >= mine_amount:
            mine.click()
        elif money >= factory_amount:
            factory.click()
        elif money >= grandma_amount:
            grandma.click()
        elif money >= cursor_amount:
            cursor.click()
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
