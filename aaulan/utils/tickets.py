import requests
from django.conf import settings


def get_ticket(id):
    resp = requests.get(url='https://api.studentersamfundet.aau.dk/aaulan', params={
        'access_token': settings.TICKET_API_KEY,
        'ticketnumber': id
    })
    if resp.status_code != 200:
        raise ConnectionError('Ticket API returned nonsuccesful status code')
    return resp.json()


def is_valid_ticket(id):
    return get_ticket()['TicketExists']