# Generated by Django 4.1.3 on 2022-12-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('book_file', models.FileField(upload_to='files/')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('preview', models.ImageField(null=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='category.category')),
            ],
            options={
                'verbose_name': ('Book',),
                'verbose_name_plural': ('Books',),
            },
        ),
        migrations.CreateModel(
            name='BookImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='books.book')),
            ],
        ),
    ]
