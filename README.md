# look_near_car

**Все зависимости находятся в requirements.txt, пример необходимых переменных окружений в .env_sample, список уникальных локаций представлен в csv файле "uszips.csv"**
**Для запуска проекта:**
- `git clone https://github.com/AliaksandrSihai/rishat_test_task.git`
-  Создать файл .env(скопировать из .env_sample пример необходимых переменных)
___
  - <br>**Разворачивание без Docker:**
    - `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
    - `python manage.py migrate && python manage.py crl && python manage.py cnr `
    - для создания супер пользователя перейти в users/management/commands/csu.py и изменить необходимые данные(email, password) и выполнить `python manage.py csu`
    - ` python manage.py runserver`
  
    <br>**Разворачивание с помощью Doker:**
    - Выполнить `docker-compose up --build`
___
## Стек:
- **Django**
- **Django REST framework**
- **PostgreSQL**
- **Celery**
- **Redis**
- **Docker**
___
## Документация:
- **Drf-yasg**
___
## О проекте:
- REST API сервиc для поиска ближайших машин к грузам.
<br>**Сервис реализует следующие функции:**
    - Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду)
    - Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль))
    - Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза)
    - Редактирование машины по ID (локация (определяется по введенному zip-коду))
    - Редактирование груза по ID (вес, описание)
    - Удаление груза по ID
    - Фильтр списка грузов (вес, мили ближайших машин до грузов)
    - Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную).
___


