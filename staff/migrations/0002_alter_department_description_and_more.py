# Generated by Django 5.0.6 on 2024-06-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='staffcategory',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='staff_role',
            field=models.CharField(choices=[('form_teacher', 'form_teacher'), ('principal', 'principal'), ('head_teacher', 'head_teacher'), ('admin_officer', 'admin_officer'), ('account_officer', 'account_officer'), ('non_teaching', 'non_teaching'), ('others', 'others'), ('select', 'select')], default='select', max_length=20),
        ),
    ]