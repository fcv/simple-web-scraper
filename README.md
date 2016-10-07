# Simple Web Scraper

## About

Simple Web Scraper POC project. Aims to retrieve data from a Web Page and expose extracted data through a REST API.

## Note about PostgreSQL usage

In ubuntu environment, in order to install PostgreSQL database adapter [psycopg2](https://pypi.python.org/pypi/psycopg2) it is necessary first to install `libpq-dev` package in order to avoid error message like one below:

    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'
