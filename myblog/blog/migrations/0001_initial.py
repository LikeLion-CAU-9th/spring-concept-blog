# Generated by Django 3.2.2 on 2021-05-10 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='제목', max_length=50)),
                ('show', models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE'), ('my', 'MY')], default='public', help_text='post_type', max_length=10)),
                ('body', models.TextField(help_text='내용')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, help_text='작성시간')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
