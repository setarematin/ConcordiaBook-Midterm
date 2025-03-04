from concordia_book.models.textbook import TextBook
from django.views.generic import ListView


class TextbookListView(ListView):
    model = TextBook
    template_name = "textbooks/textbook_list.html"  # Template to use
    context_object_name = "textbooks"

    def get_queryset(self):
        course_code = self.kwargs.get("course_code")
        return TextBook.objects.filter(course_code=course_code, availability=True)
