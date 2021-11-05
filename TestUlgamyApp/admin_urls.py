from django.urls import path

from TestUlgamyApp.AdminViews import *

urlpatterns = [
    path('',Dashboard,name='AdminDashboard'),
    path('Mugallym_List',Mugallym_List,name='Mugallym_List'),
    path('Mugallym_goshmak',Mugallym_goshmak,name='Mugallym_goshmak'),
    path('Mugallym_uytgetmek/<pk>',Mugallym_uytgetmek,name='Mugallym_uytgetmek'),
    path('Mugallym_delete/<pk>',Mugallym_delete,name='Mugallym_delete'),
    path('Student_List',Student_List,name='Student_List'),
    path('Student_goshmak',Student_goshmak,name='Student_goshmak'),
    path('Student_uytgetmek/<pk>',Student_uytgetmek,name='Student_uytgetmek'),
    path('Student_delete/<pk>',Student_delete,name='Student_delete'),
    path('All_Toparlar/',All_Toparlar,name='All_Toparlar'),
    path('Topar_goşmak',Topar_create,name='Topar_create'),
    path('Topar_üýtgetmek/<pk>',Topar_update,name='Topar_update'),
    path('Topar_delete/<pk>',Topar_delete,name='Topar_delete'),
    path('All_Kafedra/',All_Kafedra,name='All_Kafedra'),
    path('Kafedra_create',Kafedra_create,name='Kafedra_create'),
    path('Kafedra_update/<pk>',Kafedra_update,name='Kafedra_update'),
    path('Kafedra_delete/<pk>',Kafedra_delete,name='Kafedra_delete'),
]
