from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from TestUlgamyApp.Admin_Forms import *
from TestUlgamyApp.models import Users


@login_required
def Dashboard(request):
    if request.user.user_type == '1':
        return render(request, 'Administrator/Dashboard.html')
    else:
        raise Http404


@login_required
def Mugallym_List(request):
    if request.user.user_type == '1':
        models = Users.objects.filter(user_type=2)
        user_page = request.GET.get('sahypa', 1)
        user_search = request.GET.get('search')
        p = Paginator(models, 13)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        if user_search:
            page = Users.objects.filter(
                Q(user_type=2, username__icontains=user_search) | Q(user_type=2, first_name__icontains=user_search) | Q(
                    user_type=2, last_name__icontains=user_search))
        context = {
            'page': page,
        }
        return render(request, 'Administrator/Mugallym List.html', context)
    else:
        raise Http404


@login_required
def Mugallym_goshmak(request):
    if request.user.user_type == '1':
        if request.POST:
            forms = Mugallym_Goshmak_Forms(request.POST)
            if forms.is_valid():
                try:
                    username = forms.cleaned_data['username']
                    password = forms.cleaned_data['password']
                    first_name = forms.cleaned_data['first_name']
                    last_name = forms.cleaned_data['last_name']
                    kafedra = forms.cleaned_data['kafedra']
                    model = Users.objects.create_user(username=username, password=password, first_name=first_name,
                                                      last_name=last_name, user_type=2)
                    model.mugallym_profile.kafedra = kafedra
                    model.save()
                except:
                    username = forms.cleaned_data['username']
                    models = Users.objects.filter(username=username)
                    if models:
                        messages.error(request, 'Ulanyjynyň ady öz bar.Siz başga ulanyjynyň adyny ýazyň')
                return HttpResponseRedirect(reverse('Mugallym_List'))
        else:
            forms = Mugallym_Goshmak_Forms()
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Create.html', context)
    else:
        raise Http404


@login_required
def Mugallym_uytgetmek(request, pk):
    if request.user.user_type == '1':
        if request.POST:
            forms = Mugallym_Uytgetmek_Forms(request.POST)
            if forms.is_valid():
                username = forms.cleaned_data['username']
                password = forms.cleaned_data['password']
                first_name = forms.cleaned_data['first_name']
                last_name = forms.cleaned_data['last_name']
                kafedra = forms.cleaned_data['kafedra']
                model = Users.objects.get(id=pk)
                model.username = username
                model.first_name = first_name
                model.last_name = last_name
                if password:
                    model.set_password(password)
                model.mugallym_profile.kafedra = kafedra
                model.save()
                return HttpResponseRedirect(reverse('Mugallym_List'))
        else:
            models = Users.objects.get(id=pk)
            forms = Mugallym_Uytgetmek_Forms()
            forms.fields['username'].initial = models.username
            forms.fields['first_name'].initial = models.first_name
            forms.fields['last_name'].initial = models.last_name
            forms.fields['kafedra'].initial = models.mugallym_profile.kafedra
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Update.html', context)
    else:
        raise Http404


@login_required
def Mugallym_delete(request, pk):
    if request.user.user_type == '1':
        model = Users.objects.get(id=pk)
        model.delete()
        return HttpResponseRedirect(reverse('Mugallym_List'))
    else:
        raise Http404


@login_required
def Student_List(request):
    if request.user.user_type == '1':
        models = Users.objects.filter(user_type=3)
        user_page = request.GET.get('sahypa', 1)
        user_search = request.GET.get('search')
        p = Paginator(models, 13)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        if user_search:
            page = Users.objects.filter(
                Q(user_type=3, username__icontains=user_search) | Q(user_type=3, first_name__icontains=user_search) | Q(
                    user_type=3, last_name__icontains=user_search))
        context = {
            'page': page,
        }
        return render(request, 'Administrator/Student List.html', context)
    else:
        raise Http404


@login_required
def Student_goshmak(request):
    if request.user.user_type == '1':
        if request.POST:
            forms = Student_Goshmak_Forms(request.POST)
            if forms.is_valid():
                try:
                    username = forms.cleaned_data['username']
                    password = forms.cleaned_data['password']
                    first_name = forms.cleaned_data['first_name']
                    last_name = forms.cleaned_data['last_name']
                    topar = forms.cleaned_data['topar']
                    model = Users.objects.create_user(username=username, password=password, first_name=first_name,
                                                      last_name=last_name, user_type=3)
                    model.student_profile.topar = topar
                    model.save()
                except:
                    username = forms.cleaned_data['username']
                    models = Users.objects.filter(username=username)
                    if models:
                        messages.error(request, 'Ulanyjynyň ady öz bar.Siz başga ulanyjynyň adyny ýazyň')
                return HttpResponseRedirect(reverse('Student_List'))
        else:
            forms = Student_Goshmak_Forms()
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Create.html', context)
    else:
        raise Http404


@login_required
def Student_uytgetmek(request, pk):
    if request.user.user_type == '1':
        if request.POST:
            forms = Student_Uytgetmek_Forms(request.POST)
            if forms.is_valid():
                username = forms.cleaned_data['username']
                password = forms.cleaned_data['password']
                first_name = forms.cleaned_data['first_name']
                last_name = forms.cleaned_data['last_name']
                topar = forms.cleaned_data['topar']
                model = Users.objects.get(id=pk)
                model.username = username
                model.first_name = first_name
                model.last_name = last_name
                if password:
                    model.set_password(password)
                model.student_profile.topar = topar
                model.save()
                return HttpResponseRedirect(reverse('Student_List'))
        else:
            models = Users.objects.get(id=pk)
            forms = Student_Uytgetmek_Forms()
            forms.fields['username'].initial = models.username
            forms.fields['first_name'].initial = models.first_name
            forms.fields['last_name'].initial = models.last_name
            try:
                forms.fields['topar'].initial = models.student_profile.topar
            except:
                forms.fields['topar'].initial = None
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Update.html', context)
    else:
        raise Http404


@login_required
def Student_delete(request, pk):
    if request.user.user_type == '1':
        model = Users.objects.get(id=pk)
        model.delete()
        return HttpResponseRedirect(reverse('Student_List'))
    else:
        raise Http404


@login_required
def All_Toparlar(request):
    if request.user.user_type == '1':
        models = Toparlar.objects.all()
        user_page = request.GET.get('sahypa', 1)
        user_search = request.GET.get('search')
        p = Paginator(models, 13)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        if user_search:
            page = Toparlar.objects.filter(Q(name__icontains=user_search))
        context = {
            'page': page,
        }
        return render(request, 'Administrator/Toparlar.html', context)
    else:
        raise Http404


@login_required
def Topar_create(request):
    if request.user.user_type == '1':
        if request.POST:
            forms = Topar_Goshmak_Forms(request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                model = Toparlar()
                model.name = name
                model.save()
                return HttpResponseRedirect(reverse('All_Toparlar'))
        else:
            forms = Topar_Goshmak_Forms()
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Create.html', context)
    else:
        raise Http404


@login_required()
def Topar_update(request, pk):
    if request.user.user_type == '1':
        model = Toparlar.objects.get(id=pk)
        if request.POST:
            forms = Topar_Goshmak_Forms(request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                model.name = name
                model.save()
                return HttpResponseRedirect(reverse('All_Toparlar'))
        else:
            forms = Topar_Goshmak_Forms()
            forms.fields['name'].initial = model.name
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Update.html', context)
    else:
        raise Http404


@login_required()
def Topar_delete(request, pk):
    if request.user.user_type == '1':
        model = Toparlar.objects.get(id=pk)
        model.delete()
        return HttpResponseRedirect(reverse('All_Toparlar'))
    else:
        raise Http404


@login_required
def All_Kafedra(request):
    if request.user.user_type == '1':
        models = Kafedra.objects.all()
        user_page = request.GET.get('sahypa', 1)
        user_search = request.GET.get('search')
        p = Paginator(models, 13)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        if user_search:
            page = Kafedra.objects.filter(Q(name__icontains=user_search))
        context = {
            'page': page,
        }
        return render(request, 'Administrator/Kafedralar.html', context)
    else:
        raise Http404


@login_required
def Kafedra_create(request):
    if request.user.user_type == '1':
        if request.POST:
            forms = Kafedra_Goshmak_Forms(request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                model = Kafedra()
                model.name = name
                model.save()
                return HttpResponseRedirect(reverse('All_Kafedra'))
        else:
            forms = Kafedra_Goshmak_Forms()
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Create.html', context)
    else:
        raise Http404


@login_required()
def Kafedra_update(request, pk):
    if request.user.user_type == '1':
        model = Kafedra.objects.get(id=pk)
        if request.POST:
            forms = Kafedra_Goshmak_Forms(request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                model.name = name
                model.save()
                return HttpResponseRedirect(reverse('All_Kafedra'))
        else:
            forms = Kafedra_Goshmak_Forms()
            forms.fields['name'].initial = model.name
        context = {
            'forms': forms
        }
        return render(request, 'Administrator/All_Update.html', context)
    else:
        raise Http404


@login_required()
def Kafedra_delete(request, pk):
    if request.user.user_type == '1':
        model = Kafedra.objects.get(id=pk)
        model.delete()
        return HttpResponseRedirect(reverse('All_Kafedra'))
    else:
        raise Http404
