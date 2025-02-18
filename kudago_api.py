from datetime import datetime
from requests import get
from json import loads

def fetch_events():
    current_DateTime = datetime.now()
    now = datetime.timestamp(current_DateTime)
    query = f"https://kudago.com/public-api/v1.4/events/?lang=&page_size=100&fields=publication_date,title,body_text,location,categories,age_restriction,price,site_url,tags&expand=publication_date,title,body_text,location,categories,age_restriction,price,site_url,tags&order_by=&page_size=100&text_format=text&ids=&location=&actual_since={now}&actual_until=&is_free=&categories=&lon=&lat=&radius="
    response = get(query)
    page = loads(response.text)
    events = [page['results']]
    next_page = page['next']

    while True:
        response = get(next_page)
        page = loads(response.text)
        if response.status_code != 200 or page['next'] in [None, False, 'none', 'None']:
            break
        events += page['results']
        next_page = page['next']

    flat_events = []
    for sublist in events:
        if type(sublist) == list:
            flat_events += sublist
        else:
            flat_events.append(sublist)
    return flat_events

def event_to_text(event):
    text = f"Мероприятие: {event['title']}. Описание мероприятия: {event['body_text']}. Проводится в городе: {event['location']['name']}. Теговое описание мероприятия: {event['tags']}. Цена за вход: {event['price']}. Ссылка на мероприятие с сайта kudago: {event['site_url']}"
    return text

def get_text_events(events):
    return [event_to_text(event) for event in events]