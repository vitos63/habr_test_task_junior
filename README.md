1. Клонирование репозитория

   ```git clone https://github.com/vitos63/habr_test_task_junior.git```

2. Создание виртуального окружения

   ```python -m venv venv```

3. Активация виртуального окружения

   ```venv/Scripts/activate```

4. Установка зависимостей

   ```pip install -r requirements.txt```

5. Переход в директорию с файлом manage.py

   ```cd animal```
   
6. Запуск проекта

   ```python manage.py runserver```

Пример работы API:
1. GET-запрос на URL /tests
![image](https://github.com/user-attachments/assets/bcef554f-9017-447b-bdc6-261c3fbd7e0c)

2. GET-запрос на URL /tests?=species=<вид животного>
![image](https://github.com/user-attachments/assets/8b6e9743-7a58-46bc-ac69-6fc2908370e8)

3. POST-запрос на URL /tests
![image](https://github.com/user-attachments/assets/5d491519-9fef-431a-8829-3f8e28605278)

4. GET-запрос на URL /statistics
![image](https://github.com/user-attachments/assets/93f0c827-c04c-42c5-9a78-f173ae90e7cf)

