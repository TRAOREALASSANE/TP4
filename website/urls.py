from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.index, name='index'),
    path('about-us.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('gallery.html', views.gallery, name='gallery'),
    
    # Corrections des noms de fonctions
    path('our-services.html', views.services, name='services'),
    path('services-detail.html', views.services_detail, name='services-detail'),
    
    path('team.html', views.team, name='team'),
    path('pricing.html', views.pricing, name='pricing'),
    


    # Corrections blog
    path('blog.html', views.blog, name='blog'),
    path('single-blog-post-left-sidebar.html', views.blog_left, name='blog_left'),
    path('single-blog-post-right-sidebar.html', views.blog_right, name='blog_right'),
    path('single-blog-post-without-sidebar.html', views.blog_no_sidebar, name='blog_no_sidebar'),










]