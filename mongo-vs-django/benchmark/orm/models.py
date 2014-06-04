from django.db import models
import mongoengine as mongo

# Create your models here.
#class Product(models.Model):
    #name = models.CharField(max_length=255)
    #unitsInStock = models.IntegerField
    #price = models.DecimalField

    #class Meta:
        #ordering = [ 'name' ]

    #def __unicode__(self):
        #return u'%s' % self.name

class GenericTweet(mongo.Document):
    tweetid = mongo.fields.IntField(required=True)
    userid = mongo.fields.IntField(required=True)
    text = mongo.fields.StringField(required=True, max_length=200)
    location = mongo.fields.BaseField(required=True)
    geohash = mongo.fields.StringField(required=True, max_length=32)
    in_reply_to_id = mongo.fields.IntField(required=False)
    username = mongo.fields.StringField(required=True, max_length=32)
    screen_name = mongo.fields.StringField(required=True, max_length=32)
    description = mongo.fields.StringField(required=False, max_length=256)

def mongoConnect():
    mongo.connect('twitter', host='localhost:27017')
