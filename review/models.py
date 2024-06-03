from django.db import models
from django.contrib.auth import get_user_model
from people.models import PeopleType

User=get_user_model()

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment')
    to_who=models.ForeignKey(PeopleType,on_delete=models.CASCADE,related_name='comment')
    
    text=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.author
    



class Like(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='like')
    to_who=models.ForeignKey(PeopleType,on_delete=models.CASCADE,related_name='like')







# Create your models here.
