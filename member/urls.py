from django.urls import path
from .views import MemberCreateView, MemberListView

app_name = "member"

urlpatterns = [
    path('create/',MemberCreateView.as_view(),name='member-create'),
    path('list/',MemberListView.as_view(),name='member-list'),
]