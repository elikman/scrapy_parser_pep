# Установка

1. Клонировать репозиторий:
```
https://github.com/elikman/scrapy_parser_pep.git
```
2. Перейти в каталог проекта:
```
cd scrapy_parser_pep
```
3. Cоздайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
4. Установить необходимые зависимости с помощью pip:
```
pip install -r requirements.txt
```

## Использование

Для запуска парсера PEP с помощью Scrapy выполните следующую команду:
```
scrapy crawl pep
```