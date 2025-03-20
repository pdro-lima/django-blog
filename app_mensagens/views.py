from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def inbox(request):
    received = Message.objects.filter(recipient=request.user)
    return render(request, 'messages_app/inbox.html', {'messages': received})

@login_required
def send_message(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        content = request.POST.get('content')
        # Aqui você pode implementar a lógica para validar o destinatário
        from django.contrib.auth.models import User
        recipient = User.objects.get(id=recipient_id)
        Message.objects.create(sender=request.user, recipient=recipient, content=content)
        return redirect('inbox')
    return render(request, 'messages_app/send_message.html')
