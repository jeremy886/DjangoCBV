from django.views.generic import View, TemplateView
from django.http import HttpResponse


class HelloView(View):
    def get(self, request):
        return HttpResponse("Welcome to Learner's Cafe.")


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["motd"] = "Don't forget to check out new study groups!"
        context["new_groups"] = 5
        return context
