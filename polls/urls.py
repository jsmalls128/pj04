from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #Need to create a new view for homepage
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', views.IndexView.as_view(), name='index'),
    path('polls/schema/', views.SchemaView.as_view(), name='schema'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]