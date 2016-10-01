from django import forms

from .models import Drug, Clothes, TechAccessory, Book, ClothesUse, TechUse


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug


class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes


class TechAccessoryForm(forms.ModelForm):
    class Meta:
        model = TechAccessory


class BookForm(forms.ModelForm):
    class Meta:
        model = Book


class ClothesUseForm(forms.ModelForm):
    class Meta:
        model = ClothesUse


class TechUseForm(forms.ModelForm):
    class Meta:
        model = TechUse
