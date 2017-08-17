# -*- coding: utf-8 -*-
import scrapy
from pm25.items import  *

class Pm25Spider(scrapy.Spider):
    name = "pm25"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuotesbotItem()
            item["name"]=quote.css("span.text::text").extract_first()
            yield item
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def parsecity(self, response):
        for quote in response.css("tr.citytr"):
            item = QuotesbotItem()
            item["name"] = quote.css("a::").extract_first()
            yield item
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

