# Generated by Django 2.2.6 on 2020-06-23 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatserver', '0011_auto_20200620_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.CharField(max_length=10000)),
                ('rom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatserver.roomId')),
            ],
        ),
    ]
