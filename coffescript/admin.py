from django.contrib.admin import site, ModelAdmin
from coffescript.models import Paragraph, Sentence


site.register(Paragraph)
site.register(Sentence)
