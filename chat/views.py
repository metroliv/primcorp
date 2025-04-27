from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def index(request):
    # Retrieve the latest 10 messages to show in the chat history (can be paginated as well)
    messages = Message.objects.all().order_by('-timestamp')[:10]
    
    # Render the chat page and pass the messages to the template
    return render(request, 'chat.html', {'messages': messages})
