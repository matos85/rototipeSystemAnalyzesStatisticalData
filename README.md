# Freelancer Earnings Analysis CLI

**CLI-приложение для анализа доходов фрилансеров** с обработкой запросов на естественном языке через GPT-4

## Возможности

- Анализ доходов по 8+ параметрам:
  - Сравнение способов оплаты (криптовалюта vs другие)
  - Распределение по регионам
  - Статистика по экспертам
  - Рейтинги топ-фрилансеров
- Гибкая обработка запросов:
  - **GPT-4** для сложных формулировок
  - **Rule-based** fallback для базовых запросов
- Локальная обработка данных (без загрузки в OpenAI)

##  Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/freelancer-analysis-cli.git
cd freelancer-analysis-cli
```
2. Установите зависимости:

```bash
pip install -r requirements.txt
```
3. Создайте файл .env с API-ключом OpenAI d папке project:

```bash
OPENAI_API_KEY=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
#можете использовать ключ . Он будет удален через некотрое время сразу как только пойму что обратную связь не стоит ждать или я ее получил соответственно
```

Использование
Запуск системы осуществляется из папки project:

```bash
python main.py
```


## Примеры запросов:
- Какой доход у фрилансеров принимающих криптовалюту?
- Покажи статистику по регионам
- Какие платформы имеют самые высокие ставки?
-> выход
