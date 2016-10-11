release: python manage.py migrate
web: gunicorn simple_web_scraper.wsgi --log-file -
worker: cd scraper && scrapy crawl tech_crunch
