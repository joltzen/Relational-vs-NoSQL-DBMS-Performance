from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Coupon(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    expiring_date = models.DateTimeField()
    discount_amt = models.FloatField(default=0.0)
    score = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)


class Hashtag(models.Model):
    name = models.CharField(max_length=32)
    coupons = models.ManyToManyField(Coupon, blank=True)
