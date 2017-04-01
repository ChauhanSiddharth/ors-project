from .models import Orders,Orders_Item
from django import forms

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('course_Id','member_id','Total_Amount')

class Order_ItemForm(forms.ModelForm):
    class Meta:
        model = Orders_Item
        fields = ('transaction_id','order_item_id')