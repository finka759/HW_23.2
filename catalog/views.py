from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products.html', context)


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
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={"product": product})
