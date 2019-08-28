from django.urls import path
from .views import MemberCreateView, MemberListView, MemberUpdateView, member_delete_view

app_name = "member"

urlpatterns = [
    path('list/',MemberListView.as_view(),name='member-list'),
    path('create/',MemberCreateView.as_view(),name='member-create'),
    path('update/<slug:slug>/',MemberUpdateView.as_view(),name='member-update'),
    path('delete/<int:pk>/',member_delete_view,name='member-delete'),
]