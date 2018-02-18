# -*- coding: utf-8 -*-
import scrapy


class MangaSpider(scrapy.Spider):
    name = 'manga'
    allowed_domains = ['kissmanga.com']
    start_urls = ['http://kissmanga.com/']

    def parse(self, response):
        pass
