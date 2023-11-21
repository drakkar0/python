from telethon.sync import TelegramClient, events
import time
import re
from pathlib import Path
import sqlite3


DB_NAME = "Telegram/listener.db"

with sqlite3.connect(DB_NAME) as db:
    sql_request = """CREATE TABLE IF NOT EXISTS message_from_tg (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    chat_id INTEGER,
    chat_name TEXT,
    user_name TEXT,
    user_phone TEXT,
    message TEXT);
    """
    db.execute(sql_request)

def add_row_to_sql(values_tuple):
    try:
        with sqlite3.connect(DB_NAME) as db:
            sql_request = "INSERT INTO message_from_tg (user_id, chat_id, chat_name, user_name,user_phone, message) VALUES(?,?,?,?,?,?)"
            db.execute(sql_request, values_tuple)
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")


session = Path

# ищем номер заявки для отправки его в инвеб
def find_the_number(text):
    match = re.search(r'#(\d+)', text)
    request_number = match.group(1)
    return request_number


api_id = 29305848
api_hash = '649204b0999cf6dd7c29309184c48222'


# client = TelegramClient('session_name', api_id, api_hash)
# client.start()

# #print all chats name
# for dialog in client.iter_dialogs():
#     print(dialog.name, 'has ID', dialog.id, dialog.username)
key_word = ['сайт', 'доробити сайт', 'розробити сайт', 'opencart',
            'wordpress', 'редизайн', 'існуючого сайту', 'Номер заявки', 'редизайн', 'чат-бот',
            'сделать бот', 'кто делает боты', 'Вордперес']

stop_words = ['можемо зробити', 'звертайтеся', 'ми робимо', 'Готові реалізувати', 'я могу сделать', 'сделаю', 'сделаем',
              'займаємося', 'підпішіть', 'підпишить', 'підпишіть']

message_to_client = """
Вітаю, мене звати Дмитро.  👋
Я більше 15 років займаюсь розробкою сайтів. Можете розповісти докладніше про ваш проект?🙏

"""


client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    
    if event.is_group:
        incoming_text = event.raw_text.lower()
        chat_name = await event.get_chat()
        sender = await event.get_sender() # получаем имя юзера
         
        if any(stop_word in incoming_text for stop_word in stop_words):
            return

        for key in key_word:
            if 'Номер заявки'.lower() in incoming_text:
                time.sleep(2)
                data_tobd = (event.message.sender_id,
                    event.chat_id,
                    chat_name.title if chat_name.title else "None" ,
                    sender.username if sender.username else "None" ,
                    sender.phone if sender.phone else "None" ,
                    incoming_text)
                add_row_to_sql(data_tobd)
                await client.send_message(event.message.sender_id, 'Привет. #' + find_the_number(incoming_text))
                break
            elif key.lower() in incoming_text:
                data_tobd = (event.message.sender_id,
                    event.chat_id,
                    chat_name.title if chat_name.title else "None" ,
                    sender.username if sender.username else "None" ,
                    sender.phone if sender.phone else "None" ,
                    incoming_text)
                add_row_to_sql(data_tobd)
                
                time.sleep(3)
                
                # await client.send_message(event.chat_id, message_to_client) #відправка у чат
                await client.send_message(event.message.sender_id, message_to_client)
                break


client.start()
client.run_until_disconnected()
