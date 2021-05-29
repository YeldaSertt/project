# Generated by Django 3.1.5 on 2021-05-29 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('author_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=100, verbose_name='Yazar Adı')),
            ],
        ),
        migrations.CreateModel(
            name='authority',
            fields=[
                ('yetki_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('admin', models.CharField(max_length=100)),
                ('users', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100, verbose_name='Kitap Adı')),
                ('sayfa_sayisi', models.IntegerField()),
                ('yayin_tarihi', models.DateTimeField(null=True)),
                ('image', models.CharField(max_length=200)),
                ('star', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=10000)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
            ],
        ),
        migrations.CreateModel(
            name='book_species',
            fields=[
                ('species_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('species_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('comment_admit', models.IntegerField(blank=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.CreateModel(
            name='persons',
            fields=[
                ('person_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('person_name', models.CharField(blank=True, max_length=100)),
                ('person_surname', models.CharField(blank=True, max_length=100)),
                ('mail_address', models.CharField(blank=True, max_length=100)),
                ('nick_name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('photo', models.CharField(max_length=200)),
                ('pasword', models.CharField(max_length=200)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.comment')),
                ('yetki_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.authority')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='species_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book_species'),
        ),
    ]
