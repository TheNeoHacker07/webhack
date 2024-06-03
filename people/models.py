from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class PeopleType(models.Model):
    #author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=13)
    second_name=models.CharField(max_length=13)
    img=models.ImageField(upload_to='user_img',blank=True)
    email=models.EmailField(unique=True)



    def __str__(self):
        return self.email

