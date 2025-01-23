username = "Имя пользователя: "
title = "Заголовок заметки: "
content = "Описание заметки: "
status = "Статус заметки, например: \"актуальна/не актуальна\": "
created_date = "Дата заметки в формате: \"день-месяц-год\", например \"10-11-2024\": "
issue_date = "Дедлайн заметки в формате: \"день-месяц-год\", например \"10-11-2024\": "

# Добавляю 2 переменныедля для хранения изменённых дат, присваиваю им соответствующее значение.
temp_created_date = (created_date[:5])
temp_issue_date = (issue_date[:5])

print(username)
print(title)
print(content)
print(status)
print(created_date)
print(issue_date)