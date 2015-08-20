from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % (self.tag)

class Service(models.Model):
    FULFILLED = 'FU'
    CANCELLED = 'CA'
    IN_PROGRESS = 'IP'
    PENDING_PAYMENT = 'PP'
    STATUS_CHOICES = (
        (FULFILLED, 'Fulfilled'),
        (CANCELLED, 'Cancelled'),
        (IN_PROGRESS, 'In Progress'),
        (PENDING_PAYMENT, 'Pending Payment')
    )

    HIGH = 300
    NORMAL = 200
    LOW = 100
    PRIORITY_STATUS = (
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low')
    )

    request = models.TextField()
    user_request = models.ForeignKey(User, related_name='author', related_query_name="authors")
    assigned = models.ManyToManyField(User, blank=True, related_query_name="services", related_name="service")
    skills = models.ManyToManyField(Skill, related_query_name="skills", related_name="skill",
                                    help_text="Select the required skills")
    state = models.CharField(max_length=2, choices=STATUS_CHOICES, default=IN_PROGRESS)
    priority = models.IntegerField(choices=PRIORITY_STATUS, default=NORMAL)
    no_people = models.IntegerField(help_text="Number of people for the service", default=1)
    cancellable = models.BooleanField(default=False,
                                      help_text="Should it be cancelled if it doesn't reach minimum number of people?")

    def __unicode__(self):
        return u"%s, %s, %s" % (self.user_request, self.priority, self.request[:100])

class Rating(models.Model):
    EXCELLENT = 500
    VERY_GOOD = 400
    GOOD = 300
    POOR = 200
    DISASTER = 100

    RATING_CHOICES = (
        (EXCELLENT, "Excellent"),
        (VERY_GOOD, "Very good"),
        (GOOD, "Good"),
        (POOR, "Poor"),
        (DISASTER, "Disaster")
    )

    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    service = models.ForeignKey(Service)
    requester = models.ForeignKey(User, related_name="request_rating")
    performer = models.ForeignKey(User, related_name="performer_rating")

    class Meta:
        unique_together = (("service", "performer", "requester"))