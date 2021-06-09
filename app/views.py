from django.shortcuts import render
from . models import customer, product
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse


def index(request):
    return render(request, 'app/index.html')


def saveCustomers(request):
    if request.method == "POST":
        firstName1 = request.POST['fn']
        lastName1 = request.POST['ln']
        contactNo1 = request.POST['cn']
        pincode1 = request.POST['pin']
        customer(firstName=firstName1, lastName=lastName1,
                 contactNo=contactNo1, pincode=pincode1).save()
        return render(request, 'app/index.html')
    else:
        return HttpResponse("<h1>404 - Not found</h1>")


def saveProduct(request):
    if request.method == "POST":
        ProductName = request.POST['pn']
        Price = request.POST['price']
        product(productName=ProductName, productPrice=Price).save()
        return render(request, 'app/index.html')
    return render(request, 'app/product.html')


def newOrderForm(request):
    cResult = customer.objects.all()
    PResult = product.objects.all()
    return render(request, 'app/newOrder.html', {"ShowCustomer": cResult, "Showproduct": PResult})
