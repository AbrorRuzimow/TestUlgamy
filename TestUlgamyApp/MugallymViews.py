from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.transaction import commit
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from TestUlgamyApp.MugallymForms import Create_Test_Forms, Create_Sorag_Forms, Sorag_Settings_Forms
from TestUlgamyApp.models import Sorag, Soraglar, Toparlar, Sorag_Kod, User_Student_Test, Student_Test


@login_required
def Dashboard(request):
    if request.user.user_type == '2':
        return render(request, 'Mugallym/Dashboard.html')
    else:
        raise Http404


@login_required
def Testler(request):
    if request.user.user_type == '2':
        models = Sorag.objects.filter(owner=request.user)
        context = {
            'models': models
        }
        return render(request, 'Mugallym/Test List.html', context)
    else:
        raise Http404


@login_required
def Test_create(request):
    if request.user.user_type == '2':
        if request.POST:
            forms = Create_Test_Forms(request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                model = Sorag()
                model.name = name
                model.owner = request.user
                model.save()
                return HttpResponseRedirect(reverse('Teste_soraglary_goshmak', args={model.id}))
        else:
            forms = Create_Test_Forms()
        context = {
            'forms': forms,
        }
        return render(request, 'Mugallym/All_Create.html', context)
    else:
        raise Http404


@login_required
def Teste_soraglary_goshmak(request, pk):
    if request.user.user_type == '2':
        if request.POST:
            models = None
            forms = Create_Sorag_Forms(request.POST, request.FILES)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                image = forms.cleaned_data['image']
                a = forms.cleaned_data['a']
                b = forms.cleaned_data['b']
                c = forms.cleaned_data['c']
                d = forms.cleaned_data['d']
                jogap = request.POST.get('test')
                model = Soraglar()
                model.sorag = Sorag.objects.get(id=pk)
                model.name = name
                model.surat = image
                model.a = a
                model.b = b
                model.c = c
                model.d = d
                model.success = jogap
                model.save()
                model_count = Soraglar.objects.filter(sorag=pk).count()
                count_model = Sorag.objects.get(id=pk)
                count_model.sorag_count = model_count
                count_model.sorag_min = model_count
                count_model.save()
                return HttpResponseRedirect(reverse('Teste_soraglary_goshmak', args={pk}))
        else:
            forms = Create_Sorag_Forms()
            models = Soraglar.objects.filter(sorag=pk).order_by('-date')
        context = {
            'forms': forms,
            'models': models
        }
        return render(request, 'Mugallym/Test Döretmek/Soraglar.html', context)
    else:
        raise Http404


@login_required
def Teste_soraglary_uytgetmek(request, pk, sorag_id):
    if request.user.user_type == '2':
        if request.POST:
            models = None
            model = None
            forms = Create_Sorag_Forms(request.POST, request.FILES)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                image = forms.cleaned_data['image']
                a = forms.cleaned_data['a']
                b = forms.cleaned_data['b']
                c = forms.cleaned_data['c']
                d = forms.cleaned_data['d']
                jogap = request.POST.get('test')
                model = Soraglar.objects.get(id=sorag_id)
                model.sorag = Sorag.objects.get(id=pk)
                model.name = name
                model.surat = image
                model.a = a
                model.b = b
                model.c = c
                model.d = d
                model.success = jogap
                model_count = Soraglar.objects.filter(sorag=pk).count()
                count_model = Sorag.objects.get(id=pk)
                count_model.sorag_count = model_count
                count_model.sorag_min = model_count
                count_model.save()
                model.save()
                return HttpResponseRedirect(
                    reverse('Teste_soraglary_uytgetmek', kwargs={'pk': pk, 'sorag_id': sorag_id}))
        else:
            forms = Create_Sorag_Forms()
            model = Soraglar.objects.get(id=sorag_id)
            forms.fields['name'].initial = model.name
            forms.fields['image'].initial = model.surat
            forms.fields['a'].initial = model.a
            forms.fields['b'].initial = model.b
            forms.fields['c'].initial = model.c
            forms.fields['d'].initial = model.d
            models = Soraglar.objects.filter(sorag=pk).order_by('date')
        context = {
            'forms': forms,
            'models': models,
            'navbar': model,
            'nav1': pk,
            'nav2': sorag_id
        }
        return render(request, 'Mugallym/Test Döretmek/Soraglar.html', context)
    else:
        raise Http404


@login_required
def Test_settings(request, pk):
    if request.user.user_type == '2':
        if request.POST:
            forms = Sorag_Settings_Forms(request.POST)
            if forms.is_valid():
                model = Sorag.objects.get(id=pk)
                model.b_5 = forms.cleaned_data['a_ball']
                model.b_4 = forms.cleaned_data['b_ball']
                model.b_3 = forms.cleaned_data['c_ball']
                model.sorag_min = forms.cleaned_data['wagt']
                model.yalnys = forms.cleaned_data['error']
                model.toparlar.clear()
                for data in forms.cleaned_data['topar']:
                    model.toparlar.add(data)
                model.save()
                return HttpResponseRedirect(reverse('Testler'))
        else:
            forms = Sorag_Settings_Forms()
            model = Sorag.objects.get(id=pk)
            forms.fields['wagt'].initial = model.sorag_min
            forms.fields['a_ball'].initial = model.b_5
            forms.fields['b_ball'].initial = model.b_4
            forms.fields['c_ball'].initial = model.b_3
            forms.fields['topar'].initial = model.toparlar.select_for_update()
            forms.fields['error'].initial = model.yalnys
        model_count = Soraglar.objects.filter(sorag=pk).count()
        context = {
            'forms': forms,
            'model_count': model_count,
        }
        return render(request, 'Mugallym/Test Settings.html', context)
    else:
        raise Http404


@login_required
def Topar_SMS(request, pk):
    if request.user.user_type == '2':
        model = Sorag.objects.get(id=pk)
        context = {
            'models': model
        }
        return render(request, 'Mugallym/Toparlar.html', context)
    else:
        raise Http404


@login_required
def Soraglar_SMS_Parol(request, sorag, topar):
    if request.user.user_type == '2':
        model = Sorag_Kod.objects.filter(sorag=sorag, sorag__toparlar=topar)
        context = {
            'models': model
        }
        return render(request, 'Mugallym/Parollar.html', context)
    else:
        raise Http404


@login_required
def Topar_Netije(request, pk):
    if request.user.user_type == '2':
        model = Sorag.objects.get(id=pk)
        context = {
            'models': model
        }
        return render(request, 'Mugallym/Toparlar(Netije).html', context)
    else:
        raise Http404


@login_required
def Student_Netijeler(request, sorag, topar):
    if request.user.user_type == '2':
        model = Student_Test.objects.filter(sorag=sorag, user__student_profile__topar=topar)
        context = {
            'models': model
        }
        return render(request, 'Mugallym/Netije Toparlar.html', context)
    else:
        raise Http404


def Show_Student_Test(request, sorag_id, user):
    if request.user.user_type == '2':
        models = User_Student_Test.objects.filter(user=user, sorag__sorag=sorag_id)
        user_page = request.GET.get('sorag', 1)
        p = Paginator(models, 1)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        context = {
            'page': page,
            'sorag_id': sorag_id,
            'user': user,
        }
        return render(request, 'Mugallym/Testi Görmek/Test.html', context)
    else:
        raise Http404
