# Generated by Django 5.0.6 on 2024-07-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_reyting_baholash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reyting',
            name='baholash',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
    ]
