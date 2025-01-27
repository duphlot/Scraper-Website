# Scraper-Website

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

Scraper-Website is a project designed to collect data from websites programmatically. This project provides flexible functionality to scrape information such as product details, news, or other content from online sources automatically.

## 🚀 Key Features
- **Web Crawling:** Automatically navigates through multiple web pages to fetch required information.
- **Data Processing:** Cleans and organizes data into usable formats.
- **Data Export:** Exports scraped data to formats like CSV, JSON, or stores them in databases.
- **Custom Configurations:** Supports customization of scraping rules to fit various types of websites.

## 🛠️ Technologies Used
- **Language:** Python
- **Libraries:**
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): Parsing HTML and XML.
  - [Requests](https://docs.python-requests.org/): Easy HTTP requests.
  - [Selenium](https://www.selenium.dev/): Browser automation.

## 📄 Installation and Usage

### 1. System Requirements
- Python >= 3.8
- pip (Python package manager)

### 2. Installation
- Clone the repository:
    ```bash
    git clone https://github.com/duphlot/Scraper-Website.git
    cd Scraper-Website
    ```

### 3. Usage
#### Configure the scraper
- Example configuration might look like this:
    ```yaml
    target_urls:
      - "https://example.com/page1"
      - "https://example.com/page2"
    output:
      format: "csv"
      path: "data.csv"
    headers:
      User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ```

### 4. Code Examples

#### Full Scraper Implementation
Below is a concise example extracted from the [Full_code.ipynb](https://github.com/duphlot/Scraper-Website/blob/main/Full_code.ipynb):
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of target URLs
urls = [
    "https://example.com/product-page-1",
    "https://example.com/product-page-2"
]

# Headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Function to scrape product details
def scrape_product(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_name = soup.find('h1', class_='product-title').text.strip()
        price = soup.find('span', class_='price').text.strip()
        return {
            'Product Name': product_name,
            'Price': price
        }
    else:
        print(f"Failed to retrieve {url}")
        return None

# Scrape all products
product_data = []
for url in urls:
    data = scrape_product(url)
    if data:
        product_data.append(data)

# Save data to a CSV
pd.DataFrame(product_data).to_csv('products.csv', index=False)
print("Scraping completed. Data saved to products.csv")
```

This code demonstrates scraping multiple product pages and saving the collected data into a CSV file.

#### Example 1: Simple Web Scraping with BeautifulSoup
```python
import requests
from bs4 import BeautifulSoup

# Send a GET request
response = requests.get("https://example.com")
response.raise_for_status()  # Raise an error for bad responses

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract data
titles = soup.find_all("h1")
for title in titles:
    print(title.text)
```

#### Example 2: Selenium Automation
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")

# Extract element content
elements = driver.find_elements(By.TAG_NAME, "h1")
for element in elements:
    print(element.text)

# Close the browser
driver.quit()
```

## 📚 Project Structure
```
Scraper-Website/
│
├── Data/               # Main script to run the scraper
├── Trash/              # Configuration file
├── fahasa/             # Code for crawl fahasa
├── lazada/             # Code for crawl lazada
├── tiki/               # Code for crawl tiki
├── Full_code.ipynb     # Complete all code
└── README.md           # Documentation file
```

## 🤝 Contribution
Contributions are welcome! If you encounter any issues or have new ideas, feel free to open a Pull Request or an Issue.