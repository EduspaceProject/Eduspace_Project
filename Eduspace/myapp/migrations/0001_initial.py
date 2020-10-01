# Generated by Django 3.1.1 on 2020-10-01 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_school', models.CharField(max_length=50)),
                ('sec_board', models.CharField(max_length=10)),
                ('sec_percent', models.IntegerField(max_length=10)),
                ('Int_school', models.CharField(max_length=50)),
                ('Int_board', models.CharField(max_length=10)),
                ('Int_percent', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('profile_img', models.ImageField(upload_to='user/profile_img/')),
                ('mobile', models.IntegerField(max_length=12)),
                ('emailid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user_login')),
            ],
        ),
        migrations.CreateModel(
            name='graduation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem1', models.IntegerField(default=0, max_length=10)),
                ('sem2', models.IntegerField(default=0, max_length=10)),
                ('sem3', models.IntegerField(default=0, max_length=10)),
                ('sem4', models.IntegerField(default=0, max_length=10)),
                ('sem5', models.IntegerField(default=0, max_length=10)),
                ('sem6', models.IntegerField(default=0, max_length=10)),
                ('sem7', models.IntegerField(default=0, max_length=10)),
                ('sem8', models.IntegerField(default=0, max_length=10)),
                ('emailid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.education_detail')),
            ],
        ),
        migrations.AddField(
            model_name='education_detail',
            name='emailid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
