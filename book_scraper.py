import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
url = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Data list
book_data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    rating_class = book.find("p", class_="star-rating")["class"][1]
    rating_map = {
        "One": "1",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5"
    }
    rating = rating_map.get(rating_class, "No Rating")

    book_data.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# Convert to CSV
df = pd.DataFrame(book_data)
df.to_csv("books_data.csv", index=False)

print("✅ Scraping done! Data saved to 'books_data.csv'")
