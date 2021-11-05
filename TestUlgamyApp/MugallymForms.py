from django import forms

from TestUlgamyApp.models import Toparlar


class Create_Test_Forms(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Testiň adyny giriziň'}),label='Testiň ady')

class Create_Sorag_Forms(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control text-muted text-center','placeholder':'Soragyň adyny giriziň'}),label='Soragy ady')
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control select_media','id':'exampleInputFile'}),label='Surat giriziň',required=False)
    a = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-muted','placeholder':'A jogaby giriziň'}),label='A jogap')
    b = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-muted', 'placeholder': 'B jogaby giriziň'}),label='B jogap')
    c = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-muted', 'placeholder': 'C jogaby giriziň'}),label='C jogap',required=False)
    d = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-muted', 'placeholder': 'D jogaby giriziň'}),label='D jogap',required=False)

class Sorag_Settings_Forms(forms.Form):
    wagt = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Wagt')
    a_ball = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='5 baha almak üçin')
    b_ball = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='4 baha almak üçin')
    c_ball = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='3 baha almak üçin')
    topar = forms.ModelMultipleChoiceField(queryset=Toparlar.objects.all(),widget=forms.SelectMultiple(attrs={'class':'select2 multiselectfull','data-placeholder':'Toparlary saýlaň'}),label='Toparlar')
    error = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Ýalňyşmak mümkinçiligi')
