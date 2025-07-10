"""
Developer: Meher Salim
File: web-scraper.py
Project Name: News Article Web Scraper
Description:
- This script scrapes news articles from a specified website using requests and BeautifulSoup.
- It extracts article titles, summaries, publication dates, and URLs.
- The scraped data can be saved to a CSV file for further analysis.
- I have tailored this project to work with CNN.com
- If you are looking to search other news outlets, you just have to make slight changes in
  code where prompted
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# Constants
BASE_URL = "https://www.cnn.com"  # Replace with your choice of news website
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}
OUTPUT_FILE = "cnn_articles.csv"
MAX_PAGES = 3  # Reduced due to CNN's pagination limits
DELAY = 5  # Increased delay to avoid blocks

def get_soup(url):
    """
    Fetch and parse a webpage.
    Args:
        url: URL to fetch
    Returns:
        BeautifulSoup object or None if request fails
    """
    try:
        # Add delay to be polite to the server
        time.sleep(DELAY + random.uniform(0, 2))
        
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse HTML content
        # Check if we got a valid HTML response
        if 'text/html' not in response.headers.get('Content-Type', ''):
            print(f"Unexpected content type from {url}")
            return None
            
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None

def extract_article_data(article_tag):
    """
    Extract relevant data from an article HTML tag.
    Args:
        article_tag: BeautifulSoup tag containing article
    Returns:
        Dictionary with article data or None if extraction fails
    """
    try:
        # CNN's current structure (as of 2024)
        title_element = article_tag.find(['span', 'h3'], class_=['container__headline-text', 'headline__text'])
        if not title_element:
            return None
            
        title = title_element.get_text(strip=True)
        
        # Get URL
        link = article_tag.find('a', href=True)
        if not link:
            return None
            
        url = link['href']
        if url.startswith('/'):
            url = f"https://www.cnn.com{url}"
            
        # Get summary
        summary_element = article_tag.find('div', class_=['container__description', 'headline__sub-text'])
        summary = summary_element.get_text(strip=True) if summary_element else "No summary available"
        
        # Get date - often requires visiting article page
        date = "N/A"
        
        return {
            'title': title,
            'summary': summary,
            'url': url,
            'date': date
        }
    except Exception as e:
        print(f"Error parsing article: {str(e)}")
        return None

def scrape_news_page(page_num=1):
    """
    Scrape a single page of news articles.
    Args:
        page_num: Page number to scrape
    Returns:
        List of article dictionaries
    """
    url = f"{BASE_URL}/us"
    soup = get_soup(url)
    if not soup:
        return []
    
    articles = []
    # CNN uses multiple containers for articles
    containers = [
        'container__item',
        'card',
        'stack__item'
    ]
    
    for container in containers:
        article_tags = soup.find_all('div', class_=container)
        for tag in article_tags:
            article_data = extract_article_data(tag)
            if article_data:
                articles.append(article_data)
    
    return articles

def save_to_csv(articles, filename=OUTPUT_FILE):
    """
    Save scraped articles to a CSV file.
    Args:
        articles: List of article dictionaries
        filename: Output filename
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['title', 'summary', 'url', 'date'])
            writer.writeheader()
            writer.writerows(articles)
        print(f"Saved {len(articles)} articles to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {str(e)}")

def main():
    """
    Main scraping function.
    Scrapes multiple pages and saves results.
    """
    print(f"Starting CNN news scraping...")
    articles = scrape_news_page()
    
    if articles:
        save_to_csv(articles)
        print(f"Scraped {len(articles)} articles")
    else:
        print("No articles found. CNN's structure may have changed.")

if __name__ == "__main__":
    main()
