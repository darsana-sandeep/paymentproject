from django.shortcuts import render
import razorpay
from PaymentProject.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
# Create your views here.

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def payment(request):
    amount = 500
    currency = "INR"
    receipt = "order_rcptid_11"
    payment_order = client.order.create(dict(amount=amount,currency=currency,receipt=receipt,payment_capture=1))
    payment_order_id = payment_order['id']

    return render(request,'payments.html',{'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id})

