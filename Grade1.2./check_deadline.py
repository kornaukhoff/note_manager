from datetime import datetime

# Получаем текущую дату
current_date = datetime.now().date()
print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

while True:
    # Запрашиваем дату дедлайна
    issue_date_input = input("\nВведите дату дедлайна (в формате день-месяц-год): ").strip()

    try:
        # Преобразуем введённую дату в объект datetime
        issue_date = datetime.strptime(issue_date_input, '%d-%m-%Y').date()

        # Сравниваем текущую дату с дедлайном
        delta = (issue_date - current_date).days

        # Выводим результат
        if delta < 0:
            print(f"Внимание! Дедлайн истёк {abs(delta)} дней назад.")
        elif delta == 0:
            print("Сегодня последний день выполнения задачи!")
        else:
            print(f"До дедлайна осталось {delta} дней.")
        break  # Завершаем цикл после успешной проверки

    except ValueError:
        # Сообщение об ошибке формата даты
        print("""Ошибка: введённая дата некорректна. 
Пожалуйста, используйте формат день-месяц-год (например, 10-01-2025).""")