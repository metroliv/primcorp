from django.shortcuts import render
from .models import System, Service

def home(request):
    # Get the search query from the request
    query = request.GET.get('q', '').lower()
    
    # Get the filter value
    filter_value = request.GET.get('filter', 'all')
    
    # Filter systems and services based on search query and filter
    systems = System.objects.all()
    services = Service.objects.all()
    
    if query:
        systems = systems.filter(name__icontains=query)
        services = services.filter(title__icontains=query)
    
    if filter_value == 'systems':
        services = Service.objects.none()  # Hide services if only systems are filtered
    elif filter_value == 'services':
        systems = System.objects.none()  # Hide systems if only services are filtered
    
    # Check if there are no results
    no_results = not systems.exists() and not services.exists()

    return render(request, 'store/home.html', {
        'systems': systems,
        'services': services,
        'no_results': no_results  # Pass the flag to the template
    })

# View to display all services
def all_services(request):
    # Fetch all the services from the database
    services = Service.objects.all()
    # Pass the services to the template
    return render(request, 'store/services.html', {'services': services})
# Example views for custom system and contact us pages
def add_custom_system(request):
    return render(request, 'store/add_custom_system.html')

def contact_us(request):
    return render(request, 'store/contact_us.html')
