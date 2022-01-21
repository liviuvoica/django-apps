from django.db import models

# Create your models here.

# Blog post model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class Post(models.Model):
    title = models.TextField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.title
        
# Blog categories model will have a many to one relationship
# with the User model via 'owner' foreign key and a many to many relationship with
# the Post model via 'post' foreign key
# related_name refers to a custom access name for the current model
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

# Blog post comments model will have a many to one relationship
# with the User model via 'owner' foreign key and with the Post model via 'post' foreign key
# related_name refers to a custom access name for the current model
class Comment(models.Model):
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return str(self.owner).upper()