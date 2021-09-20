from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
import io
from .models import *
from .forms import *
from accounts.models import User
# Create your views here.
def index(request):
    conf_list = Conference.objects.order_by('event_date').reverse()
    contents = {
        'current_conf' : Conference.getCurrentConference(),
        'conf_list' : conf_list,
    }
    print(contents)
    return render(request, 'home/index.html', contents)

def sitemap(request):
    return render(request, 'home/sitemap.html')

@login_required
def usersetting(request):
    if request.method == 'POST':
        form = UsersettingForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UsersettingForm(instance=request.user)
    contents = {
        'form': form
    }
    return render(request, 'home/usersetting.html', contents)

def conferencelist(request):
    conf_list = Conference.objects.order_by('event_date').reverse()
    contents = {
        'conf_list' : conf_list,
    }
    return render(request, 'home/conferencelist.html', contents)

def conferenceinfo(request, conf_id):
    conf = Conference.getConferenceById(conf_id)
    contents = {
        'conf' : conf,
    }
    return render(request, 'home/conferenceinfo.html', contents)

@login_required
def entry(request, conf_id):
    conf = Conference.getConferenceById(conf_id)
    contents = {
        'conf' : conf,
    }
    return render(request, 'home/entry.html', contents)

def getIsPresenter(request, conf_id):
    if not request.user.is_authenticated:
        return JsonResponse(data={
            'success' : False,
            'message' : "You are not authenticated."
        })
    conf = Conference.getConferenceById(conf_id)
    if conf is None:
        return JsonResponse(data={
            'success' : False,
            'message' : "Invalid Conference id"
        })
    pres = Presenter.objects.filter(user=request.user, conference=conf)
    contents = {
        'is_presenter' : len(pres) != 0
    }
    return JsonResponse(data={
        'success' : True,
        'data' : contents
    })

def setPresenter(request, conf_id, is_participate):
    if not request.user.is_authenticated:
        return JsonResponse(data={
            'success' : False,
            'message' : "You are not authenticated."
        })
    conf = Conference.getConferenceById(conf_id)
    if conf is None:
        return JsonResponse(data={
            'success' : False,
            'message' : "Invalid Conference id"
        })
    pres = Presenter.objects.filter(user=request.user, conference=conf)
    is_participate = is_participate == 1
    if len(pres) == 0 and is_participate:
        pres = [Presenter.objects.create(
            user=request.user,
            conference=conf
        )]
    elif len(pres) != 0 and not is_participate:
        pres.delete()
        pres = []
    return JsonResponse(data={
        'success' : True,
        'data' : {
            'is_presenter' : len(pres) != 0
        }
    })

@login_required
def viewTestLinks(request):
    conf_list = Conference.objects.order_by('event_date').reverse()
    contents = {
        'conf_list' : conf_list,
    }
    return render(request, 'home/testlinks.html', contents)
