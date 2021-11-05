# Generated by Django 3.2.5 on 2021-10-23 09:39

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sorag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('sorag_count', models.IntegerField(default=0)),
                ('sorag_min', models.IntegerField(default=0)),
                ('b_5', models.IntegerField(default=85)),
                ('b_4', models.IntegerField(default=70)),
                ('b_3', models.IntegerField(default=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('yalnys', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Soraglar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('surat', models.ImageField(blank=True, null=True, upload_to='Soraglar')),
                ('a', models.CharField(max_length=5000, null=True)),
                ('b', models.CharField(max_length=5000, null=True)),
                ('c', models.CharField(blank=True, max_length=5000, null=True)),
                ('d', models.CharField(blank=True, max_length=5000, null=True)),
                ('success', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sorag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestUlgamyApp.sorag')),
            ],
        ),
        migrations.CreateModel(
            name='Toparlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Administrator'), (2, 'Mugallym'), (3, 'Student')], default=1, max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='User_Student_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogap_berdi', models.CharField(blank=True, max_length=10, null=True)),
                ('sorag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestUlgamyApp.soraglar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('j_b_s_user', models.IntegerField(default=0)),
                ('d_j_b_s_count', models.IntegerField(default=0)),
                ('y_j_b_s_count', models.IntegerField(default=0)),
                ('ball', models.FloatField(default=0)),
                ('s_date', models.DateTimeField(auto_now_add=True)),
                ('e_date', models.DateTimeField(auto_now=True)),
                ('e_max_date', models.DateTimeField()),
                ('end_test', models.BooleanField(default=False)),
                ('sorag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestUlgamyApp.sorag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestUlgamyApp.toparlar')),
            ],
        ),
        migrations.CreateModel(
            name='Sorag_Kod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.IntegerField(null=True)),
                ('start', models.BooleanField(default=False)),
                ('ip', models.CharField(blank=True, max_length=25)),
                ('date', models.DateTimeField(auto_now=True)),
                ('sorag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestUlgamyApp.sorag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sorag',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sorag',
            name='toparlar',
            field=models.ManyToManyField(blank=True, to='TestUlgamyApp.Toparlar'),
        ),
        migrations.CreateModel(
            name='Mugallym_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestUlgamyApp.kafedra')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
