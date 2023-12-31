# Generated by Django 4.2.7 on 2023-12-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_zamowienie_nazwa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Zalogowany',
        ),
        migrations.RemoveField(
            model_name='uzytkownik',
            name='powtorz_haslo',
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='imie',
            field=models.CharField(default='Unknown', max_length=35),
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='nazwisko',
            field=models.CharField(default='Unknown', max_length=40),
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='telefon',
            field=models.IntegerField(default=456456),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='email',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='haslo',
            field=models.CharField(default='Unknown', max_length=35),
        ),
    ]
