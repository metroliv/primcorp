from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

from store.models import Service
from django.http import Http404


def order_system(request, system_id=None):
    system = None
    if system_id:
        from store.models import System
        system = System.objects.get(id=system_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Set system/service for the order
            order = form.save(commit=False)
            if system:
                order.system = system
            order.save()
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'orders/order_system.html', {'form': form, 'system': system})

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})





# View to handle ordering a service
def order_service(request, id):
    # Get the service object by ID
    try:
        service = Service.objects.get(id=id)
    except Service.DoesNotExist:
        raise Http404("Service not found")

    # Handle the POST request for creating an order
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']
        quantity = int(request.POST['quantity'])

        # Create and save the new order
        order = Order.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            service=service,
            quantity=quantity
        )

        # Redirect to a confirmation page or service order details page
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'orders/order_service.html', {'service': service})

def order_confirmation(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise Http404("Order not found")

    return render(request, 'orders/order_confirmation.html', {'order': order})
