from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    # --- PAGES PRINCIPALES ---
    path('', views.home, name='home'),
    path('index.html', views.index, name='index'),
    path('about-us.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('gallery.html', views.gallery, name='gallery'),
    path('team.html', views.team, name='team'),
    path('pricing.html', views.pricing, name='pricing'),
    
    # --- SERVICES ---
    path('our-services.html', views.services, name='services'),
    path('services-detail.html', views.services_detail, name='services_detail'),
    
    # --- BLOG (LISTE) ---
    path('blog.html', views.blog, name='blog'),

    # --- BLOG (DÉTAIL DYNAMIQUE - LE PLUS IMPORTANT) ---
    # C'est cette ligne qui permet d'afficher un article spécifique quand on clique dessus
    path('blog/<slug:slug>/', views.blog_detail_dynamic, name='blog_detail'),

    # --- BLOG (PAGES STATIQUES - OPTIONNEL) ---
    # Tu peux les garder si tu veux voir les designs originaux, 
    # mais à terme, tu utiliseras la ligne dynamique ci-dessus.
    path('single-blog-post-left-sidebar.html', views.blog_left, name='blog_left'),
    path('single-blog-post-right-sidebar.html', views.blog_right, name='blog_right'),
    path('single-blog-post-without-sidebar.html', views.blog_no_sidebar, name='blog_no_sidebar'),
]