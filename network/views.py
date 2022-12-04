from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.core.paginator import Paginator

class NewPostForm(forms.Form):
    content = forms.CharField(
        max_length=1500,
         widget=forms.Textarea(
            attrs={"placeholder": "content", "class": "form-control col-12"}
        ))
   
def index(request):
    posts = Post.objects.all().order_by("-createdate")
    list_post = []
    for post in posts:
        is_liked = post.like_set.filter(user = request.user.id).first() is not None  
        like_count = post.like_set.count()
        list_post.append({'id':post.id, 'user_id' : post.user.id ,'username' :post.user.username , 'content' : post.content ,
                          'date' : post.createdate.date() , 'time' : post.createdate.time(), 'likecount' : like_count , 'isLiked':is_liked })
        
    # Pagination
    paginator = Paginator(list_post, 10) # Show 10 posts per page.
    page_number = int(request.GET.get('page') or 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html",{
        "posts" : page_obj ,
        "form" : NewPostForm()
    })
    

@login_required(login_url='/login')
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            # Save a record
            user = User.objects.get(pk = request.user.id)
            post = Post(
                user = user,
                content = content
            )
            post.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/index.html", {
                "form": form
            })
    else:
          return render(request, "network/index.html", {
              "form" : NewPostForm()
          })
          
@login_required(login_url='/login')
def edit_post(request):
    
    data = json.load(request)
    post_id = data['post_id']
    content = data['content']
    
    if content is None:
        message = "fill your content please"
        return JsonResponse({
             "message" : message,
             "status": 200
            })
   
    post = Post.objects.filter(id = post_id).first()
    if post is None:
        message = "post is not found"
        return JsonResponse({
         "message" : message,
         "status": 404
        })
     
    if  post.user.id != request.user.id:
        message = "you are not allowed to edit other user's post"
        return JsonResponse({
         "message" : message,
         "status": 401
        })
    
  
    post.content = content
    post.save()
    
    return JsonResponse({
                 "status": 200
            })
    
           
def profile(request,user_id):
    
    follow_user = User.objects.get(id = user_id)    
    followers = follow_user.followings.count()
    followings = follow_user.followers.count()
    posts = follow_user.posts.all().order_by("-createdate")
    
    list_post = []
    for post in posts:
        is_liked = post.like_set.filter(user = request.user.id).first() is not None  
        like_count = post.like_set.count()
        list_post.append({'id':post.id, 'user_id' : post.user.id ,'username' :post.user.username , 'content' : post.content ,
                          'date' : post.createdate.date() , 'time' : post.createdate.time(), 'likecount' : like_count , 'isLiked':is_liked })
        
    user = User.objects.filter(id = request.user.id).first()
    follower = follow_user.followings.filter(user = user).first()
    # Pagination
    paginator = Paginator(list_post, 10) # Show 10 posts per page.
    page_number = int(request.GET.get('page') or 1)
    page_obj = paginator.get_page(page_number)   
    return render(request, "network/profile.html",{
        "posts" : page_obj,
        "followers" : followers,
        "followings" : followings,
        "posts_count" : posts.count(),
        "user_info":follow_user,
        "isfollowed": follower is not None
    })
      

@login_required(login_url='/login')
def following(request):
    user = User.objects.get(id = request.user.id)
    follow = Follow.objects.filter(user = user).first()
    if follow is None:
            return render(request, "network/following.html", {
               "posts" : [],
          })
    posts=[]
    followings = follow.following.all()
    list_post = Post.objects.filter(user__in = followings).all().order_by("-createdate")
    for post in list_post:
            is_liked = post.like_set.filter(user = request.user.id).first() is not None  
            like_count = post.like_set.count()
            posts.append({'id':post.id, 'user_id' : post.user.id ,'username' :post.user.username , 'content' : post.content ,
                            'date' : post.createdate.date() , 'time' : post.createdate.time(), 'likecount' : like_count , 'isLiked':is_liked })
         
    # Pagination
    paginator = Paginator(posts, 10) # Show 10 posts per page.
    page_number = int(request.GET.get('page') or 1)
    page_obj = paginator.get_page(page_number)   
    return render(request, "network/following.html",{
        "posts" : page_obj,
    })


@login_required(login_url='/login')
def follow_user(request):
        data = json.load(request)
        follow_status = data['follow_status']
        user_id = data['user_id']
       
        follow_user = User.objects.filter(id = user_id).first()
        if follow_user is None:
            message = "user is not found"
            return JsonResponse({
                 "message" : message,
                 "status": 404
            })
        if  follow_user.id == request.user.id:
            message = "you are not allowed to follow yourself"
            return JsonResponse({
                 "message" : message,
                 "status": 401
            })
            
        user = User.objects.filter(id = request.user.id).first()
        follow1= Follow.objects.filter(user = user).first()
        follow2= Follow.objects.filter(user = follow_user).first()
       
        follow_status = int(follow_status)
        
        if follow_status == 1 :
            if  follow1 is None:
                follow = Follow(user = user)
                follow.save()
                follow.following.add(follow_user)
            
            else:
                follow1.following.add(follow_user)
                
            
            if  follow2 is None:
                follow = Follow(user = follow_user)
                follow.save()
                follow.follower.add(user)
            
            else:
                follow2.follower.add(user)
            
        else:
            follow1.following.remove(follow_user)
            follow2.follower.remove(user)
       
            
        return JsonResponse({
                 "status": 200,
                 "followers": follow_user.followings.count(),
                 "followings":  follow_user.followers.count(),
            })
   
     
   
@login_required(login_url='/login')
def like_post(request,post_id):
    if request.method == "POST":
        post = Post.objects.filter(id = post_id).first()
        if post is None:
            message = "post is not found"
            return JsonResponse({
                 "message" : message,
                 "status": 404
            })
         
        if  post.user.id == request.user.id:
            message = "you are not allowed to like or dislike your post"
            return JsonResponse({
                 "message" : message,
                 "status": 401
            })
            
        user = User.objects.filter(id = request.user.id).first()
        like = Like.objects.filter(post = post).filter(user = user).first()
        
        if like is None:
            like = Like(
                    user = user,
                    post = post
                    ) 
            like.save()
              
        else:
            like = like.delete() 
           
        
        likes_count = Like.objects.filter(post = post).count()
        
        return JsonResponse({
                 "likes" : likes_count,
                 "status": 200
            })
    else:
          return JsonResponse({
                 "message" : "try again",
                 "status": 400
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
