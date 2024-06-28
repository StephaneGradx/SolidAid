from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from App import settings
from accounts.views import logout_view, connexion, register
from contact.views import contact
from forum.views import check, getMessages, home, room, send
from payements.views import cancel, checkout, create_checkout_session, success
from solidAid.views import details_actions, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('actions', details_actions, name="actions"),
    path('connexion/', connexion, name="connexion"),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name="register"),
    path('contact/', contact, name="contact"),
    path('home', home, name="home"),
    path('check', check, name="check"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),
    path('checkout', checkout, name="checkout"),
    path('create_checkout_session', create_checkout_session, name="create_checkout_session"),
    path('payment-success/', success, name="success"),
    path('<str:room>/', room, name="room"),
    path('cancel/', cancel, name="cancel"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
