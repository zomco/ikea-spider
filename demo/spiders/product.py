# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem

class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ['ikea.com', 'ikea.cn']

    def start_requests(self):
      az_urls = ['https://www.ikea.cn/cn/zh/catalog/productsaz/{}/'.format(i) for i in range(25)]
      for az_url in az_urls:
          yield scrapy.Request(url=az_url, callback=self.parse_az)

    def parse_az(self, response):
      series_urls = response.css('li.productsAzLink a::attr(href)').extract()
      for series_url in series_urls:
        yield scrapy.Request(url='https://www.ikea.cn/{}'.format(series_url), callback=self.parse_series)
    
    def parse_series(self, response):
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
      
