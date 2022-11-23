from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   pass

class Post(models.Model):
    content = models.CharField(null = False,max_length=1500)
    createdate = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "posts")
    
    class Meta:
        ordering = ["createdate"]
        
    def __str__(self):
        return f"content : {self.content} "
    
class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    follower = models.ManyToManyField(User,blank=True,related_name = "followers")
    following= models.ManyToManyField(User,blank=True,related_name = "followings")
    
    
    def __str__(self):
        return f"user : {self.user.username}"
 
    
# class Followings(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return f"user : {self.user.username}"
    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"user : {self.user.username} , post : {self.post.content}"
    
# class Follow(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     follow = models.BooleanField()
#     createdate = models.DateTimeField(auto_now_add = True)
   
#     def __str__(self):
#         return f"user : {self.user.username} , post : {self.post.content}"
    
    
