# Ициализирую переменные с помощью функции input(), в качестве аргумента функции.
username = input("Введите имя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки, например: \"актуальна/не актуальна\": ")
created_date = input("Введите дату заметки в формате: \"день-месяц-год\", например \"10-11-2024\": ")
issue_date = input("Введите дедлайн заметки в формате: \"день-месяц-год\", например \"10-11-2024\": ")

temp_created_date = (created_date[:5])
temp_issue_date = (issue_date[:5])

print(f"Привет, {username}!")
print(title)
print(content)
print(status)
print(temp_created_date)
print(temp_issue_date)