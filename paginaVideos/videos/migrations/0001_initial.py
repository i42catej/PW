# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto_comentario', models.TextField(help_text=b'Comentario', verbose_name=b'Comentario')),
                ('fecha_comentario', models.DateTimeField(auto_now=True, verbose_name=b'Fecha del Comentario')),
                ('usuario_comentario', models.ForeignKey(verbose_name=b'Autor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_video', models.CharField(help_text=b'Titulo ', max_length=100, verbose_name=b'Titulo ')),
                ('descripcion_video', models.TextField(help_text=b'Descripcion ', verbose_name=b'Descripcion ')),
                ('keywords_video', models.TextField(help_text=b'Palabras de referencia', verbose_name=b'Palabras de referencia')),
                ('archivo_video', models.FileField(help_text=b'Seleccione un archivo', upload_to=b'videos', verbose_name=b'Seleccione un archivo')),
                ('fecha_video', models.DateTimeField(auto_now=True)),
                ('privacidad_video', models.BooleanField(default=False, help_text=b'Privado', verbose_name=b'Privado')),
                ('usuario_video', models.ForeignKey(verbose_name=b'Usuario ', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comentario',
            name='video_comentario',
            field=models.ForeignKey(to='videos.Video'),
            preserve_default=True,
        ),
    ]
