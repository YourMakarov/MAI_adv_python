from database import create_db, db_insert
from kudago_api import fetch_events, get_text_events
from embedding_utils import get_embeddings
from pinecone_utils import initialize_pinecone, upsert_vectors

# Инициализация базы данных
create_db()
print('sqlite_created')

# Получение событий с KudaGo
events = fetch_events()
text_events = get_text_events(events)
print('kudago_parsed')

# Генерация эмбеддингов
embeddings = get_embeddings(text_events)
data_vector_bd = [{'id': str(id), 'values': embedding.tolist()} for id, embedding in zip(range(len(text_events)), embeddings)]
data_sqlite = [(str(id), text) for id, text in zip(range(len(text_events)), text_events)]
print('embeggings_created')

# Инициализация Pinecone и загрузка данных
index = initialize_pinecone()
upsert_vectors(index, data_vector_bd)
db_insert(data_sqlite)
print('data_inserted')

# Запуск бота
from bot import bot
bot.polling(none_stop=True, interval=0)
