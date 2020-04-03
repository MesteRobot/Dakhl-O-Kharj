from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Expence, Income, Token,User
#from django.contrib.auth.models import 
# Create your views here.


@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Income.objects.create(text=request.POST['text'], amount=request.POST['amount'], user=this_user)
    
    return JsonResponse({
        'status :': 'ok',

    }, encoder=JSONEncoder)


@csrf_exempt
def submit_expence(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Expence.objects.create(text=request.POST['text'], amount=request.POST['amount'], user=this_user)
    
    return JsonResponse({
        'status :': 'ok',

    }, encoder=JSONEncoder)
