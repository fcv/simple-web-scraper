import scrapy
import re
from datetime import datetime
from scrapy import Spider, Request, Item
from scraper.items import ArticleItem, AuthorItem


class TechChunchSpider(Spider):

    name = "tech_crunch"

    start_urls = [
        'https://techcrunch.com/',
    ]

    def parse(self, response):
        for block in response.css('.river .river-block'):
            url = block.xpath('@data-permalink').extract_first()
            title = block.xpath('@data-sharetitle').extract_first()
            byline = block.css('.byline')
            # raw data formatted as '2016-10-07 07:03:28'
            raw_publish_date = byline.css('time::attr(datetime)').extract_first()
            try:
                publish_date = datetime.strptime(raw_publish_date, '%Y-%m-%d %H:%M:%S')
            except (TypeError, ValueError) as e:
                publish_date = None
            author_url = byline.css('a[rel=author]::attr(href)').extract_first()
            author_name = byline.css('a[rel=author]::text').extract_first()
            tags = block.css('.tags .tag > span::text').extract()
            content = block.css('p.excerpt::text').extract_first()
            yield ArticleItem(
                title = title,
                url = url,
                publish_date = publish_date,
                content = content,
                # TODO
                # authors = '',
                # tags = tags,
            )

        for author_url in set(response.css('.river .river-block a[rel=author]::attr(href)').extract()):
            author_url = response.urljoin(author_url)
            yield Request(author_url, callback=self.parse_author)


    def parse_author(self, response):
        name = response.css('.page-title > h1::text').extract_first()
        url = response.css('meta[property="og:url"]::attr(content)').extract_first()
        profile_div = response.css('div.profile')
        image_url = profile_div.css('.profile-img::attr(src)').extract_first()

        s = dict([(self.extract_social_media_name(anchor.xpath('@class').extract_first()), anchor.xpath('@href').extract_first())
                  for anchor in profile_div.css('.social-list li a[rel=external]')])
        return AuthorItem(
            name = name,
            profile_url = url,
            # TODO
            # profile_image_url = image_url,
            # social_medias = s
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

    # TODO
    def parse_article(self, response):

        url = response.css('link[rel=canonical]::attr(href)').extract_first()
        # extracts publish date from swiftype's information, it seems to be the most accurate value
        # it's formatted as as '2016-10-07 07:03:28'
        raw_publish_date = response.css('meta[class=swiftype][name=timestamp]::attr(content)').extract_first()
        title = response.css('head title::text').extract_first()

        return None




