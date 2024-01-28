from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.user.models import Vacancy
from django.core.paginator import Paginator
# Create your views here.

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()[:10]
        context = {
            'vacancies': vacancies
        }
        return render(request, 'home.html', context)
    


class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        paginator = Paginator(vacancies, 10)
        page_number = request.GET.get('page')
        vacancies = paginator.get_page(page_number)
        context = {
            'vacancies': vacancies
        }    
        return render(request, 'news_list.html', context)
    