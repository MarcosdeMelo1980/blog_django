from django.urls import path 
#from . import views 
from .views import HomeView, ArticleDetailView, AddPostView

#include - A function that takes a full Python import path to another URLconf module that should be “included” in this place. Optionally, the application 
#namespace and instance namespace where the entries will be included into can also be specified.

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name='add_post')
]

