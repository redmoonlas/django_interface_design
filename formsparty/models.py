from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):
    name = models.CharField(max_length=127, editable=True)

    def get_absolute_url(self):
        return reverse('formsparty:author-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self._meta.get_field_by_name('name')[0].editable = False
        super(Author, self).save(*args, **kwargs)