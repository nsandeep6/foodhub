# Generated by Django 5.0.2 on 2024-02-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=20)),
                ('usr_email', models.EmailField(max_length=254)),
                ('usr_phone_no', models.IntegerField()),
                ('usr_add', models.CharField(max_length=100)),
                ('pswd1', models.CharField(max_length=20)),
                ('pswd2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50)),
                ('vendor_email', models.EmailField(max_length=254)),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_license', models.ImageField(blank=True, upload_to='licimg')),
                ('shop_add', models.CharField(max_length=50)),
                ('shop_phone_no', models.IntegerField()),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]