from django.urls import path,include
from .views import PeopleList,PersonRetriev,PersonDelete,PersonUpdate,PersonCreate

urlpatterns = [
    path('people_list/',PeopleList.as_view()),
    path('person/<int:id>/',PersonRetriev.as_view()),
    path('person_create/',PersonCreate.as_view()),
    path('person_delete/<int:id>',PersonDelete.as_view()),
    path('person_update/<int:id>/',PersonUpdate.as_view())
]