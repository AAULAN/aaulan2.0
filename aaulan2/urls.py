"""aaulan2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from aaulan import views
from aaulan.views.team import TeamViewSet
from aaulan.views.event import EventViewSet
from aaulan.views.tournament import TournamentViewSet
from aaulan.views.sponsorship import SponsorshipViewSet
from aaulan.views.sponsor import SponsorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth_views.LoginView.as_view()),
    path('logout', auth_views.LogoutView.as_view()),
    path('api/1/event', EventViewSet.as_view({'get': 'list'})),
    path('api/1/event/<int:pk>', EventViewSet.as_view({'get': 'retrieve'})),
    path('api/1/event/<int:event_pk>/team', TeamViewSet.as_view({'get': 'list'})),
    path('api/1/event/<int:event_pk>/team/<int:pk>', TeamViewSet.as_view({'get': 'retrieve'})),
    path('api/1/event/<int:event_pk>/team/<int:pk>/members', TeamViewSet.as_view({'get': 'members'})),
    path('api/1/event/<int:event_pk>/tournament', TournamentViewSet.as_view({'get': 'list'})),
    path('api/1/event/<int:event_pk>/tournament/<int:pk>', TournamentViewSet.as_view({'get': 'retrieve'})),
    path('api/1/event/<int:event_pk>/sponsorship', SponsorshipViewSet.as_view({'get': 'list'})),
    path('api/1/event/<int:event_pk>/sponsorship/<int:pk>', SponsorshipViewSet.as_view({'get': 'retrieve'})),
    path('api/1/sponsor', SponsorViewSet.as_view({'get': 'list'})),
    path('api/1/sponsor<int:pk>', SponsorViewSet.as_view({'get': 'retrieve'})),
]
