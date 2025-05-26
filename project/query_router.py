from analysis import (
    compare_crypto_earnings,
    earnings_by_region,
    experts_under_100_projects,
    high_earners_rating,
    highest_avg_hourly_by_platform,
    experience_vs_rehire,
    marketing_spend_by_category,
    project_type_earnings
)
from llm_integration import interpret_query_with_llm

# Словарь соответствия команд аналитическим функциям
COMMAND_FUNCTIONS = {
    "compare_crypto_earnings": compare_crypto_earnings,
    "earnings_by_region": earnings_by_region,
    "experts_under_100_projects": experts_under_100_projects,
    "high_earners_rating": high_earners_rating,
    "highest_avg_hourly_by_platform": highest_avg_hourly_by_platform,
    "experience_vs_rehire": experience_vs_rehire,
    "marketing_spend_by_category": marketing_spend_by_category,
    "project_type_earnings": project_type_earnings
}

def fallback_rule_based(query: str, df) -> str:
    """Обрабатывает запросы пользователя по правилам, когда LLM не распознал команду.

    Использует ключевые слова в запросе для выбора соответствующей аналитической функции.

    Args:
        query (str): Текстовый запрос пользователя.
        df (pd.DataFrame): DataFrame с данными фрилансеров.

    Returns:
        str: Результат выполнения аналитической функции или сообщение об ошибке.

    Примеры:
        >>> fallback_rule_based("доход по регионам", df)
        Вызовет earnings_by_region(df)
    """
    if "криптовалют" in query or "crypto" in query:
        return compare_crypto_earnings(df)
    elif "регион" in query or "region" in query:
        return earnings_by_region(df)
    elif "эксперт" in query and ("< 100" in query or "менее 100" in query):
        return experts_under_100_projects(df)
    elif "рейтинг" in query and "10000" in query:
        return high_earners_rating(df)
    elif "платформа" in query and "почасовая ставка" in query:
        return highest_avg_hourly_by_platform(df)
    elif "опыт" in query and "повторн" in query:
        return experience_vs_rehire(df)
    elif "маркетинг" in query or "расходы" in query:
        return marketing_spend_by_category(df)
    elif "тип проекта" in query or "fixed" in query or "hourly" in query:
        return project_type_earnings(df)
    else:
        return "Извините, я не смог распознать ваш запрос. Попробуйте переформулировать."

def route_query(query: str, df) -> str:
    """Маршрутизирует пользовательский запрос к соответствующей аналитической функции.

    Сначала пытается использовать LLM для распознавания команды, при неудаче
    переходит на rule-based подход.

    Args:
        query (str): Текстовый запрос пользователя.
        df (pd.DataFrame): DataFrame с данными фрилансеров.

    Returns:
        str: Результат выполнения аналитической функции или сообщение об ошибке.

    Примеры:
        >>> route_query("Какие платформы имеют самые высокие ставки?", df)
        Вызовет highest_avg_hourly_by_platform(df)

        >>> route_query("Непонятный запрос", df)
        Вернет сообщение об ошибке распознавания
    """
    command = interpret_query_with_llm(query)

    if command in COMMAND_FUNCTIONS:
        return COMMAND_FUNCTIONS[command](df)
    elif command.startswith("llm_error") or command == "unknown":
        return fallback_rule_based(query, df)
    else:
        return "Команда не распознана моделью. Попробуйте уточнить запрос."