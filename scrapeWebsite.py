# impliment a python code that can scrapes data from website using "requests" and "beatifulsoup4" module
# import the necessary module and functions to make http requet and parse html
# scrape and extract specific data from a web page of your choice 
# print or process the extracted data as per your requirements

import requests
from bs4 import BeautifulSoup

def fetch_article_titles(url):
    # Updated headers with Chrome's User-Agent string
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
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
    # The tag and class should be based on the website structure
    article_titles = [article.text for article in soup.find_all("h1")]
    article_paragraph = [article.text for article in soup.find_all("p")]
    
    if article_titles:
        print(f"Found {len(article_titles)} articles.")
        for i, title in enumerate(article_titles, 1):
            print(f"{i}. {title}")
    else:
        print("No articles titles found.")

    if article_paragraph:
        print(f"Found {len(article_paragraph)} paragraph.")
        for i, paragraph in enumerate(article_paragraph, 1):
            print(f"{i}. {paragraph}")
    else:
        print("No articles paragraph found.")

if __name__ == "__main__":
    # Replace this URL with the website you want to scrape
    url = "https://realpython.com/iterate-through-dictionary-python/"
    fetch_article_titles(url)
