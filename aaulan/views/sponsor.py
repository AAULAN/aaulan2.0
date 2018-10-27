from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models.sponsor import Sponsor, SponsorSerializer


class SponsorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Sponsor.objects.all()
        serializer = SponsorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sponsor.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        serializer = SponsorSerializer(team)
        return Response(serializer.data)
