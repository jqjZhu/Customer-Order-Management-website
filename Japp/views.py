from django.shortcuts import render
from .models import Customer, Product, Order


# Create your views here.

def homepage(request):
    customer = Customer.objects.all()
    c_count = customer.count()

    order = Order.objects.all()
    o_count = order.count()

    order_p_count = Order.objects.filter(status='Pending').count()
    order_d_count = Order.objects.filter(status='Delivered').count()
    order_o_count = Order.objects.filter(status='Out for delivery').count()

    c = 0
    last_five = []
    for i in reversed(order):
        if c < 5:
            last_five.append(i)
            c += 1
        else:
            break

    context = {
        'customer': customer,
        'c_count': c_count,
        'o_count': o_count,
        'order_p_count': order_p_count,
        'order_d_count': order_d_count,
        'order_o_count': order_o_count,
        'last_five': last_five
    }
    return render(request, 'Japp/index.html', context)


def create(request):

    context = {}
    return render(request, 'Japp/create.html', context)