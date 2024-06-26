# Generated by Django 4.2.7 on 2024-06-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrativeId', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suscription_points', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('video_url', models.URLField(max_length=100)),
                ('type_element', models.DateField()),
                ('elementPresnet_id', models.PositiveIntegerField()),
                ('elementVideo_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElementPresenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('expression', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ElementVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elementvideoId', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fechas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('publicationStatu_id', models.PositiveIntegerField()),
                ('administrative_id', models.PositiveIntegerField()),
                ('project_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('photo_url', models.URLField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('cover_url', models.URLField(max_length=100)),
                ('video_url', models.URLField(max_length=100)),
                ('statu', models.CharField(max_length=10)),
                ('presenter_id', models.PositiveIntegerField()),
                ('editor_id', models.PositiveIntegerField()),
                ('element_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PublicationStatu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('statu', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('type_user', models.CharField(max_length=10)),
                ('administartive_id', models.PositiveIntegerField()),
                ('editor_id', models.PositiveIntegerField()),
            ],
        ),
    ]
