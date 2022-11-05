
from dataclasses import field
from tkinter import Widget
from tkinter.tix import Select
from django import forms
from django.forms import NumberInput,Textarea,TextInput

from widecity_shopping.models import Banners, Category, Products, Subcategory

class DateInput(forms.DateInput):
    input_type = 'date'
    
class add_product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
                    'name', 
                    'description',
                    'specification',
                    'stock_available',
                    'is_trusted', 
                    'available_status', 
                    'manufacturing_date',
                    'price',
                    'category', 
                    'image_1', 
                    'image_2',
                    'image_3',
                    'image_4',
                ]
        widgets = {
            'manufacturing_date':DateInput(),
            'name':TextInput(attrs={'style':'width:40%;border:1px solid grey;border-radius:10px;padding:1%;font-weight:bold;','onmouseover':'(this.placeholder = "Enter the Product Name")','onmouseout':'(this.placeholder = "")'}),
            'description':Textarea(attrs={'style':'width:40%;height:200px;border:2px solid grey;border-radius:10px;padding:10px;font-weight:bold;','onmouseover':'(this.placeholder = "write a short description about the product...")','onmouseout':'(this.placeholder = "")'}),
            'specification':Textarea(attrs={'style':'width:40%;border:2px solid grey;border-radius:10px;;padding:5%;font-weight:bold;','onmouseover':'(this.placeholder = "Please Provide the Specification of the current product...")','onmouseout':'(this.placeholder = "")'}),
            'stock_available':NumberInput(attrs={'style':'width:40%;border:2px solid grey;border-radius:10px;;padding:1%;font-weight:bold;','onmouseover':'(this.placeholder = "Enter the total stiock available")','onmouseout':'(this.placeholder = "")'}),
            'price':NumberInput(attrs={'style':'width:40%;border:2px solid grey;border-radius:10px;;padding:10px;font-weight:bold;','min':1,'max':10000,'onmouseover':'(this.placeholder = "Enter the price of the product")','onmouseout':'(this.placeholder = "")'}),
        }

class add_product_images_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = [ 
                    'image_1', 
                    'image_2',
                    'image_3',
                    'image_4',
                ]


class edit_banner(forms.ModelForm):
    class Meta:
        model = Banners
        fields = ['heading', 'description', 'image']


# class company_info(forms.ModelForm):
#     class Meta:
#         model = Company_Info
#         fields = ['company_logo', 'company_name', 'company_description']


class add_category(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image']



# uiyuiyuiyghug

from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)
