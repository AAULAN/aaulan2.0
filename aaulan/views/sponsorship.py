from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models.sponsorship import Sponsorship, SponsorshipSerializer


class SponsorshipViewSet(viewsets.ViewSet):
    def list(self, request, event_pk=None):
        queryset = Sponsorship.objects.filter(event=event_pk)
        serializer = SponsorshipSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, event_pk=None, pk=None):
        queryset = Sponsorship.objects.filter(event=event_pk)
        team = get_object_or_404(queryset, pk=pk)
        serializer = SponsorshipSerializer(team)
        return Response(serializer.data)
