import requests
import time
from bs4 import BeautifulSoup


def scrape_news(category, url, color):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {category}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    headers = soup.find_all('h2')
    news_urls = soup.find_all('a', class_="i2PrHTUx")
    article_images = soup.find_all("img", class_=lambda x: x and "i3BQvntU i2_iGbjC" in x)

    links = [link['href'] for link in news_urls]
    filtered_images = [
        img["data-src"] if img.has_attr("data-src") else img.get("src", "")
        for img in article_images
        if int(img.get("width", 0)) > 300 and int(img.get("height", 0)) > 150
    ]

    with open(f"website/categories/{category}.html", "w", encoding="utf-8") as file:
        if category == "swiat":
            category = "świat"
        file.write(f'''
                <!DOCTYPE html>
                <head>
                    <meta charset="UTF-8">
                    <title>Wiadomości - {category.capitalize()}</title>
                    <style>
                        body {{ font-family: "Rubik", sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }}
                        .header {{ padding: 10px; border-radius: 10px; text-align: center; background: {color}; color: white; font-size: 30px; margin-bottom: 20px; }}
                        .news-container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; }}
                        .article-box {{ 
                            width: 350px; 
                            border: 1px solid #ccc; 
                            background: white; 
                            border-radius: 10px; 
                            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); 
                            overflow: hidden;
                            padding: 10px;
                            text-align: center;
                        }}
                        .article-box img {{ width: 100%; height: auto; border-bottom: 1px solid #ddd; }}
                        .article-box a {{ display: block; font-size: 18px; color: black; text-decoration: none; padding: 10px; font-weight: bold; }}
                        .article-box a:hover {{ color: darkred; }}
                        .footer {{ background-color: black; color: lightgray; text-align: center; padding: 10px; font-size: 14px; margin-top: auto; }}
                    </style>
                </head>
                <body style="background-color:black;">
                    <div class="header"><h1>Wiadomości - {category.capitalize()}</h1></div>
                    <div class="news-container">
                ''')

        for x, header in enumerate(headers):
            if x < len(links) and x < len(filtered_images):
                if links[x].startswith("/s/"):
                    links[x] = "https://wiadomosci.wp.pl" + links[x]
                file.write(f'''
                            <div class="article-box">
                                <img src="{filtered_images[x]}" alt="Article Image" style="width: 308px; height: 180px; object-fit: cover;">
                                <a href="{links[x]}">{header.text}</a>
                            </div>
                            ''')
        file.write("</div>")
        file.write(f'''<div class="footer"> &copy; 2025 bartmangosc''')
        file.write("</div></body>")


categories = {
    "polska": ("https://wiadomosci.wp.pl/polska", "#ff3333"),
    "swiat": ("https://wiadomosci.wp.pl/swiat", "#3333ff"),
    "polityka": ("https://wiadomosci.wp.pl/polityka", "#a3a3c2"),
    "historia": ("https://wiadomosci.wp.pl/historia", "#ac7339"),
    "pogoda": ("https://wiadomosci.wp.pl/pogoda", "#33ccff")
}


while True:
    try:
        for category, (url, color) in categories.items():
          scrape_news(category, url, color)
        time.sleep(600)
    except Exception as e:
        print(f"Error in scraper: {e}")
