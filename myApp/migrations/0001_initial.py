# Generated by Django 4.2.6 on 2023-12-08 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('Currently_course', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=200)),
                ('MENTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=100)),
                ('MENTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.mentor')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('MENTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.mentor')),
                ('SESSION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.session')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('SESSION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.session')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('MENTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.mentor')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=200)),
                ('MENTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.mentor')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('complaint', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('FROM_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromid', to='myApp.login')),
                ('TO_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toid', to='myApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='App_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
        ),
    ]
