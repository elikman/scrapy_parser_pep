from typing import Dict, Generator, List

import scrapy
from scrapy.exceptions import DropItem
from scrapy.http import Response

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name: str = 'pep'
    start_urls: List[str] = [f'https://{ALLOWED_DOMAINS}/']

    def parse(
        self, response: Response
    ) -> Generator[scrapy.Request, None, None]:
        section = response.css('section#index-by-category')

        tbody = section.css('tbody')
        tr_all = tbody.css('tr')

        for tr in tr_all:
            pep_link = tr.css('a[href^="pep"]::attr(href)').extract_first()
            columns = tr.css('a::text').getall()
            if columns:
                number: str = columns[0].strip()
                name: str = columns[1].strip()
            else:
                raise DropItem('Ошибка данных')

            yield response.follow(
                pep_link,
                callback=self.parse_pep,
                meta={'number': number, 'name': name},
            )

    def parse_pep(self, response: Response) -> PepParseItem:
        status: str = response.css('abbr::text').get().strip()
        data: Dict[str, str] = {
            'number': response.meta['number'],
            'name': response.meta['name'],
            'status': status,
        }
        return PepParseItem(data)
