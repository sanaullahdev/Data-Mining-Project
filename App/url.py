
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('operation/',views.preprocess,name='operation'),
    path('categorize/',views.categorization,name='cate'),
    path('categorize/',views.categorization,name='cat'),
]
