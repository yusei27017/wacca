# -*- coding: utf-8 -*-
import scrapy
from ..items import MtgItem





class MtgSpider(scrapy.Spider):
    name = 'mtg'
    allowed_domains = ['www.hareruyamtg.com']
    # start_urls = ['https://www.hareruyamtg.com/ja/products/search?tags=657&saleFlg=1']
    # offset = 1
    # count = 0

    def start_requests(self):
        for offset in range(1,10):
            url = 'https://www.hareruyamtg.com/ja/products/search?tags=656&saleFlg=1&page={}'.format(offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )



    def parse(self, response):
        item = MtgItem()
        dd_list = response.xpath('//*[@id="category_item"]/div[3]/ul/li/div')
        for dd in dd_list[0::2]:
            item['name'] = dd.xpath('./a/text()').get().strip()
            item['price'] = dd.xpath('./div/p[1]/text()').get().strip()
            item['stock'] = dd.xpath('./div/p[2]/text()').get().strip()

            yield item


        # self.offset += 1
        # if self.offset <=5:
        #     url = 'https://www.hareruyamtg.com/ja/products/search?tags=657&saleFlg=1&page={}'.format(self.offset)
        #
        #     yield scrapy.Request(
        #         url=url,
        #         callback=self.parse
        #     )



# https://www.hareruyamtg.com/ja/products/search?tags=657&saleFlg={}
