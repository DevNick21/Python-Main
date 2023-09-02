from selenium import webdriver
from selenium.webdriver.common.by import By
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.python.org")

events = driver.find_element(
    By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.splitlines()
# print(events)
dictionary = {i: {'time': events[i], 'name': events[i+1]}
              for i in range(0, len(events), 2)}

print(dictionary)

driver.quit()
