# News Scraper

## Project Overview
This project is a **news web scraper** that extracts news articles from **wiadomosci.wp.pl** and organizes them into five categories. The scraped news articles are displayed on a simple web interface with categorized sections.

## Features
- Scrapes news articles from **wiadomosci.wp.pl**.
- Categorizes news into **Polska, Świat, Polityka, Historia, Pogoda**.
- Displays news with **images and titles**.
- Provides navigation through categorized buttons.
- Runs a **local web server** to serve the website.

## Directory Structure
```
news-scraper/
├── news-scraper.py          # News scraping script
├── server.py                # Local server script
│
└── website/
    ├── index.html           # Homepage with category buttons
    ├── categories/          # Folder containing news categories
    │   ├── historia.html
    │   ├── pogoda.html
    │   ├── polityka.html
    │   ├── polska.html
    │   └── swiat.html
```

## Installation & Usage
### 1. Install Dependencies
Make sure you have **Python 3** installed along with the required dependencies:
```sh
pip install requests beautifulsoup4
```

### 2. Run the Scraper
Execute the scraping script to fetch the latest news:
```sh
python news-scraper.py
```
This will generate **HTML files** inside the `website/categories/` folder.

### 3. Start the Server
Run the following command to start the local server:
```sh
python server.py
```
This will host the website on **http://localhost:9000/**.

### 4. Open in Browser
Once the server is running, open your web browser and navigate to:
```
http://localhost:9000/
```

## License
This project is open-source and can be modified or distributed under the MIT License.
