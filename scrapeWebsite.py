# impliment a python code that can scrapes data from website using "requests" and "beatifulsoup4" module
# import the necessary module and functions to make http requet and parse html
# scrape and extract specific data from a web page of your choice 
# print or process the extracted data as per your requirements

import requests
from bs4 import BeautifulSoup

def fetch_article_titles(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Make HTTP request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find and print article titles
    # Assuming articles are in h2 tags with class 'entry-title'
    article_titles = [article.text for article in soup.find_all("h1", class_="entry-title")]
    
    if article_titles:
        print(f"Found {len(article_titles)} articles.")
        for i, title in enumerate(article_titles, 1):
            print(f"{i}. {title}")
    else:
        print("No articles found.")

if __name__ == "__main__":
    # Replace this URL with the website you want to scrape
    url = "https://realpython.com/iterate-through-dictionary-python/"
    fetch_article_titles(url)
