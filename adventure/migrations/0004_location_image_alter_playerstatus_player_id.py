# Generated by Django 5.1.4 on 2024-12-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_playerstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='playerstatus',
            name='player_id',
            field=models.CharField(default='zXNn-Bn6nT', max_length=10, unique=True),
        ),
    ]