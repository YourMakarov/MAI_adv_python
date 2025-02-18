import telebot
from g4f.client import Client
from config import BOT_TOKEN
from database import db_find_by_ids
from embedding_utils import embed_bert_cls, model_embedder, tokenizer_embedder
from pinecone_utils import initialize_pinecone

bot = telebot.TeleBot(BOT_TOKEN)
client = Client()
index = initialize_pinecone()

def gpt_response(client, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        web_search=True
    )
    return response.choices[0].message.content

def find_matches_ids(text, index):
    vector = embed_bert_cls(text)
    res = index.query(
        namespace="example-namespace",
        vector=vector,
        top_k=5,
        include_values=False
    )
    return [match['id'] for match in res['matches']]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print('user_message: ' + message.text)
    ids = find_matches_ids(message.text, index)
    res = db_find_by_ids(ids)
    print('events: ' + '    '.join(res))
    prompt = message.text + ' Пользователь просит посоветовать подходящее ему мероприятие' + 'мы смогли найти вот такие мероприятия' + '    '.join(res) + 'выбери из этих мероприятий подходящие и ответь пользователю. Если наши подобранные варианты не подходят под запрос пользователя, найди нужные мероприятия в интернете'
    output = gpt_response(client, prompt)
    bot.send_message(message.from_user.id, output)
