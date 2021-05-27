from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'ReactionButton/index.html')

def view_reactionbutton(request):
    if "userid" in request.GET:
        userid = int(request.GET["userid"])
        if userid == 1:
            contents = {'name' : '杉野森'}
        if userid == 2:
            contents = {'name' : '前川'}
        contents["userid"] = request.GET["userid"]
    else:
        print('no_data')
        return HttpResponse(status=201)
    return render(request, 'ReactionButton/ReactionButton.html', contents)

def push_reaction(request):
    info = {}
    if "reaction" in request.GET:
        info['reaction'] = request.GET['reaction']
    if "reaction" in request.GET:
        info['userid'] = request.GET['userid']
    print(info)
    return HttpResponse(status=201)