from django import forms

from TestUlgamyApp.models import Kafedra, Toparlar


class Mugallym_Goshmak_Forms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ulanyjynyň adyny giriziň'}),
        label='Ulanyjynyň ady', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Paroly giriziň'}), label='Parol',
        required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adyny giriziň'}), label='Ady',
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familýasyny giriziň'}),
        label='Familýasy', required=True)
    kafedra = forms.ModelChoiceField(queryset=Kafedra.objects.all(), empty_label='Kafedrany saýlaň',
                                     widget=forms.Select(attrs={'class': 'form-control'}), label='Kafedra',
                                     required=True)


class Mugallym_Uytgetmek_Forms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ulanyjynyň adyny giriziň'}),
        label='Ulanyjynyň ady', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Paroly giriziň'}), label='Parol',
        required=False)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adyny giriziň'}), label='Ady',
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familýasyny giriziň'}),
        label='Familýasy', required=True)
    kafedra = forms.ModelChoiceField(queryset=Kafedra.objects.all(), empty_label='Kafedrany saýlaň',
                                     widget=forms.Select(attrs={'class': 'form-control'}), label='Kafedra',
                                     required=True)


class Student_Goshmak_Forms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ulanyjynyň adyny giriziň'}),
        label='Ulanyjynyň ady', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Paroly giriziň'}), label='Parol',
        required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adyny giriziň'}), label='Ady',
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familýasyny giriziň'}),
        label='Familýasy', required=True)
    topar = forms.ModelChoiceField(queryset=Toparlar.objects.all(), empty_label='Topary saýlaň',
                                   widget=forms.Select(attrs={'class': 'form-control'}), label='Topar', required=True)


class Student_Uytgetmek_Forms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ulanyjynyň adyny giriziň'}),
        label='Ulanyjynyň ady', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Paroly giriziň'}), label='Parol',
        required=False)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adyny giriziň'}), label='Ady',
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familýasyny giriziň'}),
        label='Familýasy', required=True)
    topar = forms.ModelChoiceField(queryset=Toparlar.objects.all(), empty_label='Topary saýlaň',
                                   widget=forms.Select(attrs={'class': 'form-control'}), label='Topar', required=True)


class Topar_Goshmak_Forms(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Toparyň adyny giriziň'}),
        label='Toparyň ady')


class Kafedra_Goshmak_Forms(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kafedranyň adyny giriziň'}),
        label='Kafedranyň ady')
