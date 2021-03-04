import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get all the topics name
topics_html = requests.get("https://www.brainyquote.com/topics").text
topics_soup = BeautifulSoup(topics_html, 'html.parser')

topics = []
for topic_name in topics_soup.findAll("span", {"class": "topicContentName"}):
    topics.append(topic_name.get_text().lower().replace(" ", "-").replace("'", ""))

for topic in topics:
    quotes = []

    topic_url = "https://www.brainyquote.com/topics/" + topic

    # Get single topic pagination
    topic_html = requests.get(topic_url).text
    topic_soup = BeautifulSoup(topic_html, 'html.parser')

    pages = int(topic_soup.select_one("ul.pagination > li:nth-last-child(2) > a").get_text())

    # Make pagination links
    urls = [topic_url]
    for page in range(2, pages + 1):
        urls.append("https://www.brainyquote.com/topics/" + topic + "_" + str(page))

    # Scrap every single pagination
    for url in urls:
        topic_html = requests.get(url).text
        topic_soup = BeautifulSoup(topic_html, 'html.parser')

        for quote in topic_soup.findAll("div", {"class": "bqQt"}):
            try:
                title = quote.find("a", {"class": "b-qt"}).text.strip()
                author = quote.find("a", {"class": "bq-aut"}).text.strip()
                tags = []

                for tag in quote.findAll("a", {"class": "oncl_klc"}):
                    tags.append(tag.text.strip())

                tags = ", ".join(tags)

                quotes.append({
                    "title": title,
                    "author": author,
                    "tags": tags
                })
            except:
                pass

    # Save data into csv
    pd.DataFrame(quotes).to_csv(topic + ".csv", index=False)
