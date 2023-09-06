from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
random_sleep = [7, 9, 10, 20, 15, 6]

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3656983339&f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true'
sign_in_xpath = '/html/body/div[1]/header/nav/div/a[2]'

driver.get(url)
driver.maximize_window()

# time.sleep(random.choice(random_sleep))
sign_in = driver.find_element(By.XPATH, value=sign_in_xpath)
sign_in.click()
# time.sleep(random.choice(random_sleep))

email_xpath = '//*[@id="username"]'
password_xpath = '//*[@id="password"]'
login_xpath = '//*[@id="organic-div"]/form/div[3]/button'

email = driver.find_element(By.XPATH, value=email_xpath)
email.send_keys("iheanacho.austin@gmail.com")
# time.sleep(random.choice(random_sleep))

password = driver.find_element(By.XPATH, value=password_xpath)
password.send_keys("money18.com")
# time.sleep(random.choice(random_sleep))

login = driver.find_element(By.XPATH, value=login_xpath)
login.click()
time.sleep(30)
save_xpath = '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button'

save = driver.find_element(By.XPATH, value=save_xpath)
