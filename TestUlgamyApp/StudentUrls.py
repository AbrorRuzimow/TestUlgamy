from django.urls import path

from TestUlgamyApp.StudentViews import StudentDashboard, Test, Parol_doret, Parol, Tests, Random_Test, Netijeler, \
    Test_end, Testi_gormek, Example

urlpatterns = [
    path('', StudentDashboard, name='StudentDashboard'),
    path('Tests',Tests,name='Tests'),
    path('Parol_doret/<uuid:test_id>/<student_id>',Parol_doret,name='Parol_doret'),
    path('Parol/<parol_id>',Parol,name='Parol'),
    path('Random_Test/<uuid:sorag_id>/<kod_id>',Random_Test,name='Random_Test'),
    path('Test/<uuid:sorag_id>',Test,name='Test'),
    path('Test_end/<uuid:pk>',Test_end,name='Test_end'),
    path('Netijeler',Netijeler,name='Netijeler'),
    path('Testi_gormek/<uuid:sorag_id>',Testi_gormek,name='Testi_gormek'),
    path('Example',Example,name='Example'),
]
