# News Article Web Scraper
## Developer: Meher Salim

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python script that scrapes news articles from a specified website using requests and BeautifulSoup. Extracts article titles, summaries, publication dates, and URLs, then saves the data to a CSV file for analysis. Includes polite scraping practices with delays and error handling. The base project is geared towards CNN's web structure.

## Features

- **Web Scraping**: Uses requests and BeautifulSoup to fetch and parse HTML content
- **Data Extraction**: Extracts article titles, summaries, publication dates, and URLs
- **CSV Export**: Saves scraped data to a structured CSV file
- **Polite Scraping**:
  - Implements delays between requests (5+ seconds)
  - Random delay variation to avoid pattern detection
  - Standard browser User-Agent header
- **Error Handling**: Robust error handling for failed requests or malformed data
- **Configurable**: Easy to modify for different news websites

## Installation

1. Clone the repository:
bash
git clone [https://github.com/mehersalim/News-Article-Web-Scraper]
cd news-web-scraper

2. Install the required dependencies:
bash
pip install requests beautifulsoup4

## Usage
1. Run the scraper:
bash
python web-scraper.py

2. Output:
The script generates a cnn_articles.csv file with the scraped data.

## Configuration Options
  - BASE_URL: Target news website (default: CNN)
  - HEADERS: Request headers including User-Agent
  - OUTPUT_FILE: Name/path for CSV output
  - DELAY: Seconds between requests (default: 5)
  - Modify extract_article_data() to match different website structures

## Customizating for Other Websites

To adapt this scraper for other news sites:
1. Update BASE_URL
2. Modify the CSS selectors in extract_article_data()
3. Adjust HEADERS if needed
4. Update container classes in scrape_news_page()

## Limitations
  - Currently optimized for CNN's HTML structure
  - Date extraction requires visiting individual article pages (currently shows "N/A")
  - Pagination limited to front page articles
  - Does not automatically check robots.txt (please verify manually)

# File Structure

## Best Practices

  - **Respect robots.txt**: Always check the target website's robots.txt before scraping.
  - **Rate Limiting**: The script includes delays to avoid aggressive scraping.
  - **User-Agent**: Uses standard browser headers to mimic organic traffic.
  - **Error Handling**: Gracefully handles network issues and parsing errors.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License.
