import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Users(AbstractUser):
    user_type_list = (
        (1, 'Administrator'),
        (2, 'Mugallym'),
        (3, 'Student')
    )
    user_type = models.CharField(choices=user_type_list,max_length=10, default=1, null=True)


class Admin_Profile(models.Model):
    admin = models.OneToOneField(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Toparlar(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Mugallym_Profile(models.Model):
    admin = models.OneToOneField(Users, on_delete=models.CASCADE)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Student_Profile(models.Model):
    admin = models.OneToOneField(Users, on_delete=models.CASCADE)
    topar = models.ForeignKey(Toparlar, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Sorag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000, null=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    sorag_count = models.IntegerField(default=0)
    sorag_min = models.IntegerField(default=0)
    b_5 = models.IntegerField(default=85)
    b_4 = models.IntegerField(default=70)
    b_3 = models.IntegerField(default=60)
    toparlar = models.ManyToManyField(Toparlar,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    yalnys = models.IntegerField(default=4)


class Soraglar(models.Model):
    name = models.TextField(null=True)
    sorag = models.ForeignKey(Sorag, on_delete=models.CASCADE)
    surat = models.ImageField(null=True, upload_to='Soraglar', blank=True)
    a = models.CharField(max_length=5000, null=True)
    b = models.CharField(max_length=5000, null=True)
    c = models.CharField(max_length=5000, null=True, blank=True)
    d = models.CharField(max_length=5000, null=True, blank=True)
    success = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student_Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    sorag = models.ForeignKey(Sorag, on_delete=models.CASCADE)
    j_b_s_user = models.IntegerField(default=0)
    d_j_b_s_count = models.IntegerField(default=0)
    y_j_b_s_count = models.IntegerField(default=0)
    ball = models.FloatField(default=0)
    s_date = models.DateTimeField(auto_now_add=True)
    e_date = models.DateTimeField(blank=True,null=True)
    e_max_date =models.DateTimeField(blank=True,null=True)
    end_test = models.BooleanField(default=False)


class User_Student_Test(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    sorag = models.ForeignKey(Soraglar, on_delete=models.CASCADE)
    jogap_berdi = models.CharField(max_length=10, null=True, blank=True)


class Sorag_Kod(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    sorag = models.ForeignKey(Sorag, on_delete=models.CASCADE)
    kod = models.IntegerField(null=True)
    start = models.BooleanField(default=False)
    ip = models.CharField(max_length=25,blank=True)
    date = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Users)
def create_user(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin_Profile.objects.create(admin=instance)
        if instance.user_type == 2:
            Mugallym_Profile.objects.create(admin=instance,kafedra=Kafedra.objects.get(id=1))
        if instance.user_type == 3:
            Student_Profile.objects.create(admin=instance, topar=Toparlar.objects.get(id=1))


@receiver(post_save, sender=Users)
def save_user(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin_profile.save()
    if instance.user_type == 2:
        instance.mugallym_profile.save()
    if instance.user_type == 3:
        instance.student_profile.save()