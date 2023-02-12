from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from home.models import PostIt


class IndexView(generic.TemplateView):
    template_name = "home/index.html"


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            PostIt.objects.create(user=request.user, subject=subject, message=message)
            send_mail(
                subject,
                message,
                email,
                [email],
                fail_silently=False,)

        return render(request, 'home/index.html')
