from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Guest(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

