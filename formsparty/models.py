from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):
    name = models.CharField(max_length=127)

    def get_absolute_url(self):
        return reverse('formsparty:author-detail', kwargs={'pk': self.pk})
