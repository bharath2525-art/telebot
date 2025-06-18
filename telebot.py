import requests
import time
import os

# Токен бота
TOKEN = 

# ID группы, которую нужно отслеживать
GROUP_ID = {{id_tegram}}

# ID последнего обновления
last_update_id = 0
run = 0
new_users = []
usernames = []

# Бесконечный цикл для отслеживания новых пользователей
while True:
    # Отправляем запрос к Telegram Bot API для получения новых обновлений
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_update_id + 1}')

    # Парсим ответ в формате JSON
    updates = response.json()['result']
    # Если есть новые обновления
    if updates:
        # Перебираем все обновления
        for update in updates:
            # Получаем ID обновления
            try:
                for item in updates:
                    message = item.get('message')
                    if message and 'new_chat_members' in message:
                        new_users = message.get('new_chat_member')
                        if new_users:
                            username = new_users.get('username')
                            if username:
                                usernames.append(username)
            except:
                pass
            update_id = update['update_id']
            # Если обновление относится к группе, которую мы отслеживаем
            if 'message' in update and 'new_chat_member' in update['message'] and update['message']['chat']['id'] == GROUP_ID:
                # Получаем информацию о новом пользователе
                new_user = update['message']['new_chat_member']

                # Выводим информацию о новом пользователе в консоль
                print(f'New user: {new_user["first_name"]} {new_user["last_name"]} (@{new_user["username"]})')

            # Сохраняем ID последнего обновления
            last_update_id = update_id
    run = run + 1

    print("\nНомер запроса: ", run)
    print("\nНомер обновления: ", last_update_id)
    print("________________________")
    print(usernames)
    # Делаем паузу на 1 час перед следующим запросом
    time.sleep(3600)
    # Очищаем вывод консоли
    os.system('CLS')
