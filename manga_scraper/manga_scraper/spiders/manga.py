# -*- coding: utf-8 -*-
import scrapy
from manga_scraper.items import MangaChapterItem

BASE_URL = 'https://manga-fox.com/read-nisekoi-manga-online-for-free2/chapter-'
START_CHAPTER = 8
END_CHAPTER = 16

class MangaSpider(scrapy.Spider):
    name = 'manga'
    allowed_domains = ['manga-fox.com']
    start_urls = [BASE_URL + str(x) for x in range(START_CHAPTER, END_CHAPTER + 1)]

    def parse(self, response):
        manga_chapter = MangaChapterItem()

        manga_chapter['manga_title'] = response.xpath('//span[@itemprop="title"]/text()').extract()[-1]
        manga_chapter['chapter_number'] = int(response.xpath('//title/text()').extract_first().split('/')[-1].split(' ')[-1])

        image_src = response.xpath('//div[@id="list_chapter"]/div/img/@src')
        manga_chapter['image_urls'] = image_src.extract()

        yield manga_chapter
