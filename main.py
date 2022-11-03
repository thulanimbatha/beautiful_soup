from bs4 import BeautifulSoup


with open("website.html", mode="r", encoding="utf8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")

anchor_tags = soup.find_all(name="a")
print(anchor_tags)

for a in anchor_tags:
    print(a.get("href"))
