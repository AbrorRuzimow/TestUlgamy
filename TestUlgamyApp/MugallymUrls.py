from django.urls import path

from TestUlgamyApp.MugallymViews import *

urlpatterns = [
    path('',Dashboard,name='MugallymDashboard'),
    path('Testler',Testler,name='Testler'),
    path('Test_create',Test_create,name='Test_create'),
    path('Teste_soraglary_goshmak/<uuid:pk>',Teste_soraglary_goshmak,name='Teste_soraglary_goshmak'),
    path('Teste_soraglary_uytgetmek/<uuid:pk>/<sorag_id>',Teste_soraglary_uytgetmek,name='Teste_soraglary_uytgetmek'),
    path('Test_settings/<uuid:pk>',Test_settings,name='Test_settings'),
    path('Topar_SMS/<pk>',Topar_SMS,name='Topar_SMS'),
    path('Soraglar_SMS_Parol/<uuid:sorag>/<topar>',Soraglar_SMS_Parol,name='Soraglar_SMS_Parol'),
    path('Topar_Netije/<pk>',Topar_Netije,name='Topar_Netije'),
    path('Student_Netijeler/<uuid:sorag>/<topar>',Student_Netijeler,name='Student_Netijeler'),
    path('Show_Student_Test/<uuid:sorag_id>/<user>',Show_Student_Test,name='Show_Student_Test'),
]
