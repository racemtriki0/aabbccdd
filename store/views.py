from django.shortcuts import render, redirect
from . models import Fournisseurr, Product
from . forms import SizeForm, ContactUsForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):

	context = {}

	return render(request, 'store/home.html', context)

def index3(request):
    list1 = Fournisseurr.objects.all()
    return render (request,'store/founisseurr.html',{'list1': list1})

def about(request):

	context = {}

	return render(request, 'store/about.html', context)


def serie(request):

	obj = Product.objects.filter(category = 'Serie')

	context = {
		'obj': obj,
	}

	return render(request, 'store/serie.html', context)


def mirale(request):

	obj = Product.objects.filter(category = 'Mirale')

	context = {
		'obj': obj,
	}

	return render(request, 'store/mirale.html', context)


def comptoir(request):

	obj = Product.objects.filter(category = 'Comptoir')

	context = {
		'obj': obj,
	}

	return render(request, 'store/comptoir.html', context)


def vitrine(request):

	obj = Product.objects.filter(category = 'Vitrine')

	context = {
		'obj': obj,
	}

	return render(request, 'store/vitrine.html', context)


def machine(request):

	obj = Product.objects.filter(category = 'Machine')

	context = {
		'obj': obj,
	}

	return render(request, 'store/machine.html', context)




def product_details(request, id):

    obj = Product.objects.get(pk=id)
    # if request.method == 'GET':
    # 	form = SizeForm()

    context = {
    	'obj': obj
    }

    return render(request, 'store/product_details.html', context)

def contact(request):

	form = ContactUsForm()

	if request.method == 'POST':

		form = ContactUsForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			contact = form.cleaned_data.get('contact')
			subject = form.cleaned_data.get('subject')
			message = form.cleaned_data.get('message')

			subject = f'tounsi refrigeration - {subject}'
			send_message = f'Name: {name} \n'
			send_message += f'Phone Number: {contact} \n'
			send_message += f'Email: {email} \n\n'
			send_message += message
			email_from = settings.EMAIL_HOST_USER
			email_to = ['trikiracem0@gmail.com']

			print('before email')

			# print(message)

			send_mail(
				subject,
				send_message,
				email_from,
				email_to,
				fail_silently=False,
			)

		return redirect('home')

	context = {
		'form': form
	}

	return render(request, 'store/contact.html', context)
