from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

from . import forms

# Create your views here.

def news(request):
    news_list = models.News.objects.all().order_by('-date')[:6]
    paginator = Paginator(news_list, 6)

    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news_base/news.html', {'news_list': news_list})



def new_detail(request, pk):
    new = get_object_or_404(models.News, pk=id)
    etx = {
        "title": models.News.title,
        'date': models.News.create_time,
        'image': models.News.image,
        'body': models.News.body
    }
    return render(request, 'news_base/news.html', etx)





def events(request):
    """
    交易记录列表

    """
    events_list = models.Events.objects.all().order_by('-create_time')[:9]
    papginator = Paginator(events_list, 9)
    page = request.GET.get('page')

    try:
        events = papginator.page(page)
    except PageNotAnInteger:
        events = papginator.page(1)
    except EmptyPage:
        events = papginator.page(papginator.num_pages)

    return render(request, 'news_base/events.html', {'events_list': events_list})

def event_detail(request, pk):
    """交易记录详情"""
    event = get_object_or_404(models.Events, pk=id)
    etx = {
        'title': models.Events.title,
        'image': models.Events.image
    }
    return render(request, 'news_base/events.html', etx)





def imformation(request):
    imformation_form = forms.ImformationForm()

    if request.method == "POST":
        imformation_form = forms.ImformationForm(request.POST)
        if imformation_form.is_valid():
            b = models.Imformation()
            b.name = imformation_form.cleaned_data['name']
            b.sub = imformation_form.cleaned_data['sub']
            b.tel = imformation_form.cleaned_data['tel']
            b.save()

        else:
            message = '请检查填写内容'
        return render(request, 'news_base/imformation.html', locals())
    return render(request, 'news_base/imformation.html', locals())



def about(request):
    about_list = models.About.objects.all().order_by('-pk')[:1]

    papginator = Paginator(about_list, 1)
    page = request.GET.get('page')

    try:
        about = papginator.page(page)
    except PageNotAnInteger:
        about = papginator.page(1)
    except EmptyPage:
        about = papginator.page(papginator.num_pages)

    return render(request, 'news_base/about.html', {'about_list': about_list})

def index(request):
    return render(request, 'news_base/index.html')


def cooperation(request):

    cooperation = models.Cooperation.objects.all().order_by('-pk')[:1]

    papginator = Paginator(cooperation, 1)

    page = request.GET.get('page')

    try:
        about = papginator.page(page)
    except PageNotAnInteger:
        about = papginator.page(1)
    except EmptyPage:
        about = papginator.page(papginator.num_pages)

    return render(request, 'news_base/index.html', {'cooperation': cooperation})


def services(request):
    services_list = models.Services.objects.all()[:6]
    return render(request, 'news_base/services.html', {'services': services_list})