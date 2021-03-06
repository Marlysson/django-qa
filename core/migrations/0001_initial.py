# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('conteudo', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField()),
                ('biografia', models.TextField(blank=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('pontos', models.IntegerField(blank=True, default=0, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('criada_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minhas_perguntas', to='core.Perfil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('conteudo', models.TextField()),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('mais_util', models.BooleanField(default=False)),
                ('criada_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minhas_respostas', to='core.Perfil')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='core.Pergunta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pergunta',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='core.Pergunta'),
        ),
    ]
