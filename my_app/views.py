from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from my_app.models import Product


# Create your views here.

@login_required(login_url='/admin/login')
def products_list(request):
    # return HttpResponse('Olá mundo!!')
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})
