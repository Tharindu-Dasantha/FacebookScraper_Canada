import requests
from bs4 import BeautifulSoup

url = 'https://web.facebook.com/pages/Bread-and-Rose-Bakery-Cafe'
newfile = open("Test.txt", "w")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser').find("body").find_all("div")
for item in soup:
    newfile.write(f"{item}")
    newfile.write("\n\n\n")

# # Find the div that contains the post content
# post_divs = soup.find_all('div', {'class': 'userContentWrapper'})
# for post_div in post_divs:
#     print(post_div)
#     # Extract the post text
#     post_text = post_div.find('div', {'class': 'userContent'}).text
#     print(post_text)