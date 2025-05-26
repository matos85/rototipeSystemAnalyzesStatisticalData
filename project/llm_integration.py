import os
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем переменные из .env файла
load_dotenv()

# Получаем ключ из переменной окружения
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY не найден. Убедитесь, что .env файл существует и переменная установлена.")

client = OpenAI(api_key=api_key)

def interpret_query_with_llm(query: str) -> str:
    """
    Использует LLM (GPT-4) для интерпретации пользовательского запроса
    и маршрутизации к соответствующей функции анализа данных о фрилансерах.

    Функция ожидает, что модель вернет название одной из следующих функций:
        - compare_crypto_earnings
        - earnings_by_region
        - experts_under_100_projects
        - high_earners_rating
        - highest_avg_hourly_by_platform
        - experience_vs_rehire
        - marketing_spend_by_category
        - project_type_earnings
    Если запрос не подходит ни под одну из категорий, возвращается 'unknown'.

    Args:
        query (str): Текст запроса пользователя на естественном языке.

    Returns:
        str: Название соответствующей функции или 'unknown' в случае нераспознавания.
             При возникновении ошибки возвращается строка с префиксом 'llm_error:' и сообщением об ошибке.
    """
    try:
        system_prompt = (
            "Ты ассистент, который помогает маршрутизировать запросы пользователей "
            "по анализу данных о фрилансерах. Ответь названием функции, которую нужно вызвать, "
            "выбрав одну из следующих: compare_crypto_earnings, earnings_by_region, "
            "experts_under_100_projects, high_earners_rating, highest_avg_hourly_by_platform, "
            "experience_vs_rehire, marketing_spend_by_category, project_type_earnings. "
            "Не пиши ничего лишнего. Только имя команды. "
            "Если запрос не подходит — верни 'unknown'."
        )

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        )

        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"llm_error: {str(e)}"
