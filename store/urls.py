from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('fournisseurr', views.index3, name='fournisseurr'),
	path('contact', views.contact, name='contact'),
	path('serie', views.serie, name='serie'),
	path('mirale', views.mirale, name='mirale'),
	path('comptoir', views.comptoir, name='comptoir'),
	path('vitrine', views.vitrine, name='vitrine'),
	path('machine', views.machine, name='machine'),
	path('product_details/<int:id>', views.product_details, name='product_details'),
]