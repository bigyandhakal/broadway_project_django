from organizations.models import Category
from job_portal.settings import MEDIA_URL

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories, 'MEDIA_URL': MEDIA_URL}