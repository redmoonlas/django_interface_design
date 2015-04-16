from django.views.generic import TemplateView


class Intro(TemplateView):
    slug = 'intro'
    template_name = 'coffeescript/intro.html'