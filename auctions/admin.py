from django.contrib import admin
from .models import Post, Comment, Bid, AuctionListing, Category

admin.site.register([Post, Comment, Bid, AuctionListing, Category])