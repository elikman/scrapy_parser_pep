import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from pep_parse.settings import RESULTS_DIR
from pep_parse.settings import BASE_DIR, FILE_NAME


class PepParsePipeline:
    def open_spider(self, spider) -> None:
        self.status_counts = defaultdict(int)
        self.result_dir = BASE_DIR / RESULTS_DIR
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item: Dict[str, str], spider) -> Dict[str, int]:
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider) -> None:
        file_path: Path = self.result_dir / FILE_NAME
        
        rows: List[Dict[str, str]] = [
            {'Статус': status, 'Количество': count}
            for status, count in self.status_counts.items()
        ]
        rows.append({
            'Статус': 'Total',
            'Количество': sum(self.status_counts.values())
        })

        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames: List[str] = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
