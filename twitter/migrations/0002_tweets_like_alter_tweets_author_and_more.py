# Generated by Django 4.0.1 on 2022-01-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profilefield_biography'),
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='like',
            field=models.ManyToManyField(related_name='like', to='accounts.ProfileField', verbose_name='Like'),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='accounts.profilefield', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Posted on'),
        ),
    ]