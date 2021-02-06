from .models import Categorie

def navbar(request):
    categories = Categorie.objects.all()
    return {'categories':categories}
