from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from . import models
from postmarker.core import PostmarkClient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import add_message
from django.core.mail import send_mail


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    model = models.User
    success_url = "/logout/"
    form_class = UserCreationForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


# class JoinusView(LoginRequiredMixin, TemplateView):
#     template_name = "join-us.html"


class YourrequirementsView(LoginRequiredMixin, TemplateView):
    template_name = "your-requirements.html"


class JoinusView(CreateView):
    template_name = "join-us.html"
    model = models.Joinus
    fields = '__all__'
    success_url = '/join-us'

    def form_valid(self, form):
        msg = "Hello Admins,\n\nCongrates!! %s is interested to join us. To follow up please " \
              "contact %s.\n\n Thanks,\n-Social Boutique Team" % (form.cleaned_data["name"], form.cleaned_data['email'])
        send_mail(
            'Join Us [Social Boutique]',
            msg,
            'shivem05tiwari@gmail.com',
            [user.email for user in User.objects.filter(is_superuser=True)],
            fail_silently=False,
        )
        form.save()
        add_message(self.request, 25, "Response Recorded Successfully!")
        return super(JoinusView, self).form_valid(form)

    def form_invalid(self, form):
        add_message(self.request, 25, "Form is invalid! Please try again.")
        return super(JoinusView, self).form_invalid(form)


class YourrequirementsView(CreateView):
    template_name = "Your-requirements.html"
    model = models.Yourrequirements
    fields = ("name", "email", "message")
    success_url = '/your-requirements'

    def form_valid(self, form):
        msg = "Hello Admins,\n\nCongrates!! %s is interested to join us. To follow up please " \
              "contact %s.\n\n Thanks,\n-Social Boutique Team" % (form.cleaned_data["name"], form.cleaned_data['email'])
        send_mail(
            'Join Us [Social Boutique]',
            msg,
            'shivem05tiwari@gmail.com',
            [user.email for user in User.objects.filter(is_superuser=True)],
            fail_silently=False,
        )
        obj = form.save(commit=False)
        obj.save()
        requirement_ids = self.request.POST.getlist("requirement[]")
        for id in requirement_ids:
            obj.requirements.add(models.Requirement.objects.filter(id=id).first())

        add_message(self.request, 25, "Response Recorded Successfully!")
        return super(YourrequirementsView, self).form_valid(form)

    def form_invalid(self, form):
        add_message(self.request, 25, "Form is invalid! Please try again.")
        return super(YourrequirementsView, self).form_invalid(form)

    def get_requirements(self):
        return models.Requirement.objects.all()
