# ikea-spider
IKEA宜家产品信息爬虫，保存产品信息和产品封面图片（并不是全部图片），基于Scrapy开发

## 使用

### 爬取信息

产品信息保存到result.json，同时产品图片保存到images/

scrapy crawl product -o result.json -t json

### 处理信息（开发中）

将产品图片重命名为 `产品名_货号.jpg` ，并将产品图片背景设为透明

python3 test.py

## 开发

请参考Scrapy教程
 