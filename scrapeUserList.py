import requests
from bs4 import BeautifulSoup
import re

URL = "http://www.redditanimelist.net/users.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('table', class_='users')
link_elements = results.find_all('a')


File_object = open(r"mal_reddit_user_list.txt", "a")

num = 0
for link_element in link_elements:
	num = num + 1
	if num % 2 == 1:
		continue

	File_object.write(link_element.text.strip() + "\n")

File_object.close()