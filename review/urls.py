from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import like_handler


from .views import CommentViewSet,my_view

router=DefaultRouter()
router.register('comment',CommentViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('like/<int:id>/',like_handler),
    path('user/',my_view)
    
]