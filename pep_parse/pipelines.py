import csv
from pathlib import Path
from typing import Dict

from pep_parse.settings import BASE_DIR, FILE_NAME


class PepParsePipeline:
    def __init__(self) -> None:
        self._status_counts: Dict[str, int] = {}
        self._total_peps: int = 0

    def open_spider(self, spider) -> None:
        pass

    def process_item(self, item: Dict[str, str], spider) -> Dict[str, int]:
        status: str = item['status']
        if status in self._status_counts:
            self._status_counts[status] += 1
        else:
            self._status_counts[status] = 1
        self._total_peps += 1
        return item

    def close_spider(self, spider) -> None:
        result_dir: Path = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        file_path: Path = result_dir / FILE_NAME

        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames: list[str] = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for status, count in self._status_counts.items():
                writer.writerow({'Статус': status, 'Количество': count})

            writer.writerow(
                {'Статус': 'Total', 'Количество': self._total_peps}
            )
