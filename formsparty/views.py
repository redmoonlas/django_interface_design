from django.views.generic import TemplateView


class Index(TemplateView):
    slug = 'index'
    template_name = 'formsparty/index.html'
