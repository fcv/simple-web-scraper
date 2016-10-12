release: python manage.py migrate
release: scrapy crawl tech_crunch
web: gunicorn simple_web_scraper.wsgi --log-file -

