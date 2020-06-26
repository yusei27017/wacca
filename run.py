from scrapy import cmdline

cmdline.execute('scrapy crawl mtg -o mtg.json'.split())