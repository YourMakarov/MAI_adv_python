# Курсовой проект по Python, “Ассистент по досугу”

Задача: реализовать чат-бота / веб-интерфейс для ассистента, который в диалоговой форме предлагает места для посещения или прогулки в зависимости от потребности пользователя. 
История задачи: достаточно часто люди сталкиваются с вопросом куда бы сходить развеяться и отдохнуть. Для этого они подписываются на многочисленные группы в телеграмме или в ВК, или спрашивают у друзей. Когда приходит время посоветовать место другу они называют первое что приходит в голову, называя либо не все, либо не учитывая предпочтения. Поэтому компания “Досуг и Ко” решила разработать централизованную систему проведения досуга и предложила вам реализовать прототип данной системы.

Этот проект позволяет парсить мероприятия с сайта KudaGo, создавать их текстовые описания, генерировать эмбеддинги с помощью модели RuBERT, сохранять данные в Pinecone и SQLite, а также предоставляет Telegram-бота для поиска подходящих мероприятий по запросу пользователя.

Выполнил студент группы М80-109СВ-24, Макаров Глеб Александрович

## Основные функции

- **Парсинг мероприятий**: Получение данных о мероприятиях с сайта KudaGo через API.
- **Генерация текстовых описаний**: Преобразование данных о мероприятиях в текстовый формат.
- **Эмбеддинги**: Генерация векторных представлений текстов с использованием модели RuBERT.
- **Хранение данных**: Сохранение эмбеддингов в Pinecone и текстовых данных в SQLite.
- **Telegram-бот**: Поиск подходящих мероприятий по запросу пользователя с использованием GPT-4 и Pinecone.

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/YourMakarov/MAI_adv_python/tree/main
   cd kudago-event-parser

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt

3. **Настройте конфигурацию: Откройте файл config.py и укажите свои API ключи для Pinecone и Telegram-бота**

   ```python
    API_KEY = 'your_pinecone_api_key'
    BOT_TOKEN = 'your_telegram_bot_token'

4. **Запустите проект:**

   ```bash
   python main.py
