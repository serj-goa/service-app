from rest_framework import serializers as s

from services.models import Subscription


class SubscriptionSerializer(s.ModelSerializer):
    client_name = s.CharField(source='client.company_name')
    email = s.CharField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email', )
