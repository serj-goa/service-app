from django.db import models as m

from clients.models import Client


class Subscription(m.Model):
    client = m.ForeignKey(Client, related_name='subscriptions', on_delete=m.PROTECT)
    service = m.ForeignKey('Service', related_name='subscriptions', on_delete=m.PROTECT)
    plan = m.ForeignKey('Plan', related_name='subscriptions', on_delete=m.PROTECT)

    def __str__(self):
        return f'{self.client}, {self.service}, {self.plan}'
