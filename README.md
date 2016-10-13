# Simple Web Scraper

## About

Simple Web Scraper POC project. Aims to retrieve data from a Web Page and expose extracted data through a REST API.

## Development

Simple Web Scraper has been develop on Python3 using [Django](https://www.djangoproject.com/) and [Scrapy](https://scrapy.org/) among other libraries.

### Virtual Environment

In order to build system locally is highly recommended to use a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

In an Ubuntu system Python's virtual environment tool may be installed using  command:

    $ apt-get install virtualenv

After that a new virtual environment may be created executing:

    $ virtualenv ~/path/to/new_virtual_env

Then `new_virtual_env` may be activated by:

    $ . ~/path/to/new_virtual_env/bin/activate

Bash prefix would change prepending virtual environment's name indicating that virtual environment is activated. Example:

    $ (new_virtual_env) user@host:~$

In order to deactivate virtual environment one might execute command `deactivate`.

### Install Project's Dependencies

Project dependencies are declared in `requirements.txt` file and may be installed using [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) command. Remember installing them within virtual environment.

    $ (new_virtual_env) user@host:~/simple-web-scraper$ pip install -r requirements.txt

### Database

Project has been developed targeting PostgreSQL DBMS. Its default connection property values are defined in [simple_web_scraper/settings.py](simple_web_scraper/settings.py#L84) file and they target CI environment's database, see [.gitlab-ci.yml](.gitlab-ci.yml#L10) file.

There are two ways to overwrite those properties at Development environment:

1. Define connection URL using `DATABASE_URL` environment variable. Example:

    $ export DATABASE_URL='postgres://user:pwd@host:port/databasename'

2. Overwrite `simple_web_scraper.settings.DATABASES` values in untracked file `local_settings.py`. Example:

    $ cat ./simple_web_scraper/local_settings.py
    from simple_web_scraper.settings import *
    
    DATABASES['default']['HOST'] = 'localhost'
    DATABASES['default']['PORT'] = '5432'
    
    DEBUG = True

#### Database's Sctructure Creation

Database's Tables may be created executing:

    $ (new_virtual_env) user@host:~/simple-web-scraper$ python manage.py migrate

#### Note about PostgreSQL usage

In ubuntu environment, in order to install PostgreSQL database adapter [psycopg2](https://pypi.python.org/pypi/psycopg2) it is necessary first to install `libpq-dev` package in order to avoid error message like one below:

    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'

This could be achieved by executing:

    $ sudo apt-get install libpq-dev

### Web Spider

Web Spider is implemented using [scapy](https://github.com/scrapy/scrapy) library. Web spider crawling process may be triggered by executing `scrapy crawl <spider_name>` command. Example:

    user@host:~/simple-web-scraper$ scrapy crawl tech_crunch

### Web App

Web application maybe started by executing Django's `runserver` command. Example:

    $ (new_virtual_env) user@host:~/simple-web-scraper$ python manage.py runserver

### REST API

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

Article's endpoint supports a query parameter named `"q"`. When provided system will return Articles whose title or content contains such value. Example:

    $ curl -H 'Accept: application/json; indent=4' 'http://127.0.0.1:8000/api/rest/v1/articles?q=combo'
    [
        {
            "id": 338,
            "title": "Samsung’s combo desktop/speaker is a weird sort of art",
            "url": "https://techcrunch.com/2016/10/10/art-pc/",
            "publish_date": "2016-10-10T01:27:09Z",
            "content": "If I’m Samsung, I’m looking for the next big product to capture the public’s attention while my public relations wing is attempting to put out all a whole lot of proverbial fires (to go along with the literal variety). This isn’t that. In fact, Samsung just kind of let this one loose into the world without any real fanfare. And it’s got a name to match.\nThe… "
        }
    ]
