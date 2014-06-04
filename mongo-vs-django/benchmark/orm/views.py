from django.shortcuts import render, get_object_or_404
from orm.models import GenericTweet, mongoConnect


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
        'beg': beg,
        'end': end,
        'limit': limit,
        'skip': skip,
        'tweet_count': tweet_count,
        'tweets': preprocessed_tweets[::-1]
    }
    return render(request, 'tweets.html', args)

