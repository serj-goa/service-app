from django.db import models as m


class Service(m.Model):
    name = m.CharField(max_length=50)
    full_price = m.PositiveIntegerField()

    def __str__(self):
        return f'Service name: {self.name}, Full price: {self.full_price}'
