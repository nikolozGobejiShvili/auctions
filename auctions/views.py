from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Post, AuctionListing, Bid, Category, Comment
from django.views.generic import ListView
from .forms import PostCreateFrom , CommentCreateForm, BidForm



def index(request):
    post = Post.objects.all
    comments = Comment.objects.all()
    return render(request, "auctions/index.html",{
        "posts" : post,
        "comments": comments,

    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# @login_required   
# def post_create_view(request):
    
#     if request.method == "GET" :
        
#         form=PostCreateFrom()
#         return render(request,"auctions/new.html",{
#             "form": form,
#             "categories": Post.objects.all()
#         })
    
#     form = PostCreateFrom(request.POST, request.FILES)
      
#     if form.is_valid():
#          post = form.save(commit=False)
#          post.user = request.user
#          post.save()
#          return redirect("auctions/new.html")
    
#     return redirect("auctions/index.html")
@login_required
def post_create_view(request):
    if request.method == "GET":
        form = PostCreateFrom()
        return render(request, "auctions/new.html", {
            "form": form,
            "categories": Post.objects.all()
        })

    form = PostCreateFrom(request.POST, request.FILES)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect("index")

    return redirect("index")





@login_required
def get_post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    bids= Bid.objects.all()

    # Handle comment submission if the request is a POST
    if request.method == "POST":
        comment_form = (request.POST)
        if comment_form.is_valid():
            body = comment_form.cleaned_data["body"]
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()

    else:
        comment_form = CommentCreateForm()

    return render(request, "auctions/post_details.html", {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "bids": bids,
    })




@login_required
def watchlist(request):
    user = request.user
    watchlist_posts = user.watchlist.all()
    return render(request, 'auctions/watchlist.html', {'watchlist_posts': watchlist_posts})


@login_required
def add_watchlist(request, pk):
    post = get_object_or_404(Post, pk=pk)
    request.user.watchlist.add(post)
    return redirect('watchlist')



@login_required
def remove_watchlist(request, pk):
    post = get_object_or_404(Post, pk=pk)
    request.user.watchlist.remove(post)
    return redirect('watchlist')

def bid(request, pk):
    post = get_object_or_404(Post, pk=pk)
    listing = AuctionListing.objects.get(post_id=post.pk)
    if request.method == "POST":
        bid_amount = float(request.POST.get('bid_amount', 0))
        highest_bid = listing.highest_bid()

        if bid_amount < listing.starting_bid:
            error_message = "Your bid must be at least the starting bid."
        elif highest_bid and bid_amount <= highest_bid.bid_amount:
            error_message = "Your bid should be higher than the current highest bid."
        else:
            bid = Bid(auction_listing=listing, bidder=request.user, bid_amount=bid_amount)
            bid.save()
            return redirect("post-details", pk=pk)

    return render(request, "auctions/bid.html", {
        "post": post,
        "listing": listing,
        "error_message": error_message
    })

@login_required
def close_auction(request, pk):
    auction_listing = get_object_or_404(AuctionListing, pk=pk)

    
    if auction_listing.created_by == request.user:
        
        auction_listing.closed = True
        highest_bid = auction_listing.highest_bid()
        if highest_bid:
            auction_listing.post.price = highest_bid.bid_amount
            auction_listing.post.save()

        auction_listing.save()

    return redirect('post-details', pk=auction_listing.post.pk)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'auctions/category_listings.html', {'categories': categories})



def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    active_listings = Post.objects.filter(category_id=category_id)
    return render(request, 'auctions/category_detail.html', {'category': category, 'listings': active_listings})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment_form = CommentCreateForm(request.POST)
        if comment_form.is_valid():
            body = comment_form.cleaned_data["body"]
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()

    return redirect("post-details", pk=post.pk)