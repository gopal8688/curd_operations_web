from django.db import models
from multiselectfield import MultiSelectField



class ProductData(models.Model):
    product_id = models.IntegerField()
    product_choice =(
        ('l', 'lenovo'),
        ('d', 'dell'),
        ('h', 'hp'),
        ('s', 'sony'),
    )
    product_name = MultiSelectField(max_length=1,choices=product_choice )
    product_cost = models.IntegerField()
    choice_class =(
        ('h', 'high'),
        ('f', 'first'),
        ('m', 'medium'),
        ('l', 'low'),

    )
    product_class = MultiSelectField(max_length=50, choices=choice_class)
    color_choice = (
        ('b', 'black'),
        ('w', 'white'),
        ('g', 'grey'),
        ('r', 'red'),
    )
    product_color = MultiSelectField(max_length=50,choices=color_choice)
