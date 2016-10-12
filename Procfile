release: python manage.py migrate
worker: scrapy crawl tech_crunch
web: gunicorn simple_web_scraper.wsgi --log-file -

