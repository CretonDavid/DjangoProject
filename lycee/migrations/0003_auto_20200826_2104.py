# Generated by Django 3.0.7 on 2020-08-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0002_callofroll_callofroll_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, verbose_name='call of roll date')),
                ('isAbsent', models.BooleanField(default=False)),
                ('reason', models.CharField(default='Unknown', max_length=255, null=True)),
                ('cursus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Cursus')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='callofroll_info',
            name='callofroll',
        ),
        migrations.RemoveField(
            model_name='callofroll_info',
            name='student',
        ),
        migrations.DeleteModel(
            name='CallOfRoll',
        ),
        migrations.DeleteModel(
            name='CallOfRoll_Info',
        ),
    ]