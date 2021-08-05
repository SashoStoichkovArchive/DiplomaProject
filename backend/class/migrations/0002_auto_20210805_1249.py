# Generated by Django 3.2.6 on 2021-08-05 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'classes'},
        ),
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]