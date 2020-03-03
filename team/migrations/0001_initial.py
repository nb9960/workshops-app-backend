# Generated by Django 2.2.6 on 2020-02-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('github_username', models.CharField(max_length=50)),
                ('github_image_url', models.URLField(null=True)),
            ],
        ),
    ]