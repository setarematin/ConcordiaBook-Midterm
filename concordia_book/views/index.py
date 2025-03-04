from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"

def redirect_to_textbook(request):
    course_code = request.GET.get('course_code', '').strip()
    if course_code:
        return redirect(f'/textbooks/{course_code}')
    return HttpResponse("Invalid course code", status=400)
