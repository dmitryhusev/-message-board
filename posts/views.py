from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"

#1 bad

#2

#3 omg