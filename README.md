# Пульт охраны банка

Этот проект — веб-приложение на Django, которое позволяет взаимодействовать с удаленной базой данных PostgreSQL для мониторинга и управления пропусками.

## Требования

Перед запуском проекта убедитесь, что у вас установлены:
- Python 3.2 или более поздняя версия
- Pip (менеджер пакетов Python)

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL вашего репозитория>
   cd django-orm-watching-storage
   ```

2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Создайте файл `.env`:**
   Скопируйте и отредактируйте пример файла `.env`, чтобы указать нужные переменные окружения, а именно `SECRET_KEY,HOST,PASSWORD`.

## Запуск


1. **Запустите сервер:**
   ```bash
   python manage.py runserver 
   ```

2. **Откройте в браузере:**
   Перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), чтобы увидеть работающий сайт.
   Или же можете зайти по адресу: [localhost:8000](http://0.0.0.0:8000)
## Цель проекта

Код написан в образовательных целях

---