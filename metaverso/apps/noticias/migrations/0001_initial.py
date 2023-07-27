# Generated by Django 4.2.3 on 2023-07-25 23:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(blank=True, default='noticias/notice_default.png', null=True, upload_to='noticias')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.categoria')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=20)),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='noticias.noticia')),
            ],
        ),
    ]
