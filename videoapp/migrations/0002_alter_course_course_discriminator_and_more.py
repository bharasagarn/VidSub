# Generated by Django 4.2 on 2023-05-05 05:52

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_discriminator',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='course'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('roll_no', models.CharField(blank=True, max_length=3)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pro', models.BooleanField(default=False)),
                ('pro_expiry_date', models.DateTimeField(blank=True, null=True)),
                ('subscription_type', models.CharField(choices=[('F', 'FREE'), ('M', 'MONTHLY'), ('Y', 'YEARLY')], default='FREE', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_module_name', models.CharField(max_length=100)),
                ('course_module_description', ckeditor.fields.RichTextField()),
                ('video_url', models.URLField(max_length=300)),
                ('can_view', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.course')),
            ],
        ),
    ]
