from datetime import datetime
from pathlib import Path


BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

CSV = 'csv'

BASE_DIR = Path(__file__).resolve().parent.parent

ROBOTSTXT_OBEY = True

FILE_NAME = (
    f'status_summary_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.{CSV}'
)


FEEDS = {
    f'results/pep_%(time)s.{CSV}': {
        'format': CSV,
        'encoding': 'utf8',
        'fields': ['number', 'name', 'status'],
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
