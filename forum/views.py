
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from forum.models import Message, Room

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def room(request, room):
    if room in ['success', 'cancel', 'payment-success', 'some-other-reserved-name']:
        return HttpResponse('Invalid room name', status=400)

    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)

    print("Nom de la pièce :", room)
    print("Détails de la pièce :", room_details)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })

@login_required
def check(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username='+ username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username='+ username)
@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value = message, user = username, room = room_id)
    new_message.save()
    return HttpResponse('Message envoye avec succes !')
@login_required
def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room = room_details.id).order_by('date')
    return JsonResponse({"messages":list(messages.values())})