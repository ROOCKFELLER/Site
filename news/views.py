from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успешно')
            return redirect('add_news')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_news')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

class HomeNews(ListView):
    model = News
    template_name = 'news/home_news.html'
    context_object_name = 'news'
    #extra_context = {'title': 'Главная',}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

#def index(request):
    #news = News.objects.order_by('-created_ap')
    #context = {
        #'news': news, 
        #'title': 'Список новостей',}
    #return render(request, template_name = 'news/index.html', context = context)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk = self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published=True)

#def get_category(request, category_id):
    #news = News.objects.filter(category_id=category_id)
    #category = Category.objects.get(pk=category_id)
    #return render (request, 'news/category.html', {'news': news,'category': category})
    
class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    #pk_url_kwarg = 'news_id'
    #template_name = 'news/news_detail.html'

#def view_news(request, news_id):
    #news_item = News.objects.get(pk = news_id)
    #return render( request, 'news/view_news.html', {'news_item': news_item})

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url = reverse_lazy('home')

#def add_news(request):
    #if request.method == 'POST':
        #form = NewsForm(request.POST)
        #if form.is_valid():
            #news = form.save()
            #return redirect(news)
    #else:
        #form = NewsForm()
    #return render(request, 'news/add_news.html', {'form': form})