# Generated by Django 4.1.7 on 2023-04-22 07:47

from django.db import migrations, models
import django.db.models.deletion
import school.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbv', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.IntegerField()),
                ('programme_type', models.CharField(choices=[('undergraduate', 'Undergraduate'), ('postgraduate', 'Postgraduate')], max_length=30)),
                ('degree', models.CharField(max_length=150)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programmes', to='school.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='school.faculty'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
                ('semester', models.CharField(choices=[('first', 'First'), ('second', 'Second')], default='first', max_length=15)),
                ('level', models.IntegerField(validators=[school.validators.valid_level])),
                ('unit', models.IntegerField(validators=[school.validators.valid_unit])),
                ('description', models.TextField()),
                ('is_compulsory', models.BooleanField(default=True)),
                ('instructor', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='school.department')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='school.programme')),
            ],
        ),
    ]
