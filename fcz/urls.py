from django.urls import path

from . import views

app_name = 'fcz'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:day>/<int:month>/<int:year>/<slug:product>/',\
                 views.product_detail, name='product_detail'),
    path('<slug:categ>/', views.category, name='category'),
    path('<slug:categ>/<slug:sub_categ>/', views.category, \
                                    name = 'sub_category'),
]
