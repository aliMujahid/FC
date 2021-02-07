from .models import Categorie

def navbar(request):
    categories = Categorie.objects.all()
    categ_dict = {}
    for category in categories:
        categ_dict[category] = category.subcategory_set.all()
    categories = categ_dict
    return {'categories':categories}
