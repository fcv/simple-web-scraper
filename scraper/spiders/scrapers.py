import scrapy
import re
from datetime import datetime
from scrapy import Spider, Request, Item
from scraper.items import ArticleItem, AuthorItem, OutletItem


class TechChunchSpider(Spider):

    name = "tech_crunch"

    start_urls = [
        'https://techcrunch.com/',
    ]

    def parse(self, response):

        name = response.css('meta[property="og:site_name"]::attr(content)').extract_first()
        description = response.css('meta[property="og:description"]::attr(content)').extract_first()
        logo_url = response.css('.logo-link img::attr(src)').extract_first()

        yield OutletItem(
            name = name,
            description = description,
            logo_url = logo_url,
            url = 'https://techcrunch.com/',
        )

        for block in response.css('.river .river-block'):
            url = block.xpath('@data-permalink').extract_first()
            title = block.xpath('@data-sharetitle').extract_first()
            short_content = content = block.css('p.excerpt::text').extract_first()
            if url is not None:
                yield Request(url, callback=self.parse_article, meta = {
                    'url': url,
                    'title': title,
                    'short_content': short_content,
                })

        for author_url in set(response.css('.river .river-block a[rel=author]::attr(href)').extract()):
            author_url = response.urljoin(author_url)
            yield Request(author_url, callback=self.parse_author)


    def parse_author(self, response):

        # note, some links to author doesn't look like an author profile page
        # when it does not skip it
        # ex: https://techcrunch.com/author/neal-hansch/
        if len(response.css('div.profile')) == 0:
            return None

        name = response.css('.page-title > h1::text').extract_first()
        url = response.css('meta[property="og:url"]::attr(content)').extract_first()
        profile_div = response.css('div.profile')
        image_url = profile_div.css('.profile-img::attr(src)').extract_first()
        social_medias = dict([(self.extract_social_media_name(anchor.xpath('@class').extract_first()), anchor.xpath('@href').extract_first())
                  for anchor in profile_div.css('.social-list li a[rel=external]')])
        return AuthorItem(
            name = name,
            profile_url = url,
            profile_image_url = image_url,
            social_medias = social_medias
        )

    def extract_social_media_name(self, expression):
        """
        Extracts social media name out of classname attr.
        Examples:
         - "spricon nosprite icon-twitter" returns "twitter"
         - "spricon nosprite icon-linkedin" returns "linkedin"
         - "spricon nosprite icon-youtube" return "youtube"
        :param expression: classname expression
        :return: social media name embedded into `icon-*` classname
        """

        social_media_regex = re.compile(r".+\bicon-(?P<social_media>.+)\b")
        match = social_media_regex.match(expression);
        if match is None:
            return 'Unknown (%s)' % expression
        return match.group('social_media')

    def parse_article(self, response):

        title = response.meta['title']
        short_content = response.meta['short_content']
        url = response.css('link[rel=canonical]::attr(href)').extract_first()

        # extracts publish date from swiftype's information, it seems to be the most accurate value
        # it's formatted as as '2016-10-07 07:03:28'
        raw_publish_date = response.css('meta[class=swiftype][name=timestamp]::attr(content)').extract_first()
        try:
            publish_date = datetime.strptime(raw_publish_date, '%Y-%m-%d %H:%M:%S')
        except (TypeError, ValueError) as e:
            publish_date = None

        title = response.css('head title::text').extract_first()
        tags = [tag.strip() for tag in response.css('.l-sidebar .accordion li[id$="-tag"] a::text').extract()]

        author_urls = response.css('.article-header a[rel=author]::attr(href)').extract()
        author_ids = [self.extract_author_id(url) for url in author_urls]

        return ArticleItem(
            title=title,
            url=url,
            publish_date=publish_date,
            content=short_content,
            tags=tags,
            author_profile_ids=author_ids,
        )


    def extract_author_id(self, url):
        """
        Extracts Author's id from its profile address URL.
        Example:
         - "/author/jonathan-shieber/" returns "jonathan-shieber"

        :param url: author profile's url
        :return: author's id
        """
        regex = re.compile('.*/author/(?P<authorid>[^/]+)/?$')
        match = regex.match(url)
        if match is None:
            author_id = url
        else:
            author_id = match.group('authorid')
        return author_id


