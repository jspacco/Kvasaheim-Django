# Generated by Django 2.0.1 on 2018-06-22 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvasaheim', '0005_auto_20180517_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='kvasaheim.Category'),
            preserve_default=False,
        ),
    ]
