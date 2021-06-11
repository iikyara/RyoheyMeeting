from django.shortcuts import render

def index(request):
    return render(request, 'ReactionSocket/index.html')

def room(request, room_name):
    return render(request, 'ReactionSocket/room.html', {
        'room_name': room_name
    })

def gather(request, conf_id):
    return render(request, 'ReactionSocket/gather.html', {
        'conf_id': conf_id
    })
