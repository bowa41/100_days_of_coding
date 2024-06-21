from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="span", class_="titleline")
upvotes = soup.find_all(name="span", class_="score")
# print(article_tag)
article_texts = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

# for link in links:
#     article_link = link.get("href")
#     print(article_link)
#     article_links.append(article_link)

# article_link = soup.find_all(name="a").get("href")
article_links = [links.select_one("a").get("href") for links in articles]
article_upvotes = [int(upvote.getText().split()[0]) for upvote in upvotes]

index = article_upvotes.index(max(article_upvotes))
print(index)
print(article_texts[index])
print(article_links[index])










# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.li)
#
# #find all tags of a specific type/name
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# #loop through tags and print each one
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# #Search for specific maatches
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# #search for class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# #to just get text inside a find, use .gettext
# print(section_heading.getText())

# #get value of attirbute
# print(section_heading.get("class"))
#
# #use css selectors
# # company_url = soup.select_one(selector="p a")
# # company_url = soup.select_one(selector="#name")
# company_url = soup.select_one(selector=".heading")
# print(company_url)