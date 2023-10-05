from bs4 import BeautifulSoup
import requests


form = "https://docs.google.com/forms/d/e/1FAIpQLSf1ISDgDJ78oZMqrZd0chIYJ-BI-nh4LrYh12RNlnadpM_vOQ/viewform?usp=sf_link"
on_listings = 'https://www.zillow.com/on/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A56.859036%2C%22east%22%3A-74.320381%2C%22south%22%3A41.676328%2C%22west%22%3A-95.156001%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A373579%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A5%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A404375%2C%22regionType%22%3A2%7D%5D%2C%22usersSearchTerm%22%3A%22ON%22%2C%22schoolId%22%3Anull%2C%22pagination%22%3A%7B%7D%7D'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/108.0.0.0 Safari/537.36 ',
    'Accept-Language': 'en-US,en;q=0.9',
}
res = requests.get(on_listings)
res.raise_for_status()
zillow_web_page = res.text
soup = BeautifulSoup(zillow_web_page, "html.parser")
print(soup)
