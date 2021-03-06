# Generated by Django 2.0.1 on 2018-02-08 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import kvasaheim.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kvasaheim', '0002_auto_20171223_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=models.SET(kvasaheim.models.get_sentinel_user), related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_string', models.CharField(max_length=200)),
                ('numbers', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='answer',
        ),
        migrations.AddField(
            model_name='problem',
            name='equation',
            field=models.TextField(default='def solve(x):\n  return sum(x)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='num_rands_high',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='num_rands_low',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='random_high',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='random_low',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attempt',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='kvasaheim.ProblemInstance'),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(kvasaheim.models.get_sentinel_user), related_name='attempts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='probleminstance',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instance', to='kvasaheim.Problem'),
        ),
    ]
