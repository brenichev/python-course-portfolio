from django.urls import path

from author.views import AuthorDetailView
from author.views import AuthorListView

urlpatterns = [
    path("", AuthorListView.as_view(), name="authors"),
    path("<int:pk>/", AuthorDetailView.as_view(), name="author"),
]
