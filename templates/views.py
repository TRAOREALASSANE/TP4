from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def home(request):
    # Vous pouvez passer des données au template ici
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        comment = request.POST.get('comment')

        # Sauvegarde
        ContactMessage.objects.create(
            name=name, email=email, website=website, comment=comment
        )
        messages.success(request, "Votre message a été envoyé avec succès !")
        return redirect('website:contact')

    return render(request, 'website/contact.html')

def about(request):
    context = {
        'title': 'About Us',
        'about': get_about()
    }
    return render(request, 'website/about-us.html', context)

# --- AUTRES PAGES (Fonctions renommées) ---

def gallery(request):
    return render(request, 'website/gallery.html')

def services(request):
    return render(request, 'website/our-services.html')

def services_detail(request):  # Renommé
    return render(request, 'website/services-detail.html')

def team(request):
    return render(request, 'website/team.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog_left(request): # Renommé
    return render(request, 'website/single-blog-post-left-sidebar.html')

def blog_right(request): # Renommé
    return render(request, 'website/single-blog-post-right-sidebar.html')

def blog_no_sidebar(request): # Renommé
    return render(request, 'website/single-blog-post-without-sidebar.html')





def get_about():
    return {
        'section_title': 'Since 1998',
        'about_title': 'Making transportation fast and safe',
        'description': "Lorem Ipsum is simply dummy text...",
        'about_author': 'Toto Titi',
        'about_fonction': "Directeur General",
        'about_service': [
            {'img':'1.svg', 'title':'Fast Deliver', 'description':'Lorem Ipsum', 'order':1},
            {'img':'1.svg', 'title':'100% Satifaction', 'description':'Lorem Ipsum', 'order':2},
            {'img':'3.svg', 'title':'24x7 Service', 'description':'Lorem Ipsum', 'order':3},
        ]
    }
