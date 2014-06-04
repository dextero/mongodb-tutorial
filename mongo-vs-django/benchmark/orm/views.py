from django.shortcuts import render, get_object_or_404
from orm.models import GenericTweet, mongoConnect
from orm.forms import UserForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()

	return render_to_response(
			'register.html',
			{'user_form': user_form, 'registered': registered},
			context)

def user_login(request):
	context = RequestContext(request)
	disabled = False
	invalid = False
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/tweets/')
			else:
				disabled = True
		else:
			invalid = True
	return render_to_response('login.html', 
			{'disabled': disabled, 'invalid': invalid}, 
			context)

# Create your views here.
def get_tweets(request):
    limit = 100
    skip = 0

    if 'limit' in request.GET:
        try:
            limit = int(request.GET['limit'])
        except ValueError:
            pass

    if 'skip' in request.GET:
        try:
            skip = int(request.GET['skip'])
        except ValueError:
            pass

    mongoConnect()
    tweet_count = GenericTweet.objects.count()

    end = max(0, tweet_count - skip)
    beg = max(0, end - limit)

    tweets = GenericTweet.objects[beg:end]
    preprocessed_tweets = []

    for tweet in tweets:
        preprocessed_tweets.append({
            'username': tweet.username,
            'screen_name': tweet.screen_name,
            'text': tweet.text,
            'location': u'%f, %f' % (tweet.location['lat'], tweet.location['lon'])
        })

    args = {
        'tweet_count': tweet_count,
        'tweets': preprocessed_tweets[::-1]
    }
    return render(request, 'tweets.html', args)

