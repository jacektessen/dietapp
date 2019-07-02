from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    subject = request.POST['subject']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(message=message, user_id=user_id)
      if has_contacted:
        messages.error(request, 'Wysłałeś już dokładnie taką samą wiadomość')
        return redirect('contact_page')

    contact = Contact(subject=subject, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    send_mail(
      'DietApp kontakt od ' + name + '. Temat:' + subject + '',
      'Otrzymałeś wiadomość od ' + name + ' o treści: ' + message + '',
      'jacek.tessen2@gmail.com',
      ['jacek.tessen2@gmail.com'],
      fail_silently=False
    )

    messages.success(request, 'Twoja wiadomość została wysłana. Dziękuję!!!')
    return redirect('index')