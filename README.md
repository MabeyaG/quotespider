# 🕷️ Legit Scrapy Project — Quotes Spider

A Scrapy-based web crawler to scrape quotes from [quotes.toscrape.com](https://quotes.toscrape.com/).

## 🎯 Objective

- Crawl quote text, author, tags, and author link.
- Handle multiple pages (pagination).
- Export data as JSON or CSV.
- Mimic a real browser to avoid getting blocked.

## 🚀 Usage

1. Install Scrapy:
   ```
   pip install scrapy
   ```
2. Run the spider:
   ```
   scrapy crawl quotes
   ```

Output files:  
- `quotes.json`  
- `quotes.csv`  

## 📂 Project Structure

```
quotes/
├── scrapy.cfg
├── quotes/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── quotes_spider.py
└── README.md
```

## 🌍 Target Site
Scrapes quotes from:

[https://quotes.toscrape.com/](https://quotes.toscrape.com/)

*You can change the domain if needed.*
