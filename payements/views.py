from django.shortcuts import redirect, render

from payements import models
from payements.models import Checkout
import stripe

# Create your views here.

def checkout(request):
    return render(request, 'checkout.html')
stripe.api_key = 'sk_test_51P8kbuP4tIpb0Xu5OQbR1RyMdkJOciwBRtpXdHun9EmU079mA4E21P15btXctHNEx8W8FrH5xKGKE9FP8uYOnium00eeLciUcU'

def create_checkout_session(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': "price_1P8l26P4tIpb0Xu5xZ1UxCYB",
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/payment-success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )
    return redirect(checkout_session.url, code=303)

def success(request):
    return render(request, 'payements/success.html')


def cancel(request):
    return render(request, 'cancel.html')