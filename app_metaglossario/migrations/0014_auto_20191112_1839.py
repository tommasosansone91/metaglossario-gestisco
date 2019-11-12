# Generated by Django 2.2.2 on 2019-11-12 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0013_auto_20191111_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='prepared_terminology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lemma', models.CharField(blank=True, max_length=256, null=True)),
                ('Acronimo', models.CharField(blank=True, max_length=25, null=True)),
                ('Definizione', models.TextField(blank=True, null=True)),
                ('Ambito_riferimento', models.CharField(blank=True, max_length=256, null=True)),
                ('Autore_definizione', models.TextField(blank=True, null=True)),
                ('Posizione_definizione', models.TextField(blank=True, null=True)),
                ('Url_definizione', models.URLField(blank=True, max_length=400, null=True)),
                ('Titolo_documento_fonte', models.TextField(blank=True, null=True)),
                ('Autore_documento_fonte', models.TextField(blank=True, null=True)),
                ('Host_documento_fonte', models.TextField(blank=True, null=True)),
                ('Url_documento_fonte', models.URLField(blank=True, max_length=400, null=True)),
                ('Commento_entry', models.TextField(blank=True, null=True)),
                ('Data_inserimento_entry', models.DateField(default=datetime.date(2019, 11, 12))),
                ('Id_statico_entry', models.CharField(default='ITCH00000', max_length=256)),
                ('Admin_approval_switch', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default=('hide', 'hide'), max_length=30)),
            ],
            options={
                'ordering': ['Admin_approval_switch', 'Lemma', 'Data_inserimento_entry', 'Id_statico_entry'],
            },
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 12)),
        ),
        migrations.AlterField(
            model_name='glossary_entry',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 12)),
        ),
        migrations.AlterField(
            model_name='glossary_file',
            name='Data_inserimento_glossary',
            field=models.DateField(default=datetime.date(2019, 11, 12)),
        ),
    ]
