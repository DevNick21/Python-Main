from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(url=URL)
webpage = res.text

# print(movie_names)
soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_names = [movie.get_text() for movie in movies[::-1]]
with open("top_100_movies _of_all_time/movies.txt", "w", encoding="utf-8") as data:
    for movie in movie_names:
        if movie == "12: The Godfather Part II":
            movie = "12) The Godfather Part II"
        data.write(f"({movie}\n")
