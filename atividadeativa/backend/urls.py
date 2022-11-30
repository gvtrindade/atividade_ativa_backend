from django.urls import path
from . import views

app_name='backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<int:question_id>', views.results, name='results'),
    path('vote/<int:question_id>', views.vote, name='vote'),
]