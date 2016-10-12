release: python manage.py migrate
web: gunicorn simple_web_scraper.wsgi --log-file -
worker: scrapy crawl tech_crunch
