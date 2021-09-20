from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from home.models import *

@login_required
def index(request):
    pres = Presenter.objects.filter()
    users = []
    for p in pres:
        users.append({
            'user' : p,
            'name' : p.user.get_full_name(),
            'nickname' : p.user.nickname,
            'userid' : p.id
        })
    contents = {'users' : users}
    return render(request, 'ReactionButton/index.html', contents)

@login_required
def view_reactionbutton(request):
    if "userid" in request.GET:
        contents = {}
        userid = int(request.GET["userid"])
        pre = Presenter.objects.filter(id=userid)
        if len(pre)==0:
            return redirect('ReactionButton_home')
        pre = pre[0]
        contents = {
            'dest_user' : pre.user,
            'name' : pre.user.get_full_name(),
            'nickname' : pre.user.nickname,
            'userid' : pre.id
        }
    else:
        return redirect('ReactionButton_home')
    return render(request, 'ReactionButton/ReactionButton.html', contents)

@login_required
def push_reaction(request):
    info = {}
    if "reaction" in request.GET and "userid" in request.GET and "count" in request.GET:
        reaction = int(request.GET['reaction'])
        userid = int(request.GET['userid'])
        count = int(request.GET['count'])
        pre = Presenter.objects.filter(id=userid).first()
        conf = Conference.getCurrentConference().first()
        reacT = ReactionType.objects.filter(number=reaction).first()
        if not pre or not conf or not reacT:
            return HttpResponse(status=400)
        reac_cnt = Reaction.objects.filter(reaction_type=reacT, dest_user=pre.user, conference=conf).first()
        print(reac_cnt == None)
        if reac_cnt:
            reac_cnt.count += count
            reac_cnt.save()
            print("update : %s" % str(reac_cnt))
        else:
            reac_cnt = Reaction.objects.create(count=count, dest_user=pre.user, conference=conf, reaction_type=reacT)
            print("add : %s" % str(reac_cnt))
    return HttpResponse(status=201)

@login_required
def test_scss(request):
    contents = {
        "userid" : Presenter.objects.filter()[0].id
    }
    return render(request, 'ReactionButton/test.html', contents)

@login_required
def view_reactionresult(request, conf_id):
    conf = Conference.getConferenceById(conf_id).first()
    if not conf:
        return HttpResponse(status=404)
    #reac_cnt = Reaction.objects.filter(conference=conf).order_by('dest_user')
    reac_cnt = Reaction.getReactionsByEachPresenter(conf)
    contents = {
        "conf" : conf,
        "reactions" : reac_cnt,
    }
    return render(request, 'ReactionButton/ReactionResult.html', contents)
