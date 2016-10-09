# Simple Web Scraper

## About

Simple Web Scraper POC project. Aims to retrieve data from a Web Page and expose extracted data through a REST API.

## Web Spider

Web Spider is implemented using [scapy](https://github.com/scrapy/scrapy) library. Web spider crawling process may be triggered by executing `scrapy crawl <spider_name>` under `./scraper` folder. Example:

    user@host:~/simple-web-scraper/scraper$ scrapy crawl tech_crunch

## Note about PostgreSQL usage

In ubuntu environment, in order to install PostgreSQL database adapter [psycopg2](https://pypi.python.org/pypi/psycopg2) it is necessary first to install `libpq-dev` package in order to avoid error message like one below:

    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'
