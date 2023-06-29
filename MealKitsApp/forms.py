# from django import forms
# from .models import *
#
#
# class ShippingAddressForm(forms.ModelForm):
#     address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
#
#     def __init__(self, *args, **kwargs):
#         super(ShippingAddressForm, self).__init__(*args, **kwargs)
#         #super().__init__()
#         self.fields['address'].label = "SHIPPING ADDRESS"
#         self.fields['city'].label = "CITY"
#         self.fields['zipcode'].label = "ZIP CODE"
#         self.fields['country'].label = "COUNTRY"
#         self.fields['shipping_time_start'].label = "PREFERRED SHIPPING TIME"
#         self.fields['shipping_time_end'].label = ""
#
#         for field in self.visible_fields():
#             field.field.widget.attrs["class"] = "form-control"
#
#     class Meta:
#         model = ShippingAddress
#         exclude = ("customer", "order", "date_added")
#
#
# class PaymentForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PaymentForm, self).__init__(*args, **kwargs)
#        # super().__init__()
#         for field in self.visible_fields():
#             field.field.widget.attrs["class"] = "form-control"
#
#     class Meta:
#         model = PaymentInfo
#         exclude = ("customer",)
#
#
# class RecipeForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(RecipeForm, self).__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             field.field.widget.attrs["class"] = "form-control"
#
#     class Meta:
#         model = Recipe
#         exclude = ("", )