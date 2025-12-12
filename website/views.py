from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import * 

# --- PAGE D'ACCUEIL ---
def index(request):
    return home(request) # Redirige vers la fonction home pour éviter de dupliquer

def home(request):
    # --- Pour banner.html ---
    banner = PageBanner.objects.filter(page_name='accueil', is_active=True).first()
    
    # --- Pour about.html ---
    about = AboutSection.objects.filter(is_active=True).first()
    about_features = AboutFeature.objects.filter(is_active=True).order_by('order')
    
    # --- Pour service.html ---
    services = Service.objects.all()[:3] # Les 3 premiers seulement
    
    # --- Pour paralax.html (Si c'est la section Video ou Why Choose Us) ---
    # Adapte ceci selon ce qu'il y a dans ton fichier paralax.html
    why_choose = WhyChooseUs.objects.filter(is_active=True).first()
    video = VideoSection.objects.first()

    # --- Pour map.html (AJOUT IMPORTANT) ---
    # Si tu inclus la map sur l'accueil, il faut l'envoyer ici aussi !
    map_info = MapSection.objects.filter(is_active=True).first()

    context = {
        'banner': banner,
        'about': about,         # Attention au nom de variable utilisé dans about.html
        'features': about_features,
        'services': services,
        'why_choose': why_choose,
        'video': video,
        'map': map_info,        # Variable pour map.html
    }
    return render(request, 'index.html', context)


def blog(request):
    # --- Données existantes (Bannière & Articles) ---
    header_info = BlogPostHeader.objects.filter(is_active=True).first()
    articles_list = bloc_spr.objects.all().order_by('-created_at')

    # --- NOUVELLES DONNÉES pour les autres sections ---
    # 1. Pour la section Partenaires (partners.html)
    partners = Client.objects.all()
    
    # 2. Pour la section Rejoignez-nous (join_us.html)
    join_us_data = JoinUsSection.objects.first()

    # --- On met tout dans le contexte ---
    context = {
        'header': header_info,
        'articles': articles_list,
        # On ajoute les nouvelles clés ici :
        'clients': partners,   # Attention: vérifie le nom de variable utilisé dans partners.html
        'join_us': join_us_data, # Attention: vérifie le nom de variable dans join_us.html
    }
    
    return render(request, 'website/blog.html', context)


def contact(request):
    # --- PARTIE 1 : GESTION DU FORMULAIRE (Quand on clique sur Envoyer) ---
    if request.method == "POST":
        # On récupère les données tapées par l'utilisateur
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        comment = request.POST.get('comment')

        # Vérification simple (Nom, Email et Message sont obligatoires)
        if name and email and comment:
            # On enregistre dans la base de données
            ContactMessage.objects.create(
                name=name,
                email=email,
                website=website,
                comment=comment
            )
            # On affiche un message de succès
            messages.success(request, "Votre message a bien été envoyé ! Nous vous répondrons vite.")
            # On recharge la page pour vider le formulaire (pattern PRG)
            return redirect('website:contact')
        else:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")

    # --- PARTIE 2 : RECUPERATION DES DONNEES POUR L'AFFICHAGE ---
    
    # 1. Pour 'website/sections/banner.html'
    # On cherche la bannière spécifique à la page 'contact'
    banner_info = PageBanner.objects.filter(page_name='contact', is_active=True).first()
    
    # 2. Pour 'website/sections/contact.html' (Infos adresse, tel, email...)
    contact_data = ContactSection.objects.first()

    # 3. Pour 'website/sections/map.html'
    map_data = MapSection.objects.filter(is_active=True).first()

    context = {
        'banner': banner_info,   # Variable pour banner.html
        'info': contact_data,    # Variable pour contact.html (Partie infos)
        'map': map_data,         # Variable pour map.html
    }

    # Assure-toi que le nom du fichier ici est bien celui de ton template
    return render(request, 'website/contact.html', context)


def gallery(request):
    # 1. Pour 'website/sections/banner_G.html'
    # On cherche une bannière spécifique qu'on nommera 'gallery' dans l'admin
    banner_info = PageBanner.objects.filter(page_name='gallery', is_active=True).first()

    # 2. Pour 'website/sections/portfolio.html'
    # On récupère tous les projets pour les afficher
    projects = PortfolioProject.objects.all()
    
    # (Optionnel) Si tu as besoin d'afficher les boutons de filtres dynamiquement
    # On récupère les catégories définies dans le modèle
    categories = PortfolioProject.CATEGORY_CHOICES

    # 3. Pour 'website/sections/about1.html'
    # On réutilise les infos de la section À Propos
    about_data = AboutSection.objects.filter(is_active=True).first()

    # 4. Pour 'website/sections/testimonials.html'
    testimonials_data = Testimonial.objects.all()

    context = {
        'banner': banner_info,       # Variable pour banner_G.html
        'projects': projects,        # Variable pour portfolio.html
        'categories': categories,    # (Optionnel) pour les filtres
        'about': about_data,         # Variable pour about1.html
        'testimonials': testimonials_data, # Variable pour testimonials.html
    }

    # Assure-toi que le nom du fichier ici est bien celui de ton template
    return render(request, 'website/gallery.html', context)


def index(request):
    # 1. Pour 'website/sections/slider.html' (Bannière d'accueil)
    # On cherche la bannière identifiée comme 'accueil'
    slider_data = PageBanner.objects.filter(page_name='accueil', is_active=True).first()

    # 2. Pour 'website/sections/about.html'
    about_data = AboutSection.objects.filter(is_active=True).first()
    # Souvent la section about affiche aussi des petites icônes (features)
    about_features = AboutFeature.objects.filter(is_active=True).order_by('order')

    # 3. Pour 'website/sections/service.html'
    # On affiche généralement les 3 ou 6 premiers services sur l'accueil
    services_data = Service.objects.all()[:3]

    # 4. Pour 'website/sections/feature.html'
    # Ce sont souvent les caractéristiques (ServiceFeature)
    features_data = ServiceFeature.objects.filter(is_active=True).order_by('ordre')

    # 5. Pour 'website/sections/paralax.html'
    # C'est souvent une vidéo ou une section avec image de fond fixe
    video_data = VideoSection.objects.first()

    # 6. Pour 'website/sections/les_autres_section.html'
    # Je charge ici tout ce qui pourrait s'y trouver :
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    join_us = JoinUsSection.objects.first()
    # Les 3 derniers articles de blog pour les "News"
    latest_articles = bloc_spr.objects.all().order_by('-created_at')[:3]

    context = {
        'banner': slider_data,      # Pour le slider
        'about': about_data,        # Pour about (requis par ton "with about=about")
        'about_features': about_features,
        'services': services_data,  # Pour service.html
        'features': features_data,  # Pour feature.html
        'video': video_data,        # Pour paralax.html
        
        # Données bonus pour "les_autres_section.html"
        'testimonials': testimonials,
        'clients': clients,
        'join_us': join_us,
        'articles': latest_articles, 
    }

    return render(request, 'index.html', context)


def home_view(request):
    context = {
        # Récupération depuis la DB
        'banner': Banner.objects.first(),
        'about': About.objects.first(),
        'services': Service.objects.all()[:6],
        'features': Feature.objects.all()[:8],
        'testimonials': Testimonial.objects.filter(active=True)[:4],
        'clients': Client.objects.all()[:10],
        
        # Statistiques calculées
        'stats': {
            'total_clients': Client.objects.count(),
            'total_services': Service.objects.count(),
            'total_projects': 450,  # Ou depuis un autre modèle
            'years_experience': 10,
        }
    }
    return render(request, 'home.html', context)


def pricing_view(request):
    context = {
        # Données pour banner_P.html (banner pricing)
        'banner_pricing': Banner.objects.filter(type='pricing').first() or Banner.objects.first(),
        
        # Données pour pricing.html
        'pricing_plans': Pricing.objects.all()[:6],  # Plans tarifaires
        
        # Données pour testimonials.html (réutilisation)
        'testimonials': Testimonial.objects.filter(active=True)[:6],
        
        # Statistiques spécifiques pricing
        'stats': {
            'plans_available': Pricing.objects.count(),
            'satisfied_clients': 250,
        }
    }
    return render(request, 'pricing.html', context)


def service_detail_view(request):
    context = {
        # Données pour banner_SD.html
        'banner_service': Banner.objects.filter(type='service_detail').first() or Banner.objects.first(),
        
        # Données pour service_det.html
        'service_details': ServiceDetail.objects.all()[:12],
        
        # Données pour JOIN_sD.html (call to action)
        'join_section': JoinSection.objects.first(),
        
        # Statistiques services
        'stats': {
            'total_services': ServiceDetail.objects.count(),
            'completed_projects': 320,
            'satisfaction_rate': '98%',
        }
    }
    return render(request, 'service-detail.html', context)


def spl_view(request):
    context = {
        # Données pour banner_SPL.html
        'banner_spl': Banner.objects.filter(type='spl').first() or Banner.objects.first(),
        
        # Données pour single_bloc_SPL.html
        'spl_blocks': SinglePageLanding.objects.all()[:6],
        
        # Données pour to_top.html (OBLIGATOIRE pour l'include)
        'to_top': ToTop.objects.first(),
        
        # Statistiques SPL
        'stats': {
            'total_blocks': SinglePageLanding.objects.count(),
            'visits': 12500,
            'conversion_rate': '15%',
        }
    }
    return render(request, 'single-blog-post-left-sidebar.html', context)


def spr_view(request):
    context = {
        # Données pour banner_SPR.html
        'banner_spr': Banner.objects.filter(type='spr').first() or Banner.objects.first(),
        
        # Données pour single_bloc_SPR.html
        'spr_blocks': SinglePageSPR.objects.all()[:6],
        
        # Données pour to_top.html
        'to_top': ToTop.objects.first(),
        
        # Statistiques SPR
        'stats': {
            'total_blocks': SinglePageSPR.objects.count(),
            'projects': 89,
            'success_rate': '97%',
        }
    }
    return render(request, 'single-post-right-sidebar.html', context)


def spw_view(request):
    context = {
        # Données pour banner_A.html
        'banner_a': Banner.objects.filter(type='about').first() or Banner.objects.first(),
        
        # Données pour single_bloc_S.html
        'single_blocks_s': SingleBlockS.objects.all()[:6],
        
        # Données pour to_top.html
        'to_top': ToTop.objects.first(),
        
        # Statistiques About
        'stats': {
            'total_blocks': SingleBlockS.objects.count(),
            'team_members': 25,
            'experience_years': 12,
        }
    }
    return render(request, 'single-blog-post-without-sidebar.html', context)


def team_view(request):
    context = {
        # Données pour banner_T.html
        'banner_team': Banner.objects.filter(type='team').first() or Banner.objects.first(),
        
        # Données pour team.html
        'team_members': TeamMember.objects.filter(active=True)[:12],
        
        # Données pour testimonials.html
        'testimonials': Testimonial.objects.filter(active=True)[:6],
        
        # Données pour to_top.html
        'to_top': ToTop.objects.first(),
        
        # Statistiques Team
        'stats': {
            'total_team': TeamMember.objects.count(),
            'departments': 5,
            'experience_avg': '8 ans',
        }
    }
    return render(request, 'team.html', context)





# --- PAGE À PROPOS ---
def about(request):
    # Récupération des sections
    about_info = AboutSection.objects.filter(is_active=True).first()
    about_features = AboutFeature.objects.filter(is_active=True).order_by('order')
    
    # Équipe et Récompenses
    team_members = TeamMember.objects.all()
    award_title = AwardSection.objects.filter(is_active=True).first()
    award_logos = AwardLogo.objects.all().order_by('order')

    context = {
        'title': 'About Us',
        'about': about_info,
        'features': about_features,
        'team': team_members,
        'award_title': award_title,
        'awards': award_logos,
    }
    return render(request, 'website/about-us.html', context)




# --- PAGES SERVICES ---
def services(request):
    banner = ServicesBanner.objects.filter(is_active=True).first()
    all_services = Service.objects.all()
    features = ServiceFeature.objects.filter(is_active=True).order_by('ordre')
    
    context = {
        'banner': banner,
        'services': all_services,
        'features': features,
    }
    return render(request, 'website/our-services.html', context)

def services_detail(request):
    # NOTE: Idéalement, cette vue devrait prendre un ID ou SLUG pour afficher UN service précis
    # Pour l'instant, on envoie juste des détails génériques
    details = service_detail.objects.all().order_by('order')
    return render(request, 'website/services-detail.html', {'details': details})

def pricing(request):
    # Récupère les plans et leurs fonctionnalités
    plans = PricingPlan.objects.all().order_by('order')
    return render(request, 'website/pricing.html', {'plans': plans})

# --- PAGE GALERIE / PORTFOLIO ---
def gallery(request):
    projects = PortfolioProject.objects.all()
    # On récupère les catégories distinctes pour le filtre HTML (optionnel)
    categories = [choice[0] for choice in PortfolioProject.CATEGORY_CHOICES]
    
    context = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'website/gallery.html', context)

def team(request):
    members = TeamMember.objects.all()
    return render(request, 'website/team.html', {'team': members})

# --- BLOG ---



def blog_detail_dynamic(request, slug):
    """ Cette vue remplace blog_left, blog_right, etc. """
    article = get_object_or_404(bloc_spr, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'article': article,
        'categories': categories,
        'tags': tags,
    }
    
    # Tu peux choisir ici quel template utiliser
    # Par défaut, prenons celui avec la sidebar à droite
    return render(request, 'website/single-blog-post-right-sidebar.html', context)

# Si tu veux garder tes anciennes URLs pour l'instant (mais elles seront statiques) :
def blog_left(request):
    return render(request, 'website/single-blog-post-left-sidebar.html')

def blog_right(request):
    return render(request, 'website/single-blog-post-right-sidebar.html')

def blog_no_sidebar(request):
    return render(request, 'website/single-blog-post-without-sidebar.html')