BOT_NAME = "jobspider"

SPIDER_MODULES = ["jobspider.spiders"]
NEWSPIDER_MODULE = "jobspider.spiders"

ROBOTSTXT_OBEY = False

FEEDS = {
    'quotes.json': {'format': 'json', 'overwrite': True},
    'quotes.csv': {'format': 'csv', 'overwrite': True},
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

ALLOWED_DOMAINS = ["quotes.toscrape.com"]
