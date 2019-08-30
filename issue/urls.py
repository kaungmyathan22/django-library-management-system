from django.urls import path
from .views import IssuedBookListView, IssuedBookCreateView, issue_update_view, issue_delete_view, recieve_issue_book_view

app_name = "issue"

urlpatterns = [
    path('list/', IssuedBookListView.as_view(), name="issue-list"),
    path('create/', IssuedBookCreateView.as_view(), name="issue-create"),
    path('update/<int:pk>/', issue_update_view, name="issue-update"),
    path('delete/<int:pk>/', issue_delete_view, name="issue-delete"),
    path('return/<int:pk>/', recieve_issue_book_view, name="issue-return"),
]
