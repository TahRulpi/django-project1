from django.urls import path,include
from .router import router
from django.urls import re_path
from . import views


urlpatterns=[
   path('', include(router.urls)),
    re_path(r'^rest-auth/', views.task_viewset.as_view({'get': 'list', 'post': 'create'}), name='rest-auth'),
   
   path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
   #path('login/', views.UserLoginView.as_view(), name='user-login'),
    
]
