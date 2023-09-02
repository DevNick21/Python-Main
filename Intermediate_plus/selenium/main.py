from selenium import webdriver
from selenium.webdriver.common.by import By
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Bluetooth-Belt-Driven-Turntable-Speakers-Headphone/dp/B07N3WYLKZ/ref=sr_1_1_sspa?crid=4JPX636TJ4QJ&keywords=vinyl+player&qid=1692367737&sprefix=vinyl+p%2Caps%2C1197&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A1P1OHB2JFMIPI")
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text} dollars and {price_cents.text} cents")
# driver.close()
driver.quit()
