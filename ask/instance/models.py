from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % (self.tag)

class Service(models.Model):
    request = models.TextField()
    user_request = models.ForeignKey(User, related_name='author')
    assigned = models.ForeignKey(User)
    skills = models.ManyToManyField(Skill)
