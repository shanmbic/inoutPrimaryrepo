from django.shortcuts import render

# Create your views here.
from django.core.context_processors import request  
from django.contrib.auth.models import User
from romeocore.models import UserProfile, Messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.


def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			return HttpResponse(status=201)
		else:
			return HttpResponse(status=400)

@csrf_exempt 
def register(request):
	#print request
	if request.method == 'POST':
		data = json.loads(request.body)
		try:
			name = data['name']
			email = data['email']
			username = data['username']
			password = data['password']
			repassword = data['repassword']
			lat = data['lat']
			lon = data['lon']
			r=requests.get(url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+lat+','+lon+'&key=AIzaSyD2PEgdYwVh8FcdHEVWb0vg05pJm--RXHk').json()
			r=dict(r)
			location=r["results"][0]["address_components"][5]["long_name"]
			type_user = data['user_type']
			phone = data['phone']
			if password == repassword:				
				try:
					user = User.objects.create_user(username, password, email)
				except:
					return HttpResponse('Username already exists', status=500, content_type='text/plain')
				profile = UserProfile.objects.create(user=user, name=name, phone=phone,  current_location=location, type_user=type_user)
				return HttpResponse(status=200)
		except Exception, e:
			print e
			return HttpResponse(status=400)


@login_required
def search_users(request):
	data=[]
	if request.method == 'POST':
		username = request.POST['username']
		user = UserProfile.objects.get(username=username)
		user_location = user.current_location
		users = UserProfile.objects.filter(current_location=user_location)
		for item in users:
			data.append({'username':item.username, 'name':str(item.name)})
		return HttpResponse(json.dumps(data), mimetype='application/json')

@login_required
def search_messages(request):
	data = []
	if request.method == 'POST':
		username = request.META['username']
		user = UserProfile.objects.get(username=username)
		user_location = user.current_location
		messages = Messages.objects.filter(user__current_location==user_location)
		for item in messages:
			data.append({'username':item.username, 'content':item.content, 'timestamp':item.timestamp})
		return HttpResponse(json.dumps(data), mimetype='application/json')
	else:
		return HttpResponse('Login Required', status=400, content_type='text/plain' )



@login_required
def push_messages(request):
	if request.method == 'POST':
		try:
			user = request.META['username']
			content = request.POST['content']
			timestamp = request.POST['timestamp']
			message = Messages.objects.create(content=content, user=UserProfile.objects.get(username=user), timestamp=timestamp)
			return HttpResponse(status=200)
		except:
			return HttpResponse(status=400)

@login_required
def logout(request):
	try:
		logout(request)
		return HttpResponse(status=200)
	except:
		return HttpResponse('Please login', status=500, content_type='text/plain')

@login_required
def askquestion(request):
	if request.method == 'POST':
		user = request.META['username']
		if user.type_user == 'HEALTH_WORKER':
			question_type = request.POST['question_type']
			question = request.POST['question']
			headers = {'Content-Type':'application/json'}
			data = {"question": {"questionText":question}}
			r = request.post(url='https://gateway.watsonplatform.net/question-and-answer-beta/api/v1/question/{healthcare}/', auth=("05ed1923-b4e5-4c92-bb92-c5c25dc0404e","amfepk6cPdDO"), headers=headers, data=json.dumps(data)).json()
			x=str(r[0]['question']['evidencelist'][10]['text'])
			return HttpResponse(x, status=200, content_type='text/plain')
		else:
			return HttpResponse('Login as HEALTH_WORKER', status=400, content_type='text/plain')
	else:
		return HttpResponse('Login to continue', status=400, content_type='text/plain')


@login_required
def get_doctors(request):
	data=[]
	if request.method == 'POST':
		user = request.META['username']
		if user.type_user == 'HEALTH_WORKER':
			users = UserProfile.objects.filter(current_location==user.current_location, type_user=='DOCTOR')
			for item in users:
				data.append({'name':str(item.name), 'phone':item.phone})
			return HttpResponse(json.dumps(data), mimetype='application/json')
		else:
			return HttpResponse('Login as HEALTH_WORKER', status=400, content_type='text/plain')


data = {"model_id": "en-fr","source": "en", "target": "es","text": ["My name is"]}

data = {"languages": ["Hello"]}