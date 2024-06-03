from django.urls import path,include
from .views import ListHistory,RetrieveHistory

urlpatterns=[
    path('get_history_list/',ListHistory.as_view()),
    path('get_history_retrieve/<int:id>/',RetrieveHistory.as_view())
]

