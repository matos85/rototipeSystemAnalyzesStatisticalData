def compare_crypto_earnings(df):
    """
    Сравнивает средний доход между фрилансерами, принимающими криптовалюту и другими способами оплаты.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Payment_Method' (str): способ оплаты ('Crypto' или другие)
            - 'Earnings_USD' (float): доход в долларах

    Returns:
        str: Форматированная строка с результатами сравнения в формате:
            'Средний доход (Crypto): $X.XX
             Средний доход (другое): $Y.YY
             Разница: $Z.ZZ'
    """
    crypto = df[df['Payment_Method'] == 'Crypto']['Earnings_USD'].mean()
    non_crypto = df[df['Payment_Method'] != 'Crypto']['Earnings_USD'].mean()
    return f"\nСредний доход (Crypto): ${crypto:.2f}\nСредний доход (другое): ${non_crypto:.2f}\nРазница: ${crypto - non_crypto:.2f}"


def earnings_by_region(df):
    """
    Анализирует средний доход фрилансеров по регионам клиентов.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Client_Region' (str): регион клиента
            - 'Earnings_USD' (float): доход в долларах

    Returns:
        str: Форматированная строка с отсортированными по убыванию дохода результатами
             в формате 'Доход по регионам:\nРегион1 X.XX\nРегион2 Y.YY'
    """
    region_stats = df.groupby('Client_Region')['Earnings_USD'].mean().sort_values(ascending=False)
    return "\nДоход по регионам:\n" + region_stats.to_string()


def experts_under_100_projects(df):
    """
    Рассчитывает процент экспертов, выполнивших менее 100 проектов.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Experience_Level' (str): уровень опыта ('Expert' и др.)
            - 'Job_Completed' (int): количество выполненных проектов

    Returns:
        str: Строка в формате 'XX.XX% экспертов выполнили менее 100 проектов'
             Возвращает 0%, если нет экспертов в данных.
    """
    experts = df[df['Experience_Level'] == 'Expert']
    under_100 = experts[experts['Job_Completed'] < 100]
    percent = len(under_100) / len(experts) * 100 if len(experts) > 0 else 0
    return f"\n{percent:.2f}% экспертов выполнили менее 100 проектов"


def high_earners_rating(df):
    """
    Рассчитывает средний рейтинг фрилансеров с доходом выше $10,000.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Earnings_USD' (float): доход в долларах
            - 'Client_Rating' (float): рейтинг клиента (0.0-5.0)

    Returns:
        str: Строка в формате 'Средний рейтинг фрилансеров с доходом выше $10,000: X.XX'
    """
    high_earners = df[df['Earnings_USD'] > 10000]
    avg_rating = high_earners['Client_Rating'].mean()
    return f"\nСредний рейтинг фрилансеров с доходом выше $10,000: {avg_rating:.2f}"


def highest_avg_hourly_by_platform(df):
    """
    Находит платформу с наибольшей средней почасовой ставкой.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Platform' (str): название платформы
            - 'Hourly_Rate' (float): почасовая ставка в долларах

    Returns:
        str: Строка в формате 'Платформа с самой высокой средней почасовой ставкой: ИмяПлатформы ($X.XX/час)'
    """
    platform_rates = df.groupby('Platform')['Hourly_Rate'].mean().sort_values(ascending=False)
    top_platform = platform_rates.idxmax()
    top_rate = platform_rates.max()
    return f"\nПлатформа с самой высокой средней почасовой ставкой: {top_platform} (${top_rate:.2f}/час)"


def experience_vs_rehire(df):
    """
    Анализирует зависимость доли повторных заказов от уровня опыта фрилансера.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Experience_Level' (str): уровень опыта
            - 'Rehire_Rate' (float): доля повторных заказов (0.0-1.0)

    Returns:
        str: Форматированная строка с результатами в формате:
             'Средняя доля повторных заказов по уровням опыта:
              Уровень1 X.XX
              Уровень2 Y.YY'
    """
    experience_stats = df.groupby('Experience_Level')['Rehire_Rate'].mean().sort_values(ascending=False)
    return "\nСредняя доля повторных заказов по уровням опыта:\n" + experience_stats.to_string()


def marketing_spend_by_category(df):
    """
    Рассчитывает средние маркетинговые расходы по категориям проектов.

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Job_Category' (str): категория проекта
            - 'Marketing_Spend' (float): расходы на маркетинг в долларах

    Returns:
        str: Форматированная строка с результатами в формате:
             'Средние маркетинговые расходы по категориям:
              Категория1 X.XX
              Категория2 Y.YY'
    """
    marketing_stats = df.groupby('Job_Category')['Marketing_Spend'].mean().sort_values(ascending=False)
    return "\nСредние маркетинговые расходы по категориям:\n" + marketing_stats.to_string()


def project_type_earnings(df):
    """
    Анализирует средний доход по типам проектов (фиксированная ставка/почасовая).

    Args:
        df (pd.DataFrame): DataFrame с данными фрилансеров, должен содержать колонки:
            - 'Project_Type' (str): тип проекта ('Fixed' или 'Hourly')
            - 'Earnings_USD' (float): доход в долларах

    Returns:
        str: Форматированная строка с результатами в формате:
             'Средний доход по типу проекта:
              Тип1 X.XX
              Тип2 Y.YY'
    """
    earnings_stats = df.groupby('Project_Type')['Earnings_USD'].mean().sort_values(ascending=False)
    return "\nСредний доход по типу проекта:\n" + earnings_stats.to_string()