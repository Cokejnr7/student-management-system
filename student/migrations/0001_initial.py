# Generated by Django 4.1.7 on 2023-04-14 12:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import student.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_no', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('passport_img', models.ImageField(upload_to='passport/%Y/%m/%d', validators=[student.validators.is_image, student.validators.check_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.faculty')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.programme')),
            ],
        ),
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('title', models.CharField(choices=[('MR', 'mister'), ('MRS', 'missus'), ('MISS', 'misses')], max_length=200)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=50)),
                ('nationality', models.CharField(max_length=100)),
                ('state_of_origin', models.CharField(max_length=100)),
                ('local_government', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{11,15}$')])),
                ('next_of_kin', models.CharField(max_length=100)),
                ('kin_phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{11,15}$')])),
                ('name_of_sponsor', models.CharField(max_length=100)),
                ('sponsor_address', models.CharField(max_length=200)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
