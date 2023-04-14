from rest_framework import serializers as s

from services.models import Plan


class PlanSerializer(s.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
