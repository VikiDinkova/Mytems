from django import forms

from .models import Drug, Clothes, TechAccessory, Book, ClothesUse, TechUse


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'


class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'


class TechAccessoryForm(forms.ModelForm):
    class Meta:
        model = TechAccessory
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ClothesUseForm(forms.ModelForm):
    class Meta:
        model = ClothesUse
        fields = '__all__'


class TechUseForm(forms.ModelForm):
    class Meta:
        model = TechUse
        fields = '__all__'
