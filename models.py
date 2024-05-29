from django.db import models
from django.contrib import admin

#adfs is the database model name for the students who are registered
class adfs(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()    
    email = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.username


# model for editing character cards
#will adjust later to add more fields
class teachers(models.Model):

    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)
    question = models.CharField(max_length=55, null=True, blank=True)
    answer = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.name


# model for teachers who have registered
# fsteacher.com
class teachusers(models.Model):
    #let the fields stay for user verification

    id = models.AutoField(primary_key=True)
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.username


#for admin user management
# fsadmin.com
class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    

    def __str__(self):
        return self.username
    



