# Generated by Django 4.2.1 on 2023-06-14 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnote', '0003_alter_runite_coefficient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='id',
        ),
        migrations.RemoveField(
            model_name='runite',
            name='id',
        ),
        migrations.RemoveField(
            model_name='unite',
            name='id',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='Netudiant',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='runite',
            name='code_ressource',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='unite',
            name='code',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='examens',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnote.etudiant'),
        ),
        migrations.AlterField(
            model_name='note',
            name='examens',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnote.examens'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.FloatField(max_length=4),
        ),
    ]
