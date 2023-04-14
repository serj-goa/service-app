from django.core.validators import MaxValueValidator
from django.db import models as m


class Plan(m.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )

    plan_type = m.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = m.PositiveIntegerField(default=0, validators=[MaxValueValidator(100), ])

    def __str__(self):
        return f'Plan type: {self.plan_type}, Discount: {self.discount_percent}%'
