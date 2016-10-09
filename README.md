# Simple Web Scraper

## About

Simple Web Scraper POC project. Aims to retrieve data from a Web Page and expose extracted data through a REST API.

## Web Spider

Web Spider is implemented using [scapy](https://github.com/scrapy/scrapy) library. Web spider crawling process may be triggered by executing `scrapy crawl <spider_name>` under `./scraper` folder. Example:

    user@host:~/simple-web-scraper/scraper$ scrapy crawl tech_crunch

## REST API

Extracted data is accessible through REST API's endpoints.
 
Available endpoints are `/api/rest/v1/authors/` and `/api/rest/v1/articles/`. Example:

    $ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/rest/v1/authors
    [
        {
            "id": 1,
            "name": "Todd Gardner",
            "profile_url": "http://social.techcrunch.com/contributor/todd-gardner/"
        },
        {
            "id": 2,
            "name": "Matthew Hodgson",
            "profile_url": "http://social.techcrunch.com/contributor/matthew-hodgson/"
        }
    ]

## Note about PostgreSQL usage

In ubuntu environment, in order to install PostgreSQL database adapter [psycopg2](https://pypi.python.org/pypi/psycopg2) it is necessary first to install `libpq-dev` package in order to avoid error message like one below:

    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'
