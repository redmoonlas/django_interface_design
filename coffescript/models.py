from django.db import models

class Paragraph(models.Model) :
    order = models.IntegerField()

    def __unicode__(self):
        return u""


class Sentence(models.Model) :
    text = models.TextField()
    paragraph = models.ForeignKey(Paragraph)

    def __unicode__(self):
        return u""

