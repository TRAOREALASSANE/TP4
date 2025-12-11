from django.db import models

# --- Gestion des Pages et Sections (Structure) ---

class Page(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la page")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    sections = models.ManyToManyField(
        'Section',
        through='PageSection',
        related_name='pages'
    )
    def __str__(self):
        return f"Page {self.nom} ({self.titre})"

class Section(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la section")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Section {self.nom} ({self.titre})"

class PageSection(models.Model):
    page = models.ForeignKey(
        'Page', on_delete=models.CASCADE, verbose_name="Page hôte"
    )
    section = models.ForeignKey(
        'Section', on_delete=models.CASCADE, verbose_name="Section incluse"
    )
    ordre = models.PositiveIntegerField(verbose_name="Ordre dans la page")

    class Meta:
        unique_together = (('page', 'ordre'), ('page', 'section'),)
        ordering = ['ordre']

    def __str__(self):
        return f"Ordre {self.ordre}: {self.section.nom} dans {self.page.nom}"

class Element(models.Model):
    section = models.ForeignKey(Section, related_name='elements', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100) 
    description = models.TextField()       
    icon = models.CharField(max_length=100, help_text="Nom du fichier (ex: 1.svg)")
    ordre = models.IntegerField(default=1)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return self.nom

# --- Menus ---

class Menu(models.Model):
    libelle = models.CharField(max_length=32, verbose_name="Nom du menu")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent menu", null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name="URL du menu")
    ordre = models.IntegerField(verbose_name="Ordre du menu")

    def __str__(self):
        return f"Menu {self.libelle} ({self.url})"


class BlogComment(models.Model):
    # Maintenant que BlogPost est juste au-dessus, cela va fonctionner
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comments"

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

class AboutSection(models.Model):
    section_title = models.CharField(max_length=100, default="About Us")
    main_title = models.CharField(max_length=200, default="Making transportation fast and safe")
    description = models.TextField()
    author_name = models.CharField(max_length=100, default="Tom Henders")
    author_title = models.CharField(max_length=100, default="CEO of Company")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return f"About Section - {self.section_title}"

class AboutFeature(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='about/icons/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = "About Feature"
        verbose_name_plural = "About Features"

    def __str__(self):
        return self.title


class PageBanner(models.Model):
    page_name = models.CharField(max_length=50, unique=True, default='accueil', verbose_name="Nom de la page (identifiant)")
    title = models.CharField(max_length=100, default="Our Gallery", verbose_name="Titre Principal")
    subtitle = models.CharField(max_length=100, default="faster deliveries", verbose_name="Sous-titre")
    image = models.ImageField(upload_to='banners/', blank=True, null=True, verbose_name="Image de fond")
    
    # AJOUTEZ CETTE LIGNE QUI MANQUAIT :
    is_active = models.BooleanField(default=True, verbose_name="Actif ?")

    def __str__(self):
        return f"Bannière: {self.page_name}"

class ServiceFeature(models.Model):
    # Il ne doit PAS y avoir de page_name ici !
    
    titre = models.CharField(max_length=100, verbose_name="Titre")
    description = models.CharField(max_length=255, verbose_name="Description courte")
    icon = models.ImageField(upload_to='features/', verbose_name="Icône")
    
    # C'est ce champ "is_active" que Django cherche et ne trouve pas
    is_active = models.BooleanField(default=True, verbose_name="Afficher ?")
    ordre = models.IntegerField(default=0, verbose_name="Ordre")

    class Meta:
        verbose_name = "Caractéristique (Service)"
        verbose_name_plural = "Caractéristiques (Services)"
        ordering = ['ordre']

    def __str__(self):
        return self.titre
    
class ServicesBanner(models.Model):
    # Titres par défaut basés sur votre HTML
    main_title = models.CharField(max_length=100, default="Our Services", verbose_name="Titre Principal")
    sub_title = models.CharField(max_length=100, default="what we do", verbose_name="Sous-titre")
    
    # Image pour remplacer le fond "banner-img-02"
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Image de fond")
    
    # Champ pour activer/désactiver
    is_active = models.BooleanField(default=True, verbose_name="Actif ?")

    class Meta:
        verbose_name = "Bannière Services"
        verbose_name_plural = "Bannière Services"

    def __str__(self):
        return self.main_title

class BlogDetailBanner(models.Model):
    # Les textes
    category = models.CharField(max_length=50, default="transportation", verbose_name="Catégorie (ex: transportation)")
    title = models.CharField(max_length=200, verbose_name="Titre de l'article")
    
    # Les métadonnées (Auteur, Date, etc.)
    author = models.CharField(max_length=50, default="John", verbose_name="Nom de l'auteur")
    publish_date = models.DateField(verbose_name="Date de publication")
    
    # Pour les chiffres (vous pouvez mettre du texte comme "5.5K" ou des chiffres)
    comments_count = models.CharField(max_length=10, default="3", verbose_name="Nombre de commentaires")
    views_count = models.CharField(max_length=10, default="5.5K", verbose_name="Nombre de vues")

    # Image de fond
    image = models.ImageField(upload_to='blog_details/', blank=True, null=True, verbose_name="Image de fond")
    
    is_active = models.BooleanField(default=True, verbose_name="Actif ?")

    class Meta:
        verbose_name = "Bannière Détail Blog"
        verbose_name_plural = "Bannière Détail Blog"

    def __str__(self):
        return self.title

class BlogPostHeader(models.Model):
    # Partie Textes
    category = models.CharField(max_length=100, default="Air Freight", verbose_name="Catégorie")
    title = models.CharField(max_length=255, verbose_name="Titre de l'article")
    
    # Partie Métadonnées (Auteur, Date, Chiffres)
    author_name = models.CharField(max_length=50, default="John", verbose_name="Auteur")
    publish_date = models.DateField(verbose_name="Date de publication")
    comments_count = models.IntegerField(default=3, verbose_name="Nb Commentaires")
    views_count = models.CharField(max_length=20, default="5.5K", verbose_name="Nb Vues (ex: 5.5K)")
    
    # Image de fond et activation
    image = models.ImageField(upload_to='blog_headers/', blank=True, null=True, verbose_name="Image de fond")
    is_active = models.BooleanField(default=True, verbose_name="Actif ?")

    class Meta:
        verbose_name = "En-tête Article Blog"
        verbose_name_plural = "En-têtes Article Blog"

    def __str__(self):
        return self.title

# 1. Pour gérer le titre et le sous-titre de la section
class AwardSection(models.Model):
    title = models.CharField(max_length=100, default="International awards 2024", verbose_name="Titre Principal")
    subtitle = models.CharField(max_length=100, default="Awards", verbose_name="Sous-titre")
    is_active = models.BooleanField(default=True, verbose_name="Afficher la section ?")

    class Meta:
        verbose_name = "Section Récompenses (Titres)"
        verbose_name_plural = "Section Récompenses (Titres)"

    def __str__(self):
        return self.title

# 2. Pour gérer les images (logos) individuellement
class AwardLogo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du client/prix (pour info)")
    image = models.ImageField(upload_to='awards/', verbose_name="Logo")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['order']
        verbose_name = "Logo Récompense"
        verbose_name_plural = "Logos Récompenses"

    def __str__(self):
        return self.name

# 1. Modèle pour les informations de contact (Côté gauche)
class ContactSection(models.Model):
    # Titres de gauche
    main_title = models.CharField(max_length=100, default="Talk or Meet with Us", verbose_name="Titre Principal (Gauche)")
    sub_title = models.CharField(max_length=100, default="Get In Touch", verbose_name="Sous-titre (Gauche)")
    
    # Coordonnées
    address_title = models.CharField(max_length=50, default="Get Us Here", verbose_name="Titre Adresse")
    address = models.TextField(default="1355 Market St, Suite 900\nSan Francisco, CA 94", verbose_name="Adresse")
    
    phone_title = models.CharField(max_length=50, default="Call Us", verbose_name="Titre Téléphone")
    phone = models.CharField(max_length=50, default="+1 123 456 7890", verbose_name="Numéro de téléphone")
    
    email_title = models.CharField(max_length=50, default="Write Us", verbose_name="Titre Email")
    email = models.EmailField(default="info@thisone.com", verbose_name="Email de contact")

    # Titres du formulaire (Côté droit)
    form_main_title = models.CharField(max_length=100, default="Let Us Know Here", verbose_name="Titre Formulaire")
    form_sub_title = models.CharField(max_length=100, default="Estimate Project", verbose_name="Sous-titre Formulaire")

    class Meta:
        verbose_name = "Section Contact (Infos)"
        verbose_name_plural = "Section Contact (Infos)"

    def __str__(self):
        return "Configuration de la section Contact"


# 2. Modèle pour enregistrer les messages reçus (Formulaire)
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    website = models.CharField(max_length=200, blank=True, null=True, verbose_name="Site Web")
    comment = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")

    class Meta:
        verbose_name = "Message Reçu"
        verbose_name_plural = "Messages Reçus"
        ordering = ['-created_at'] # Les plus récents en premier

    def __str__(self):
        return f"Message de {self.name}"

class FeatureSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='features/')
    
    # Pour l’accordéon
    accordion_title_1 = models.CharField(max_length=255)
    accordion_text_1 = models.TextField()

    accordion_title_2 = models.CharField(max_length=255)
    accordion_text_2 = models.TextField()

    accordion_title_3 = models.CharField(max_length=255)
    accordion_text_3 = models.TextField()

    def __str__(self):
        return self.title

class JoinUsSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)  # LET’s Connect
    button_text = models.CharField(max_length=50, default="GET A QUOTE")
    button_link = models.URLField(default="#")

    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('roadandtruck', 'Road & Truck'),
        ('airplane', 'Airplane'),
        ('maritime', 'Maritime'),
        ('videos', 'Videos'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.category})"

# TEAM
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# PRICING
class PricingPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    period = models.CharField(max_length=20, default="month")
    features = models.TextField()  # liste de features séparées par des virgules
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# BLOG
# Remplacer la classe BlogPost existante par celle-ci :

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    
    # CORRECTION : Ajout d'une valeur par défaut pour éviter l'erreur "non-nullable field"
    author = models.CharField(max_length=100, default="Admin")
    
    # CORRECTION : On autorise la date à être vide pour les anciens articles
    date = models.DateField(null=True, blank=True)
    
    # CORRECTION : On autorise l'image à être vide pour éviter les erreurs
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    
    content = models.TextField()
    views = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# TESTIMONIALS
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

    def __str__(self):
        return self.name

# CLIENTS
class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name

# VIDEO SECTION
class VideoSection(models.Model):
    video_url = models.URLField()

# website/models.py

class MapSection(models.Model):
    title = models.CharField(max_length=100, default="Notre Localisation", verbose_name="Titre (pour admin)")
    # Le lien src="..." de l'iframe
    map_url = models.TextField(verbose_name="Lien Google Maps (src)", help_text="Copiez uniquement le lien entre les guillemets de 'src' dans le code d'intégration Google.")
    height = models.IntegerField(default=400, verbose_name="Hauteur (px)")
    is_active = models.BooleanField(default=True, verbose_name="Afficher la carte ?")

    class Meta:
        verbose_name = "Configuration de la Carte"
        verbose_name_plural = "Configuration de la Carte"

    def __str__(self):
        return self.title

# website/models.py

class WhyChooseUs(models.Model):
    # Textes
    tagline = models.CharField(max_length=100, default="Why Choose us", verbose_name="Petit titre (Haut)")
    title = models.CharField(max_length=200, default="We are logistic improving our skills...", verbose_name="Titre Principal")
    description = models.TextField(verbose_name="Description")
    
    # Contact
    call_title = models.CharField(max_length=100, default="BOOK THROUGH CALL", verbose_name="Titre appel")
    phone_number = models.CharField(max_length=20, default="+1 234 567 8910", verbose_name="Numéro affiché")
    
    # Image de fond
    background_image = models.ImageField(upload_to='banners/', blank=True, null=True, verbose_name="Image de fond")
    
    is_active = models.BooleanField(default=True, verbose_name="Afficher la section ?")

    class Meta:
        verbose_name = "Section Pourquoi Nous Choisir"
        verbose_name_plural = "Section Pourquoi Nous Choisir"

    def __str__(self):
        return self.title


# 30/11.25


class PortfolioProject(models.Model):

    # Les catégories doivent correspondre aux classes CSS utilisées par ton filtre JS
    CATEGORY_CHOICES = [
        ('roadandtruck', 'Road & Truck'),
        ('airplane', 'Airplane'),
        ('maritime', 'Maritime'),
        ('videos', 'Videos'),
    ]

    title = models.CharField(max_length=200, verbose_name="Nom du projet")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Catégorie")
    image = models.ImageField(upload_to='portfolio/', verbose_name="Image")
    
    # Si c'est une vidéo, on met le lien ici. Sinon, on laisse vide.
    video_url = models.URLField(blank=True, null=True, verbose_name="Lien Vidéo (Vimeo/Youtube)")

    def __str__(self):
        return self.title

    # Une petite méthode pour savoir quel classe CSS utiliser pour le popup
    @property
    def popup_class(self):
        if self.category == 'videos' or self.video_url:
            return 'popup-vimeo' # ou popup-youtube selon ton JS
        return 'image-popup-vertical-fit'

    # Une méthode pour obtenir le bon lien (soit l'image HD, soit la vidéo)
    @property
    def link(self):
        if self.video_url:
            return self.video_url
        return self.image.url
    

class PricingPlan(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titre (ex: Basic)")
    price = models.IntegerField(verbose_name="Prix")
    currency = models.CharField(max_length=5, default="$", verbose_name="Devise")
    period = models.CharField(max_length=20, default="/month", verbose_name="Période")
    description = models.CharField(max_length=200, default="All plans include a 30 day trial!")
    
    # Ce champ permet de définir quel plan sera mis en avant (classe CSS "best")
    is_popular = models.BooleanField(default=False, verbose_name="Est-ce le plan populaire ?")
    
    # Pour l'ordre d'affichage (1, 2, 3...)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class PlanFeature(models.Model):
    # On pointe vers 'PricingPlan' et on garde 'features' comme related_name
    plan = models.ForeignKey('PricingPlan', related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=100, verbose_name="Texte de la fonctionnalité")

    def __str__(self):
        return self.text
    



class service_detail(models.Model):
    name = models.CharField(max_length=100)  # Ex: Basic, Popular
    price = models.IntegerField()            # Ex: 49
    currency = models.CharField(max_length=50, default="/month") # Ex: /month
    is_popular = models.BooleanField(default=False) # Pour la classe "best"
    
    # Pour l'ordre d'affichage (facultatif mais recommandé)
    order = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class service2(models.Model):
    # On pointe vers 'PricingPlan' et on change le related_name pour éviter le conflit
    plan = models.ForeignKey('PricingPlan', related_name='service_items', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Service(models.Model):
    title = models.CharField(max_length=100)         # Ex: Air Freight
    description = models.TextField()                 # Ex: Lorem ipsum dolor sit amet...
    image = models.ImageField(upload_to='services/') # L'image sera stockée dans media/services/
    
    # Un slug pour créer un lien unique (ex: /service/air-freight)
    slug = models.SlugField(unique=True, blank=True) 

    def __str__(self):
        return self.title


# blog/models.py

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

from django.db import models

class bloc_spl(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(unique=True) 
    image = models.ImageField(upload_to='blog_images/', verbose_name="Image Principale")
    content = models.TextField(verbose_name="Contenu de l'article")
    
    # SIMPLIFICATION ICI : Ce sont juste des champs texte maintenant
    category_name = models.CharField(max_length=100, default="Technologie", verbose_name="Nom de la catégorie")
    tags_string = models.CharField(max_length=200, help_text="Séparez les tags par des virgules", verbose_name="Tags (texte)")
    author_name = models.CharField(max_length=100, default="Admin", verbose_name="Nom de l'auteur")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class bloc_spr(models.Model):
    # 1. Infos principales de l'article
    title = models.CharField(max_length=255, verbose_name="Titre de l'article")
    slug = models.SlugField(unique=True, help_text="L'URL de l'article (ex: mon-super-article)")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Image Principale")
    content = models.TextField(verbose_name="Contenu de l'article")
    
    # 2. Infos de classification (Simplifiées en texte)
    category_name = models.CharField(max_length=100, default="Général", verbose_name="Nom de la catégorie")
    tags_string = models.CharField(max_length=200, help_text="Séparez les tags par des virgules (ex: Web, Design, SEO)", verbose_name="Liste des tags")

    # 3. Infos de l'auteur (Pour correspondre à votre HTML "About Author")
    author_name = models.CharField(max_length=100, default="Admin", verbose_name="Nom de l'auteur")
    author_image = models.ImageField(upload_to='author_images/', blank=True, null=True, verbose_name="Photo de l'auteur")
    
    # 4. Date
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")

    class Meta:
        ordering = ['-created_at'] # Affiche les articles du plus récent au plus ancien

    def __str__(self):
        return self.title







