from django.db import models
from django.contrib.auth.models import User

class Coupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False, blank=True)    
    name = models.CharField(max_length=32)
    expiring_date = models.DateTimeField(null=True, blank=True)
    discount_amt = models.FloatField(default=0.0)
    score = models.IntegerField(default=0)
    def __str__(self):
        return "%s - %s" % (self.user, self.id)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)


class Hashtag(models.Model):
    name = models.CharField(max_length=32)
    coupons = models.ManyToManyField(Coupon, blank=True)
