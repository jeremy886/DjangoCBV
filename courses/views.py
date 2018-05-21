from django.views.generic import View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Learner's Cafe.")
