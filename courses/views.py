from django.views.generic import (
    View, TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import StudyGroup


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


class StudyGroupListView(ListView):
    model = StudyGroup


class StudyGroupDetailView(DetailView):
    model = StudyGroup


class StudyGroupCreateView(CreateView):
    model = StudyGroup
    fields = ["name", "location", "host", "next_at"]


class StudyGroupUpdateView(UpdateView):
    model = StudyGroup
    fields = ["name", "location", "host", "next_at"]


class StudyGroupDeleteView(DeleteView):
    model = StudyGroup
    success_url = reverse_lazy("courses:list")

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(host=self.request.user)
        return self.model.objects.all()
