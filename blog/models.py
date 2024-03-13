from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)
    
    class Meta:
        verbose_name_plural = "categories"
        
     # this will keep the name of the model in the admin site as "Categories" instead of "categorys"   
    def __str__(self):
        return self.name
    

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    Categories = models.ManyToManyField("category",related_name = "posts")
    # This will keep the name of the post as its tittle in the admin site as well as the real site
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.CharField(max_length = 60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey("post",on_delete = models.CASCADE)
    
    # This will set the name of the comment done by a user in a blog as shown below instead of saying a random comment object
    def __str__(self):
        return f"'{self.author}' on '{self.post}'"