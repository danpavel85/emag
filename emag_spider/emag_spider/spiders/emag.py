# -*- coding: utf-8 -*-
import scrapy
from ..items import EmagSpiderItem
from scrapy.loader import ItemLoader
import json


class EmagSpider(scrapy.Spider):
    name = 'emag'
    allowed_domains = ['emag.ro']
    start_urls = ['https://www.emag.ro/search-by-url?source_id=7&templates%5B%5D=full&is_eab49=false&sort%5Bpopularity%5D=desc&listing_display_id=2&page%5Blimit%5D=60&page%5Boffset%5D=60&fields%5Bitems%5D%5Bimage_gallery%5D%5Bfashion%5D%5Blimit%5D=2&fields%5Bitems%5D%5Bimage%5D%5Bresized_images%5D=1&fields%5Bitems%5D%5Bresized_images%5D=200x200%2C350x350&fields%5Bitems%5D%5Bfamily%5D=1&fields%5Bitems%5D%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbuying_options%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbundles%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bgifts%5D=1&fields%5Bquick_filters%5D=1&search_id=d27c0b387b234a5b494d&search_fraze=&search_key=a4e5afc34d23c6d5fa89a21908d1ae6d&url=%2Ftelefoane-mobile%2Fc']


    def parse(self, response):
        json_resp = json.loads(response.body)
        items = json_resp.get('data').get('items')
        for x in items:
            loader = ItemLoader(item=EmagSpiderItem())
            loader.add_value('id', x.get('id'))
            loader.add_value('current_price', x.get('offer').get('price').get('current'))
            loader.add_value('initial_price', x.get('offer').get('price').get('initial'))
            try:
                loader.add_value('absolute_disc', x.get('offer').get('price').get('discount').get('absolute'))
            except:
                pass
            try:
                loader.add_value('percent_disc', x.get('offer').get('price').get('discount').get('percent'))
            except:
                pass
            loader.add_value('url', x.get('url').get('path'))
            loader.add_value('part_number', x.get('offer').get('part_number'))
            loader.add_value('name', x.get('name'))

            for url in self.start_urls:
                yield scrapy.Request(url=url, callback=self.parse)
            yield loader.load_item()

        json_res_text = json.loads(response.text)

        current_page  = 2

        total_pages = json_res_text.get('data').get('pagination').get('pages')[3].get('id')
        while current_page <= total_pages:
            current_page = current_page + 1
            new_url = 'https://www.emag.ro/search-by-url?source_id=7&templates%5B%5D=full&is_eab49=false&sort%5Bpopularity%5D=desc&listing_display_id=2&page%5Blimit%5D=60&page%5Boffset%5D=0&fields%5Bitems%5D%5Bimage_gallery%5D%5Bfashion%5D%5Blimit%5D=2&fields%5Bitems%5D%5Bimage%5D%5Bresized_images%5D=1&fields%5Bitems%5D%5Bresized_images%5D=200x200%2C350x350&fields%5Bitems%5D%5Bfamily%5D=1&fields%5Bitems%5D%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbuying_options%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bflags%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bbundles%5D=1&fields%5Bitems%5D%5Boffer%5D%5Bgifts%5D=1&fields%5Bquick_filters%5D=1&search_id=fa95ccb9887c594004a5&search_fraze=&search_key=98c63ad2f25cb2cd1ca30cf777532aa2&url=%2Ftelefoane-mobile%2Fp{}%2Fc'.format(current_page)
            yield scrapy.Request(url=new_url, callback=self.parse)
