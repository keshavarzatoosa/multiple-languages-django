from django.db import models
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    title = models.CharField(_('title'), max_length=90)
    description = models.TextField(_('description'))
    date = models.DateField(_('date'))
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
