# Generated by Django 4.0.6 on 2022-08-10 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='index.movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
