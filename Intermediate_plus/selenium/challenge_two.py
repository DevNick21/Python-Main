from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Todo
number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
number.click()

# Todo
driver.maximize_window()
search = driver.find_element(
    By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()

# Todo
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")
fname.send_keys("Iheanacho")
lname.send_keys("Ekene")
email.send_keys("jdjjdjd@gmail.com")
button.click()
