# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem

class ProductAllSpider(scrapy.Spider):
    name = "productall"
    allowed_domains = ['ikea.com', 'ikea.cn']

    def start_requests(self):
      url = 'https://www.ikea.cn/cn/zh/catalog/allproducts'
      yield scrapy.Request(url=url, callback=self.parse_all)

    def parse_all(self, response):
      category_urls = response.css('div.productCategoryContainer a::attr(href)').extract()
      for category_url in category_urls:
        yield scrapy.Request(url='https://www.ikea.cn/{}'.format(category_url), callback=self.parse_category)
    
    def parse_category(self, response):
      product_urls = response.css('a.productLink::attr(href)').extract()
      for product_url in product_urls:
        yield scrapy.Request(url='https://www.ikea.cn/{}'.format(product_url), callback=self.parse_product)
    
    def parse_product(self, response):
      product = ProductItem()
      product['number'] = response.css('meta[name=partnumber]::attr(content)').extract_first()
      product['name'] = response.css('meta[name=product_name]::attr(content)').extract_first()
      image_url = response.css('img[id=productImg]::attr(src)').extract_first()
      product['image_urls'] = ['https://www.ikea.cn/{}'.format(image_url)]
      product['images'] = []
      yield product
      
