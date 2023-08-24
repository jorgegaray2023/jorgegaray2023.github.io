from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('single/', views.single, name='single'),
    path('project/', views.project, name='project'),
]