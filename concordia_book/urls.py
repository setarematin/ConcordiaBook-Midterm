from django.urls import path
from .views import TextbookListView
urlpatterns = [
    path("<str:course_code>", TextbookListView.as_view(), name="textbook_list"),

]
