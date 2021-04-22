from bs4 import BeautifulSoup
import requests
response= requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_site= response.text
soup = BeautifulSoup(empire_site, 'html.parser')
print(soup)

movie_info = soup.find(name='h3', class_='jsx-4245974604')
print(movie_info)
movie_list = [movie.getText() for movie in soup.find_all(name="h3", class_="jsx-4245974604")]
print(movie_list)