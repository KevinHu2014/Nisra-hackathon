from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import User
from models import Message
from models import Send
from time import strftime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db import connection
import random
# git test
# Create your views here.
@csrf_exempt
def checkLogin(request):
    print request.POST
    email = request.POST["email"]
    password = request.POST["password"]
    success = User.objects.filter(Q(userEmail=email)&Q(userPassword=password)).count()
    if success == 0:
	   return render_to_response('future/fail.html')
    else:
	   return render_to_response('future/success.html')	

def loginPage(request):
    return render_to_response('Login.html')
  
def userAdd(request):
	name = request.POST["userName"]
	email = request.POST["userEmail"]
	password = request.POST["password"]
	checkCode = random.randint(1000,10000)
	while User.objects.filter(checkCode=checkCode).count() > 0
		checkCode = random.randint(1000,10000)
	success = User.objects.filter(userEmail=email).count()
	if success == 0:
		user = User(userName=name,userEmail=email,userPassword=password,checkCode=checkCode)
		user.save()
		#send email not to do
		return render_to_response('future/UserSuccess.html')
	else:
		return render_to_response('future/UserFail.html')
