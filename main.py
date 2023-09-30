import requests
from bs4 import BeautifulSoup
import csv

# ADD FUNCTION: scrap movie data from imdb


class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_titles(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            article_text = soup.find_all("span", attrs={"class": "text"})
            article_authors = soup.find_all("small", attrs={"class": "author"})
            titles = [title.text for title in article_text]
            authors = [author.text for author in article_authors]
            return titles, authors
        else:
            print("Failed to retrieve the webpage")
            return []

    def export_to_csv(self, data, data2, filename):
        file = open(filename, "w")
        writer = csv.writer(file)
        writer.writerow(["QUOTES", "AUTHORS"])
        for data, data2 in zip(data, data2):
            writer.writerow([data, data2])
        file.close()
        print(f"Data exported to {filename}")


url_to_scrape = "https://quotes.toscrape.com/"
scraper = WebScraper(url_to_scrape)

text, writer = scraper.scrape_titles()

if text:
    scraper.export_to_csv(text, writer, "scraped_titles.csv")
