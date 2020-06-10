from django import forms
from multiselectfield import MultiSelectFormField



class InsertData(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Id'
            }
        )
    )
    product_choice = (
        ('l', 'lenovo'),
        ('d', 'dell'),
        ('h', 'hp'),
        ('s', 'sony'),
    )
    product_name = MultiSelectFormField(max_length=100,choices=product_choice)
    #     label="Enter Product Name",
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Product Name'
    #         }
    #     )
    # )
    product_cost = forms.CharField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
    choice_class = (
        ('h', 'high'),
        ('f', 'first'),
        ('m', 'medium'),
        ('l', 'low'),

    )
    product_class = MultiSelectFormField(max_length=100,choices=choice_class)
    #     label="Enter Product Class",
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Product Class'
    #         }
    #     )
    # )
    color_choice = (
        ('b', 'black'),
        ('w', 'white'),
        ('g', 'grey'),
        ('r', 'red'),
    )
    product_color = MultiSelectFormField(max_length=100,choices=color_choice)
    #     label="Enter Product Color",
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Product Color'
    #         }
    #     )
    # )


class UpdateData(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Id'
            }
        )
    )
    product_cost = forms.CharField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )


class DeleteData(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Id'
            }
        )
    )
