Here's a README file for your Yellow Pages Scraper application:

# Yellow Pages Scraper

## Overview

This is a Python-based application that scrapes business information from Yellow Pages search results. The application extracts business names, phone numbers, and website links, and saves the collected data into an Excel file. It uses the `requests` library to fetch web pages, `BeautifulSoup` for parsing HTML, and `pandas` for data manipulation and saving to Excel. The application also features a simple GUI built with `tkinter` for ease of use.

## Features

- Scrapes business names, phone numbers, and website links from Yellow Pages search results.
- Saves the collected data into an Excel file.
- Simple GUI for entering the URL and number of pages to scrape.
- Handles consecutive rows with matching data to avoid duplicates.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `tkinter` (usually included with Python installations)

## Installation

1. Clone this repository to your local machine.
2. Install the required libraries using pip:
   ```sh
   pip install requests beautifulsoup4 pandas
   ```

## Usage

1. Run the application:
   ```sh
   python yellow_pages_scraper.py
   ```
2. Enter the URL of the Yellow Pages search results and the number of pages to scrape.
3. Click the "Scrape" button to start the scraping process.
4. The data will be saved to an Excel file in the location you choose.

## Example

1. URL format:
   ```
   https://www.yellowpages.ca/search/si/1/plumber/Service+Road+North+Mississauga+ON
   ```
2. Number of pages: `5`
3. The application will scrape the first 5 pages of search results and save the data to an Excel file.

## Code Explanation

### `scrape_yellow_pages(url)`

This function takes a URL, sends a GET request to it, parses the HTML response, and extracts business names, phone numbers, and website links. It returns a list of dictionaries containing the extracted data.

### `start_scraping(url, pages)`

This function manages the scraping process. It constructs the URLs for each page, calls `scrape_yellow_pages` for each URL, and collects the data. It then processes the data to handle consecutive rows with matching website links and saves the data to an Excel file.

### `on_scrape_button_click()`

This function is triggered when the "Scrape" button is clicked. It starts the scraping process in a separate thread to keep the GUI responsive.

### GUI

The GUI is created using `tkinter`. It includes labels and entry fields for the URL and the number of pages, and a button to start the scraping process.

## Acknowledgements

- [requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pandas](https://pandas.pydata.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
