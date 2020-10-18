Фреймворк написан с использованием Python 3.8
***
##### Основные файлы
```
* run.py        - Файл используется для запуска фреймворка
* create_db.py  - Используется для создания базы данных
```
***
##### Директория BASE содержит файлы самого фреймворка
``` 
* core.py       - Основная функция фреймворка  
* templator.py  - Обработчик шаблонов html 
* patterns.py   - Используемые паттерны
* settings.py   - Файл настроек используемых директорий
* logging.py    - Функционал для логирования событий
```
***
##### Директория DB содержит файлы базы данных
```
* create_db.sql     - Здесь необходимо указать SQL запросы для создания таблиц в новой базе данных
* database.sqlite   - Пустой файл базы данных в который будут добавляться данные
```
***
##### Директория SETUP содержит файлы в которых необходимо добавить нужный функционал для вашего сайта (проекта)
```
* urls.py       - Здесь необходимо добавить ссылки вашего сайта (по умолчанию фал содержит примеры)
* views.py      - В данном файле добавляются необходимы представления (по умолчанию фал содержит примеры)
* models.py     - Необходимо добавить необходимые модели (по умолчанию фал содержит примеры)
```
***
##### Директория TEMPLATES должна содержать файлы шаблонов html
```
Для удобства были созданы примеры шаблонов.
Директория INCLUDES не является обязательной, но как пример в ней создан файл главного меню
* main_menu_example - Пример главного меню
* base_example      - Пример базового шаблона с использованием подключенного файла меню
* page_example      - Пример страницы с использованием подключенного базового шаблона
```