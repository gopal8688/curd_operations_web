from django.shortcuts import render
from .models import ProductData
from .forms import InsertData, UpdateData, DeleteData
from django.http.response import HttpResponse


def main_page(request):
    return render(request, 'main_page.html')


def insert_view(request):
    if request.method == "POST":
        iform = InsertData(request.POST)
        if iform.is_valid():
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_cost = request.POST.get('product_cost')
            product_class = request.POST.get('product_class')
            product_color = request.POST.get('product_color')
            data = ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_class=product_class,
                product_color=product_color
            )
            data.save()
            iform = InsertData()
            return render(request, 'insertdata.html', {'iform': iform})
        else:
            return HttpResponse("Invalid Product Details")
    else:
        iform = InsertData()
        return render(request, 'insertdata.html', {'iform': iform})


def retrieve_view(request):
    pdata = ProductData.objects.all()
    return render(request, 'retrievedata.html', {'pdata': pdata})


def update_view(request):
    if request.method == "POST":
        uform = UpdateData(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')
            productdata = ProductData.objects.filter(product_id=product_id)
            if productdata:
                productdata.update(product_cost=product_cost)
                uform = UpdateData()
                return render(request, 'updatedata.html', {'uform': uform})
            else:
                return HttpResponse("User Invalid Data")
    else:
        uform = UpdateData()
        return render(request, 'updatedata.html', {'uform': uform})


def delete_view(request):
    if request.method == "POST":
        dform = DeleteData(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')
            proid = ProductData.objects.filter(product_id=product_id)
            if proid:
                proid.delete()
                return render(request, 'deletedata.html', {'dform': dform})
            else:
                return HttpResponse("Product Id Not Available")
        else:
            return HttpResponse("User Invalid Data")
    else:
        dform = DeleteData()
        return render(request, 'deletedata.html', {'dform': dform})
