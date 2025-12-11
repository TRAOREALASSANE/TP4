from .models import PageBanner

def page_banners(request):
    """
    Rend les bannières disponibles dans tous les templates
    """
    banners = {}
    for banner in PageBanner.objects.filter(is_active=True):
        banners[banner.page] = banner
    
    return {'page_banners': banners}