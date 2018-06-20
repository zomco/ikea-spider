# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    number = scrapy.Field()  # 货号
    name = scrapy.Field()  # 名称
    image_urls = scrapy.Field()  # 图片路径
    images = scrapy.Field()  # 图片路径
