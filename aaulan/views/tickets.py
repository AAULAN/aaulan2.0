from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from ..models import Attendee
from ..utils import tickets

@login_required
def verify_ticket(request):
    if not 'ticket' in request.META:
        resp = JsonResponse({'status': 'error', 'info': 'missing ticket argument'})
        resp.status_code = 400
        return resp

    attendee = Attendee.objects.get(user=request.user)
    if attendee.ticket is None:
        return JsonResponse({'status': 'failure', 'info': 'you have already registered a ticket'})

    ticket = request.META['ticket']
    if not tickets.is_valid_ticket(ticket):
        return JsonResponse({'status': 'failure', 'info': 'invalid ticket'})

    attendee.ticket = request.META['ticket']

    return JsonResponse({'status': 'success'})