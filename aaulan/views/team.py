from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models.team import TeamSerializer, Team


class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
