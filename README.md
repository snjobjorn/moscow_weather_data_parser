# Moscow Weather Data Parser

Скрипт для автоматического сбора и сохранения архивных погодных данных по Москве с сайта [pogoda1.ru](https://pogoda1.ru/moscow/).

## 📌 Описание

Этот проект предназначен для парсинга архивных погодных данных по Москве за каждый день года. Скрипт автоматически:

- Проходит по всем датам в формате `dd-mm` (например, `01-01`, `02-01`, ..., `31-12`)
- Формирует соответствующие URL-адреса на сайте [pogoda1.ru](https://pogoda1.ru/moscow/)
- Загружает и парсит HTML-страницы
- Извлекает данные о погоде
- Сохраняет результаты в формате JSON в папке `result/` с указанием даты и времени сбора данных

## 🗂️ Структура проекта

```
moscow_weather_data_parser/
├── main.py
├── utils/
│   ├── get_page_content.py
│   ├── get_weather_data.py
│   ├── parse_dates.py
│   └── ...
├── result/
│   └── result_YYYYMMDD_HHMMSS.json
├── requirements.txt
└── README.md
```

## 🚀 Установка и запуск

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/snjobjorn/moscow_weather_data_parser.git
cd moscow_weather_data_parser
```

2. **Создайте виртуальное окружение и активируйте его:**

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate   # для Windows
```

3. **Установите зависимости:**

```bash
pip install -r requirements.txt
```

4. **Запустите скрипт:**

```bash
python main.py
```

После выполнения скрипта, результаты будут сохранены в папке `result/` в файле с именем `result_YYYYMMDD_HHMMSS.json`.

## 🛠️ Зависимости

- `requests`
- `beautifulsoup4`
(см. подробнее в requirements.txt)

Убедитесь, что все зависимости установлены перед запуском скрипта.
