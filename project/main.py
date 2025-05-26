from query_router import route_query
import pandas as pd
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

# Загрузка данных
df = pd.read_csv('freelancer_earnings_bd.csv')

def main():
    print("\nСистема анализа доходов фрилансеров. Введите запрос или 'выход':")
    while True:
        query = input("\n> ").strip().lower()
        if query == 'выход':
            print("Выход из системы.")
            break
        response = route_query(query, df)
        print("\nОтвет:")
        print(response)

if __name__ == '__main__':
    main()
