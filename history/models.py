from django.db import models
from django.contrib.auth import get_user_model
from people.models import PeopleType


User=get_user_model()

class History(models.Model):
    searcher=models.ForeignKey(User,on_delete=models.CASCADE)
    crush=models.ForeignKey(PeopleType,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.searcher,self.crush



# Create your models here.
