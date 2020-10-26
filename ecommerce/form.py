
from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
	class Meta:
		model = Product_bought
		fields = '__all__'

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
