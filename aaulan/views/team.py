from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models.team import TeamSerializer, Team
from ..models.team_association import TeamAssociation, TeamAssociationSerializer


class TeamViewSet(viewsets.ViewSet):
    def list(self, request, event_pk=None):
        queryset = Team.objects.filter(event=event_pk)
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, event_pk=None, pk=None):
        queryset = Team.objects.filter(event=event_pk)
        team = get_object_or_404(queryset, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def members(self, request, event_pk=None,  pk=None):
        team = get_object_or_404(Team.objects.filter(event=event_pk), pk=pk)
        members = TeamAssociation.objects.filter(team=team)
        serializer = TeamAssociationSerializer(members, many=True)
        return Response(serializer.data)
