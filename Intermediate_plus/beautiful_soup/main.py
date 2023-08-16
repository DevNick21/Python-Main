from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")

yc_web_page = res.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(
            class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(f"{article_titles[max_points_index]}, {article_upvotes[max_points_index]} points, available at: {article_links[max_points_index]}.")
