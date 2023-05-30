from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name





class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class AuctionListing(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    def highest_bid(self):
        return self.bids.order_by('-bid_amount').first()

    def is_expired(self):
        return self.post.modified_at < timezone.now()

class Bid(models.Model):
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)    