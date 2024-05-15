from django.shortcuts import render

from catalog.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={"products": products})


def contacts(request):
    if request.method == 'POST':
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(name)
            print(phone)
            print(message)

            data = request.POST
            print(data)

    return render(request, 'contacts.html')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', context={"product": product})
