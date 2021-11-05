import datetime
import random
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from TestUlgamyApp.models import Sorag, Sorag_Kod, Users, Student_Test, Soraglar, User_Student_Test


@login_required
def StudentDashboard(request):
    if request.user.user_type == '3':
        return render(request, 'Student/Dashboard.html')
    else:
        raise Http404


@login_required
def Tests(request):
    if request.user.user_type == '3':
        models = []
        try:
            model = Sorag.objects.filter(toparlar=request.user.student_profile.topar)
            for data in model:
                try:
                    model2 = Student_Test.objects.get(user=request.user, sorag=data.id)
                except:
                    model2 = None
                if model2:
                    continue
                else:
                    models.append(data)
        except:
            models = None
        context = {
            'models': models
        }
        return render(request, 'Student/Testler.html', context)
    else:
        raise Http404


@login_required
def Parol_doret(request, test_id, student_id):
    if request.user.user_type == '3':
        try:
            models = Sorag_Kod.objects.get(user=student_id, sorag=test_id)
        except:
            models = None
        if models:
            models.user = Users.objects.get(id=student_id)
            models.sorag = Sorag.objects.get(id=test_id)
            import math, random
            kod = ''
            number = '0123456789'
            for i in range(6):
                kod += number[math.floor(random.random() * 10)]
            models.kod = int(kod)
            models.save()
            return HttpResponseRedirect(reverse('Parol', kwargs={'parol_id': models.id}))
        else:
            model = Sorag_Kod()
            user = Users.objects.get(id=student_id)
            model.user = user
            sorag = Sorag.objects.get(id=test_id)
            model.sorag = sorag
            import math, random
            kod = ''
            number = '0123456789'
            for i in range(6):
                kod += number[math.floor(random.random() * 10)]
            model.kod = int(kod)
            model.save()
            return HttpResponseRedirect(reverse('Parol', kwargs={'parol_id': model.id}))
    else:
        raise Http404


@login_required
def Parol(request, parol_id):
    if request.user.user_type == '3':
        if request.POST:
            password = request.POST.get('password')
            kod = Sorag_Kod.objects.get(id=parol_id)
            if str(password) == str(kod.kod):
                model = Sorag_Kod.objects.get(id=parol_id)
                model.ip = request.META.get('REMOTE_ADDR')
                model.start = True
                model.save()
                return HttpResponseRedirect(
                    reverse('Random_Test', kwargs={'sorag_id': kod.sorag.id, 'kod_id': parol_id}))
            else:
                messages.error(request, 'Girizen parolyňyz ýalňyş')
                return HttpResponseRedirect(reverse('Parol', args={parol_id}))
        return render(request, 'Student/Test üçin/Teste girmek üçin parol.html')
    else:
        raise Http404


def Random_Test(request, sorag_id, kod_id):
    if request.user.user_type == '3':
        try:
            old_register_model = Student_Test.objects.get(sorag=sorag_id, user=request.user)
            messages.error(request, 'Siz bu testi öň tabşyrdyňyz!')
            return HttpResponseRedirect(reverse('Parol', args={kod_id}))
        except:
            registrasiya = Student_Test()
            sorag = Sorag.objects.get(id=sorag_id)
            registrasiya.sorag = sorag
            student_user = Users.objects.get(id=request.user.id)
            registrasiya.user = student_user
            date1 = datetime.datetime.now()
            date2 = timedelta(minutes=registrasiya.sorag.sorag_min)
            date = date1 + date2
            registrasiya.e_max_date = date
            registrasiya.save()
            models = list(Soraglar.objects.filter(sorag=sorag_id))
            models_count = Soraglar.objects.filter(sorag=sorag_id).count()
            model_data = random.sample(models, models_count)
            for data in model_data:
                model = User_Student_Test()
                model.user = request.user
                model.sorag = data
                model.save()
        return HttpResponseRedirect(reverse('Test', kwargs={'sorag_id': registrasiya.id}))
    else:
        raise Http404


@login_required
def Test(request, sorag_id):
    if request.user.user_type == '3':
        model = Student_Test.objects.get(id=sorag_id)
        date_now = datetime.datetime.now()
        date = (model.e_max_date - date_now).seconds
        if date_now >= model.e_max_date:
            model.end_test = True
            model.e_date = datetime.datetime.now()
            model.save()
        if model.end_test:
            return HttpResponseRedirect(reverse('Netijeler'))
        models = User_Student_Test.objects.filter(user=request.user, sorag__sorag=model.sorag.id)
        user_page = request.GET.get('sorag', 1)
        p = Paginator(models, 1)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        page_list = page.number * 100 / p.count
        if request.POST:
            if request.POST.get('next_page') == 'Finish':
                succes = User_Student_Test.objects.get(id=page.object_list)
                if request.POST.get('test') != None:
                    if succes.jogap_berdi == None:
                        if succes.sorag.success == request.POST.get('test'):
                            model.d_j_b_s_count += 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                        else:
                            model.y_j_b_s_count += 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                    else:
                        if succes.sorag.success == succes.jogap_berdi and succes.sorag.success == request.POST.get(
                                'test'):
                            pass
                        elif succes.sorag.success != succes.jogap_berdi and succes.sorag.success == request.POST.get(
                                'test'):
                            model.y_j_b_s_count -= 1
                            model.d_j_b_s_count += 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                        elif succes.sorag.success == succes.jogap_berdi and succes.sorag.success != request.POST.get(
                                'test'):
                            model.y_j_b_s_count += 1
                            model.d_j_b_s_count -= 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                        elif succes.sorag.success != succes.jogap_berdi and succes.sorag.success != request.POST.get(
                                'test'):
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                count_all = User_Student_Test.objects.filter(user=request.user, sorag__sorag=model.sorag.id, ).count()
                count = User_Student_Test.objects.filter(user=request.user, sorag__sorag=model.sorag.id,
                                                         jogap_berdi=None).count()
                model.j_b_s_user = count_all - count
                model.ball = (model.d_j_b_s_count - (model.y_j_b_s_count // 4)) * 100 / count_all
                model.save()
                return HttpResponseRedirect(reverse('Test_end', args={sorag_id}))
            else:
                next_page = request.POST.get('next_page')
                succes = User_Student_Test.objects.get(id=page.object_list)
                if request.POST.get('test') != None:
                    if succes.jogap_berdi == None:
                        if succes.sorag.success == request.POST.get('test'):
                            model.d_j_b_s_count += 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                            print(11)
                        else:
                            model.y_j_b_s_count += 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                            print(10)
                    else:
                        if succes.sorag.success == succes.jogap_berdi and succes.sorag.success == request.POST.get(
                                'test'):
                            print(111)
                            pass
                        elif succes.sorag.success != succes.jogap_berdi and succes.sorag.success == request.POST.get(
                                'test'):
                            model.y_j_b_s_count -= 1
                            model.d_j_b_s_count += 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                            print(21)
                        elif succes.sorag.success == succes.jogap_berdi and succes.sorag.success != request.POST.get(
                                'test'):
                            model.y_j_b_s_count += 1
                            model.d_j_b_s_count -= 1
                            model.save()
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                            print(20)
                        elif succes.sorag.success != succes.jogap_berdi and succes.sorag.success != request.POST.get(
                                'test'):
                            succes.jogap_berdi = request.POST.get('test')
                            succes.save()
                count_all = User_Student_Test.objects.filter(user=request.user, sorag__sorag=model.sorag.id, ).count()
                count = User_Student_Test.objects.filter(user=request.user, sorag__sorag=model.sorag.id,
                                                         jogap_berdi=None).count()

                model.j_b_s_user = count_all - count
                model.ball = (model.d_j_b_s_count - (model.y_j_b_s_count // 4)) * 100 / count_all
                model.save()
                return HttpResponseRedirect(next_page)
        jogap_count = model.j_b_s_user
        jogap_pro = jogap_count * 100 / p.count
        context = {
            'page': page,
            'sorad_id': sorag_id,
            'count': p.count,
            'page_list': int(page_list),
            'jogap_count': jogap_count,
            'jogap_pro': int(jogap_pro),
            'date': date,
        }
        return render(request, 'Student/Test üçin/Test.html', context)
    else:
        raise Http404


@login_required()
def Test_end(request, pk):
    if request.user.user_type == '3':
        model = Student_Test.objects.get(id=pk)
        model.end_test = True
        model.e_date = datetime.datetime.now()
        model.save()
        return HttpResponseRedirect(reverse('Netijeler'))
    else:
        raise Http404


@login_required()
def Netijeler(request):
    if request.user.user_type == '3':
        models = Student_Test.objects.filter(user=request.user, end_test=True)
        user_page = request.GET.get('sahypa', 1)
        user_search = request.GET.get('search')
        p = Paginator(models, 11)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        if user_search:
            page = Student_Test.objects.filter(Q(sorag__name__icontains=user_search, user=request.user, end_test=True))
        context = {
            'page': page
        }
        return render(request, 'Student/Netijeler.html', context)
    else:
        raise Http404


@login_required()
def Testi_gormek(request, sorag_id):
    if request.user.user_type == '3':
        models = User_Student_Test.objects.filter(user=request.user, sorag__sorag=sorag_id)
        model = User_Student_Test.objects.filter(user=request.user, sorag__sorag=sorag_id).first()
        user_page = request.GET.get('sorag', 1)
        p = Paginator(models, 1)
        try:
            page = p.page(user_page)
        except:
            page = p.page(1)
        context = {
            'page': page,
            'sorag_id': model.sorag.sorag.id
        }
        return render(request, 'Student/Testi Görmek/Test.html', context)
    else:
        raise Http404


def Example(request):
    if request.user.user_type == '3':
        return render(request, 'Student/Test üçin/Test.html')
    else:
        raise Http404
