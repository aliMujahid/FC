from .models import Categorie
from .forms import SearchForm

def navbar(request):
    form = SearchForm()
    categories = Categorie.objects.all()
    categ_dict = {}
    for category in categories:
        categ_dict[category] = category.subcategory_set.all()
    categories = categ_dict
    return {'categories':categories, 'form':form}
