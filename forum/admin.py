from django.contrib import admin

from forum.models import Room, Message

admin.site.register(Room)
admin.site.register(Message)