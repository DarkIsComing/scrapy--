# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['https://maoyan.com/board/4']
    start_urls = ['https://maoyan.com/board/4/']

    def parse(self, response):
        films=response.css('.board-wrapper')
        for film in films:
            item=DoubanItem()
            index=film.css('.board-index::text').extract()
            img=film.css('a img::attr(data-src)').extract()
            title=film.css('.name a::attr(title)').extract()
            star=film.css('.star::text').extract()
            score1=film.css('.integer::text').extract()
            score2=film.css('.fraction::text').extract()
            score=score1+score2
            item['index']=index
            item['title']=title
            item['img']=img
            item['star']=star
            item['score']=score1
            return item