import math
import random

from django.shortcuts import render
import razorpay
from rest_framework import status

from PaymentProject.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import requests

# from decouple import config
# API = config("OTP_API")
# Create your views here.
from raz import models


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def payment(request):
    amount = 500
    currency = "INR"
    receipt = "order_rcptid_11"
    payment_order = client.order.create(dict(amount=amount,currency=currency,receipt=receipt,payment_capture=1))
    payment_order_id = payment_order['id']

    return render(request,'payments.html',{'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id})




def messages(request):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "variables_values=5599&route=otp&numbers=9526621880"
    headers = {
        'authorization': "Lderu02qNhVRBFG5kZpf71Jv3CsYXKUmnjwizbWHyEP6ltI4Ogp12Kf6z9D0ZlmQBXNs8jExhLAnai5e",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return render(request,'message.html', {"res" : response.text})



    # digits_in_otp = "0123456789"
    # OTP = ""
    #
    # # fr a 4 digit OTP we are using 4 in range
    # for i in range(6):
    #     OTP += digits_in_otp[math.floor(random.random() * 10)]
    #
    # print(OTP)
    #
    # mobile_num = 9526621880
    # url = "https://www.fast2sms.com/dev/bulkV2"
    # payload = f"variables_values={OTP} , Team  Arclif Inc ! &route=otp&numbers={mobile_num})"
    # headers = {
    #     'authorization': "Lderu02qNhVRBFG5kZpf71Jv3CsYXKUmnjwizbWHyEP6ltI4Ogp12Kf6z9D0ZlmQBXNs8jExhLAnai5e",
    #     'Content-Type': "application/x-www-form-urlencoded",
    #     'Cache-Control': "no-cache",
    # }
    #
    # response = requests.request("POST", url, data=payload, headers=headers)
    # if not response:
    #     return {"status": status.HTTP_503_SERVICE_UNAVAILABLE}
    #
    #
    # print(status.HTTP_202_ACCEPTED,mobile_num)
