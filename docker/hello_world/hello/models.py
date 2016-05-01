from __future__ import unicode_literals

from django.db import models


class Quotes(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return '{} says {}'.format(self.author, self.text)
