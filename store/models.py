from django.db import models

# Create your models here.

class Size(models.Model):

	size = models.CharField(max_length=30)

	def __str__(self):
		return self.size

class OtherImages(models.Model):

	other_image = models.ImageField(upload_to='Store')

class Fournisseurr(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+str(self.telephone)

class Product(models.Model):
	category_choice = {
		('Serie', 'Serie'),
		('Mirale', 'Mirale'),
		('Comptoir', 'Comptoir'),
		('Vitrine', 'Vitrine'),
		('Machine', 'Machine')
	}

	category = models.CharField(max_length=20, choices=category_choice, default='serie')
	size = models.ManyToManyField(Size)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=300)
	price = models.IntegerField()
	image = models.ImageField(upload_to='Store')
	other_image = models.ManyToManyField(OtherImages, blank=True)

	def __str__(self):
		return self.title

		