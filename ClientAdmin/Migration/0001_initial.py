

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('AdminID', models.AutoField(primary_key=True, serialize=False)),
                ('AdminName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('ClientID', models.AutoField(primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=500)),
                 ('ClientDOj', models.DateField()),
                ('ClientDept', models.CharField(max_length=500)),
               
                ('ClientFile', models.CharField(max_length=500)),
            ],
        ),
    ]