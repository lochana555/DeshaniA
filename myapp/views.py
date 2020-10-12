from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductsForm


def index(request):
    return render(request,"index.html")


def load_form(request):
    form=ProductsForm
    return render(request,"index2.html",{'form':form})


def add(request):
    form=ProductsForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    products=Products.objects.all
    return render(request,'show.html',{'products':products})


def edit(request,id):
    products=Products.objects.get(id=id)
    return render(request,'edit.html',{'products':products})


def update(request,id):
    products=Products.objects.get(id=id)
    form=ProductsForm(request.POST,instance=products)
    form.save()
    return redirect('/show')


def delete(request,id):
    products = Products.objects.get(id=id)
    products.delete()
    return redirect('/show')


def search(request):
    given_name=request.POST['name']
    products = Products.objects.filter(pname__icontains=given_name)
    return render(request,'show.html',{'products':products})
