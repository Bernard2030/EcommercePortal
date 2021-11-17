# Generated by Django 3.2.9 on 2021-11-17 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211115_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=11)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sms_messages', to='products.userprofile')),
            ],
        ),
    ]
