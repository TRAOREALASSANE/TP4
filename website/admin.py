from django.contrib import admin
from .models import *

# --- Structure & Menus ---
admin.site.register(Page)
admin.site.register(Section)
admin.site.register(PageSection)
admin.site.register(Element)
admin.site.register(Menu)

# --- Blog ---
admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(BlogPostHeader)
admin.site.register(BlogDetailBanner)

# --- Sections À Propos & Services ---
admin.site.register(AboutSection)
admin.site.register(AboutFeature)
admin.site.register(ServiceFeature)
admin.site.register(ServicesBanner)
admin.site.register(WhyChooseUs)
admin.site.register(FeatureSection)

# --- Contact & Localisation ---
admin.site.register(ContactSection)
admin.site.register(ContactMessage)
admin.site.register(MapSection)
admin.site.register(JoinUsSection)

# --- Portfolio, Team, Pricing ---
admin.site.register(PortfolioItem)
admin.site.register(TeamMember)
admin.site.register(PricingPlan)
admin.site.register(Client)
admin.site.register(Testimonial)

# --- Media & Autres ---
admin.site.register(PageBanner)
admin.site.register(VideoSection)
admin.site.register(AwardSection)
admin.site.register(AwardLogo)




@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')
    list_filter = ('category',)